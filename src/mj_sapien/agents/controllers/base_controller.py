from dataclasses import dataclass
from typing import Any
import torch
from gymnasium.spaces import Space


@dataclass(frozen=True)
class BaseControllerConfig:
    stiffness: float | list[float]
    damping: float | list[float]


class BaseController:
    active_joint_indices: torch.Tensor
    """indices of active joints controlled in list of all joints of an articulation"""
    action_space: Space

    has_state: bool
    """Whether the controller maintains state"""

    def __init__(self, cfg: BaseControllerConfig):
        self.cfg = cfg

    @property
    def device(self) -> torch.device:
        """
        The device the controller is on.
        """
        pass

    def _preprocess_action(self, action: torch.Tensor) -> torch.Tensor:
        """
        Preprocess an action. By default the action is clipped to [-1, 1] and re-scaled to
        the action space low, high bounds
        """
    
    def before_simulation_step(self):
        """Called before each simulation step in one control step"""

    def get_state_dict(self) -> dict[str, Any]:
        """
        Get the current state of the controller as a dictionary
        """
        raise NotImplementedError()

    def set_state_dict(self, state_dict: dict[str, Any]):
        """
        Set the current state of the controller from a dictionary
        """
        raise NotImplementedError()

    def reset(self):
        """
        Reset the controller's state
        """
        raise NotImplementedError()
