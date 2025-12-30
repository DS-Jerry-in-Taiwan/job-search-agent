from typing import Dict, Optional
from .base import AgentBase

class AgentRegistry:
    _instance = None
    _agents: Dict[str, AgentBase] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def register(self, agent: AgentBase):
        self._agents[agent.name] = agent

    def get_agent(self, name: str) -> Optional[AgentBase]:
        return self._agents.get(name)

    def list_agents(self):
        return list(self._agents.keys())
