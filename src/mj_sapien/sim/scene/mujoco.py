from mj_sapien.sim.scene import BaseScene, BaseSceneConfig
from dataclasses import dataclass

@dataclass(frozen=True)
class MujocoSceneConfig(BaseSceneConfig):
    pass

class MujocoScene(BaseScene):
    def __init__(self, cfg: MujocoSceneConfig):
        super().__init__(cfg)

    def step(self, dt):
        mujoco.mj_step(self.model, self.data, dt)