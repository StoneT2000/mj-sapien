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

    def __init__(self, cfg: BaseAgentConfig):
        self.cfg = cfg

    def _load_agent(self):
        """
        Load a model of this agent into the environment
        """
        raise NotImplementedError()

    @property
    def controllers(self) -> dict[str, BaseController]:
        """
        Dictionary mapping controller ids to the controller objects
        """
        raise NotImplementedError()
