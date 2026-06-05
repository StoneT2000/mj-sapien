from dataclasses import dataclass

import torch
from gymnasium.spaces import Space


@dataclass(frozen=True)
class BaseControllerConfig:
    pass


class BaseController:
    active_joint_indices: torch.Tensor
    """indices of active joints controlled in list of all joints of an articulation"""
    action_space: Space

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
