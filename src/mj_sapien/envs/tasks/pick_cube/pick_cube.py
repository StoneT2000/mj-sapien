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
        self.robot = FrankaResearch3Robot()
        builder = self.robot._load_agent()
        self.scene.add_builder(builder)

        builder = newton.ModelBuilder()
        builder.add_shape_box(
            body=-1,
            hx=0.02,
            hy=0.02,
            hz=0.02,
            xform=wp.transform(wp.vec3(0, 0, 0), wp.quat_identity()),
            cfg=newton.ModelBuilder.ShapeConfig(mu=0.3),
        )
        self.scene.add_builder(builder)
        builder = newton.ModelBuilder()
        builder.add_ground_plane(cfg=newton.ModelBuilder.ShapeConfig(mu=0.3))
        self.scene.add_builder(builder)