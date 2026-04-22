from dataclasses import dataclass
from typing import Any, NamedTuple

from mj_sapien.sim import backend

import torch
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

    ### Scene management and instantiation functions ###
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
    
    def _initialize_episode(self, env_idx: torch.Tensor):
        """
        Initialize the episode by setting the appropriate sim state for the environment
        """
        pass

    ### Observables ###
    def get_obs(self):
        """
        Retrieve the current observation of the environment
        """
        pass

    def evaluate(self) -> dict[str, Any]:
        """
        Evaluate the current state of the environment
        """
        return dict()

    ### Gymnasium style lifecycle functions ###
    def reset(self, options: ResetOptions | None = None):
        """
        Reset the environment. This internally calls `_initialize_episode` to reset the sim state.
        """
        if options is not None:
            if options["reconfigure"]:
                self._reconfigure()

        return self.get_obs(), self.evaluate()
        
    def step(self):
        pass

    def render(self):
        """
        Render the current state of the environment
        """
        pass

    ### Sim state management functions ###
    def get_state_dict(self) -> dict[str, Any]:
        """
        Get the current state of the environment as a dictionary
        """
        pass

    def set_state_dict(self, state_dict: dict[str, Any]):
        """
        Set the current state of the environment from a dictionary
        """
        pass