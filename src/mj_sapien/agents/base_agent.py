from dataclasses import dataclass

@dataclass(frozen=True)
class BaseAgentCfg:
    pass


class BaseAgent:
    """Base class for agents/robots. An agent/robot is an entity that can perform actions to interact with 
    the environment. Users implementing their own agents/robots should inherit from this class.
    """

    def __init__(self, cfg: BaseAgentCfg = BaseAgentCfg()):
        pass

    def _load_agent(self):
        """
        Load a model of this agent into the environment
        """
        raise NotImplementedError()