from typing import List, Dict, Any
from dataclasses import dataclass, field
import time

@dataclass
class Turn:
    user_msg: str
    agent_msg: str
    timestamp: float = field(default_factory=time.time)
    metadata: Dict[str, Any] = field(default_factory=dict)

class ConversationMemory:
    def __init__(self, max_turns: int = 20):
        self.turns: List[Turn] = []
        self.max_turns = max_turns

    def add_turn(self, user_msg: str, agent_msg: str, metadata: Dict[str, Any] = None):
        turn = Turn(user_msg, agent_msg, metadata=metadata or {})
        self.turns.append(turn)
        if len(self.turns) > self.max_turns:
            self.turns.pop(0)

    def get_recent_turns(self, n: int = 5) -> List[Turn]:
        return self.turns[-n:]

    def get_context(self) -> Dict:
        # 提取最近對話上下文
        return {
            "history": [
                {"user": t.user_msg, "agent": t.agent_msg, "time": t.timestamp}
                for t in self.get_recent_turns()
            ]
        }
