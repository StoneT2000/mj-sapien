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