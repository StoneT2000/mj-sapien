from mj_sapien.agents.robots.franka_research_3.robot import FrankaResearch3Robot
from mj_sapien.envs.base_env import BaseEnv, BaseEnvConfig
import newton
import warp as wp

class PickCubeTaskConfig(BaseEnvConfig):
    pass


class PickCubeTask(BaseEnv):
    def __init__(self, cfg: PickCubeTaskConfig):
        super().__init__(cfg)

    def _load_scene(self):
        # self.scene.add_builder(builder)
        # self.scene = newton.ModelBuilder()
        builder = newton.ModelBuilder()
        body = builder.add_body(
            xform=wp.transform(wp.vec3(0.6, 0.0, 0.1), wp.quat_identity()),
        )
        builder.add_shape_box(
            body=body,
            hx=0.025,
            hy=0.025,
            hz=0.025,
            cfg=newton.ModelBuilder.ShapeConfig(mu=0.3),
        )
        self.scene.add_builder(builder)
        self.body = len(self.scene._newton_scene.body_q) - 1
        builder = newton.ModelBuilder()
        builder.add_ground_plane(cfg=newton.ModelBuilder.ShapeConfig(mu=0.3))
        self.scene.add_builder(builder)

    def _load_agent(self):
        robot = FrankaResearch3Robot()
        # create the initial builder for our pre-built robot
        builder = robot._load()
        # you can modify builder or robot for your specific task before adding to scene and returning it
        self.scene.add_builder(builder)
        return robot 
    def get_obs(self):
        return dict(cube_pos=self.scene.state_0.body_q.numpy()[self.body, :3])