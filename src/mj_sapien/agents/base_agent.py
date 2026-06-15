from dataclasses import dataclass

from mj_sapien.agents.controllers.base_controller import BaseController


@dataclass(frozen=True)
class BaseAgentConfig:
    pass


class BaseAgent:
    """Base class for agents/robots. An agent/robot is an entity that can perform actions to
    interact with the environment. Users implementing their own agents/robots should inherit
    from this class.
    """

    controller: BaseController
    """the current active controller of the agent"""

    def __init__(self, cfg: BaseAgentConfig | None = None):
        self.cfg = cfg if cfg is not None else BaseAgentConfig()

    def _load(self):
        """
        Load a model of this agent into the environment by returning a builder
        """
        raise NotImplementedError()

    def reset(self):
        """
        Reset the agent's state if there is any.
        """
        return
        if self.controller.has_state:
            self.controller.reset()

    @property
    def controllers(self) -> dict[str, BaseController]:
        """
        Dictionary mapping controller ids to the controller objects
        """
        raise NotImplementedError()
