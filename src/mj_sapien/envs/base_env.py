from dataclasses import dataclass
from typing import NamedTuple

from mj_sapien.sim import backend


@dataclass(frozen=True)
class BaseEnvCfg:
    num_envs: int = 1
    sim_backend: backend.SimBackend = "mujoco_cpu"
    render_backend: backend.RenderBackend = "mujoco_warp"


class ResetOptions(NamedTuple):
    reconfigure: bool = False


class BaseEnv:
    def __init__(self, cfg: BaseEnvCfg):
        self.cfg = cfg

    def _load_scene(self):
        """
        Loads all scene rigid bodies, articulations etc.
        """
        pass

    def _reconfigure(self):
        """
        Reconfigures the environment. This is essentially equivalent to deleting the environment
        and calling all relevant functions such as `_load_scene`
        """
        pass

    def get_obs(self):
        """
        Retrieve the current observation of the environment
        """
        pass

    def reset(self, options: ResetOptions | None = None):
        """
        Reset the environment. This internally calls `_initialize_episode` to reset the sim state.
        """
        pass

    def step(self):
        pass

    def render(self):
        """
        Render the current state of the environment
        """
        pass
