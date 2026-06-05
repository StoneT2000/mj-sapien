from mj_sapien.agents.robots.franka_research_3.robot import FrankaResearch3Robot
from mj_sapien.envs.base_env import BaseEnv, BaseEnvCfg


class PickCubeTaskCfg(BaseEnvCfg):
    pass


class PickCubeTask(BaseEnv):
    def __init__(self, cfg: PickCubeTaskCfg):
        super().__init__(cfg)

    def _load_scene(self):
        self.robot = FrankaResearch3Robot()
        builder = self.robot._load_agent()
        self.scene.add_builder(builder)