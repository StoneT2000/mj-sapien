from mj_sapien.agents.base_agent import BaseAgent
import newton
import warp as wp

class FrankaResearch3Robot(BaseAgent):

    def _load(self):
        builder = newton.ModelBuilder()
        builder.rigid_gap = 0.005
        newton.solvers.SolverMuJoCo.register_custom_attributes(builder)

        builder.add_urdf(
            newton.utils.download_asset("franka_emika_panda") / "urdf/fr3_franka_hand.urdf",
            xform=wp.transform(wp.vec3(0, 0, 0), wp.quat_identity()),
            floating=False,
            enable_self_collisions=False,
            parse_visuals_as_colliders=False,
        )

        builder.joint_q[:9] = [
            -3.6802115e-03,
            2.3901723e-02,
            3.6804110e-03,
            -2.3683236e00,
            -1.2918962e-04,
            2.3922248e00,
            7.8549200e-01,
            0.04,
            0.04,
        ]
        builder.joint_target_pos[:9] = builder.joint_q[:9]
        builder.joint_target_ke[:9] = [400, 400, 400, 400, 400, 400, 400, 100, 100]
        builder.joint_target_kd[:9] = [40, 40, 40, 40, 40, 40, 40, 10, 10]
        builder.joint_effort_limit[:9] = [87, 87, 87, 87, 12, 12, 12, 100, 100]
        builder.joint_armature[:9] = [0.3] * 4 + [0.11] * 3 + [0.15] * 2

        # Gravity compensation
        gravcomp_attr = builder.custom_attributes["mujoco:jnt_actgravcomp"]
        if gravcomp_attr.values is None:
            gravcomp_attr.values = {}
        for dof_idx in range(7):
            gravcomp_attr.values[dof_idx] = True

        gravcomp_body = builder.custom_attributes["mujoco:gravcomp"]
        if gravcomp_body.values is None:
            gravcomp_body.values = {}
        for body_idx in range(2, 14):
            gravcomp_body.values[body_idx] = 1.0

        solimp_attr = builder.custom_attributes.get("mujoco:geom_solimp")
        priority_attr = builder.custom_attributes.get("mujoco:geom_priority")
        if solimp_attr is not None and priority_attr is not None:
            if solimp_attr.values is None:
                solimp_attr.values = {}
            if priority_attr.values is None:
                priority_attr.values = {}
            for s, b in enumerate(builder.shape_body):
                if b in (12, 13):
                    solimp_attr.values[s] = (0.7, 0.95, 0.0001, 0.5, 2.0)
                    priority_attr.values[s] = 1

        return builder