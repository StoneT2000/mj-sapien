import newton
import warp as wp

class Scene:
    def __init__(self):
        pass

    ### Building and scene compilation functions ###
    def add_builder(self, builder):
        """
        Add a builder to the scene, which is used to construct a part of the scene
        """
        pass
    def finalize(self):
        """
        Finalize the scene and compile it, ready for simulation/rendering
        """

    ### Simulation functions ###
    def step(self):
        raise NotImplementedError("Step function not implemented for this scene type")


class NewtonScene(Scene):
    def __init__(self):
        super().__init__()
        self._newton_scene = newton.ModelBuilder()
        self.viewer = newton.viewer.ViewerGL(headless=False)
        self.sim_time = 0.0
        self.fps = 60
        self.frame_dt = 1.0 / self.fps
        self.sim_substeps = 16
        self.sim_dt = self.frame_dt / self.sim_substeps
        print(f"Sim dt: {self.sim_dt}, frame dt: {self.frame_dt}, fps: {self.fps}, sim substeps: {self.sim_substeps}")

    def add_builder(self, builder):
        self._newton_scene.add_builder(builder)

    def finalize(self):
        self._model = self._newton_scene.finalize()
        contact_max = 16384
        self._model.rigid_contact_max = contact_max
        self.collision_pipeline = newton.CollisionPipeline(
            self._model,
            # TODO (stao): understand and make notes on these choices
            reduce_contacts=True,
            rigid_contact_max=contact_max,
            broad_phase="nxn"
        )
        self.solver = newton.solvers.SolverMuJoCo(
            self._model,
            solver="newton",
            integrator="implicitfast",
            iterations=15,
            ls_iterations=100,
            nconmax=contact_max,
            njmax=contact_max * 2,
            cone="elliptic",
            impratio=50.0,
            use_mujoco_contacts=False,
        )

        self.state_0 = self._model.state()
        self.state_1 = self._model.state()
        self.control = self._model.control()
        self.contacts = self.collision_pipeline.contacts()
        wp.copy(wp.zeros(9), self._model.joint_q[:9])
        self.viewer.set_model(self._model)
        self.capture()

    def capture(self):
        self.graph = None
        self.graph_ik = None
        if wp.get_device().is_cuda:
            with wp.ScopedCapture() as capture:
                self._control_step()
            self.graph = capture.graph
            # with wp.ScopedCapture() as capture:
            #     self.ik_solver.step(self.joint_q_ik, self.joint_q_ik, iterations=self.ik_iters)
            # self.graph_ik = capture.graph

    def _control_step(self):
        self.collision_pipeline.collide(self.state_0, self.contacts)
        for _ in range(self.sim_substeps):
            self.state_0.clear_forces()
            self.viewer.apply_forces(self.state_0)
            self.solver.step(self.state_0, self.state_1, self.control, self.contacts, self.sim_dt)
            self.state_0, self.state_1 = self.state_1, self.state_0

    def step(self, action):
        if self.graph:
            wp.capture_launch(self.graph)
        else:
            self._control_step()
        self.sim_time += self.frame_dt
        

    def render(self):
        self.viewer.begin_frame(self.sim_time)
        self.viewer.log_state(self.state_0)
        self.viewer.log_contacts(self.contacts, self.state_0)
        self.viewer.end_frame()
