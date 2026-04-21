from dataclasses import dataclass

from mj_sapien.sim import backend


@dataclass(frozen=True)
class BaseEnvCfg:
    num_envs: int = 1
    sim_backend: backend.SimBackend = "mujoco_cpu"
    render_backend: backend.RenderBackend = "mujoco_warp"

class BaseEnv:
    def __init__(self, cfg: BaseEnvCfg):
        self.cfg = cfg