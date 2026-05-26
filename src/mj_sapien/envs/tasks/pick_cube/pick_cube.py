from mj_sapien.envs.base_env import BaseEnv, BaseEnvCfg


class PickCubeTaskCfg(BaseEnvCfg):
    pass


class PickCubeTask(BaseEnv):
    def __init__(self, cfg: PickCubeTaskCfg):
        super().__init__(cfg)

    def _load_scene(self):
        pass

    def _reconfigure(self):
        pass

    def get_obs(self):
        pass
