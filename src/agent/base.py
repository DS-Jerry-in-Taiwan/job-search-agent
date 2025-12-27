from abc import ABC, abstractmethod
from typing import List, Dict, Any
from .tool import Tool
from .memory import Memory

class AgentBase(ABC):
    def __init__(self, name: str, tools: List[Tool], memory: Memory):
        self.name = name
        self.tools = {tool.name: tool for tool in tools}
        self.memory = memory
        self.llm = None  # LLM client (Day 1)

    @abstractmethod
    def run(self, task: str, context: Dict) -> str:
        """子類需實現具體邏輯"""
        pass

    def call_tool(self, tool_name: str, **kwargs) -> Any:
        if tool_name not in self.tools:
            raise ValueError(f"Tool '{tool_name}' not found in agent '{self.name}'")
        return self.tools[tool_name].run(**kwargs)

    def remember(self, message: str):
        self.memory.add(role="agent", content=message)

    def recall(self, query: str) -> List[str]:
        # 回傳相關記憶內容（可擴充語意檢索）
        return [item["content"] for item in self.memory.search(query)]
