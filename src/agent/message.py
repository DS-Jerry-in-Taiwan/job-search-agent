from dataclasses import dataclass, asdict
from typing import Dict, Any
import time

@dataclass
class Message:
    sender: str
    receiver: str
    content: str
    type: str  # e.g. "task", "result", "error"
    metadata: Dict[str, Any]
    timestamp: float

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Message":
        return Message(
            sender=data["sender"],
            receiver=data["receiver"],
            content=data["content"],
            type=data["type"],
            metadata=data.get("metadata", {}),
            timestamp=data.get("timestamp", time.time())
        )
