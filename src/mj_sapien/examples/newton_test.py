import newton


def main():

    # Build a model
    builder = newton.ModelBuilder()
    builder.add_mjcf("src/mj_sapien/assets/robots/franka_emika_panda/panda.xml")
    builder.add_ground_plane()
    model = builder.finalize()

    # Create a solver and allocate state
    solver = newton.solvers.SolverMuJoCo(model, njmax=100)
    state_0 = model.state()
    state_1 = model.state()
    control = model.control()
    contacts = model.contacts()

    newton.eval_fk(model, model.joint_q, model.joint_qd, state_0)
    viewer = newton.viewer.ViewerGL()
    viewer.begin_frame(0.0)
    viewer.end_frame()
    # Step the simulation
    for step in range(1000):
        print("step", step)
        state_0.clear_forces()
        model.collide(state_0, contacts)
        solver.step(state_0, state_1, control, contacts, 1.0 / 60.0 / 4.0)
        state_0, state_1 = state_1, state_0


if __name__ == "__main__":
    main()
