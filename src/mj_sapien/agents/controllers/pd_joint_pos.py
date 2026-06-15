from typing import Any
from mj_sapien.agents.controllers.base_controller import BaseController, BaseControllerConfig
from dataclasses import dataclass

import torch

@dataclass(frozen=True)
class PDJointPosControllerConfig(BaseControllerConfig):
    normalize: bool = True
    delta: bool = False

class PDJointPosController(BaseController):
    has_state: bool = False

    def _preprocess_action(self, action: torch.Tensor) -> torch.Tensor:
        return super()._preprocess_action(action)