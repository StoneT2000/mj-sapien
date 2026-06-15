from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass(frozen=True)
class BaseSceneConfig:
    pass

class BaseScene(ABC):

    def __init__(self, cfg: BaseSceneConfig):
        self.cfg = cfg
        pass

    @property
    def can_render(self) -> bool:
        """
        Whether the scene can render.
        """
        raise NotImplementedError()

    ### Building and scene compilation functions ###
    @abstractmethod
    def add_builder(self, builder):
        """
        Add a builder to the scene, which is used to construct a part of the scene
        """
        pass

    @abstractmethod
    def finalize(self):
        """
        Finalize the scene and compile it, ready for simulation/rendering
        """

    ### Simulation functions ###
    @abstractmethod
    def step(self):
        """
        Step the scene forward by one simulation step.
        """
        raise NotImplementedError("Step function not implemented for this scene type")