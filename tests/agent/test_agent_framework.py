import pytest
from src.agent import AgentBase, Tool, Memory, Message, AgentRegistry

class DummyAgent(AgentBase):
    def run(self, task: str, context: dict) -> str:
        return f"Task: {task}, Context: {context}"

def dummy_func(x: int, y: int) -> int:
    return x + y

def test_agent_base_init():
    agent = DummyAgent(name="test", tools=[], memory=Memory())
    assert agent.name == "test"
    assert isinstance(agent.memory, Memory)

def test_tool_creation_and_execution():
    tool = Tool(
        name="add",
        func=dummy_func,
        description="Add two numbers",
        parameters={"x": (int, ...), "y": (int, ...)}
    )
    result = tool.run(x=2, y=3)
    assert result == 5

def test_memory_add_and_retrieve():
    memory = Memory()
    memory.add("user", "hello")
    memory.add("agent", "hi")
    recent = memory.get_recent(2)
    assert len(recent) == 2
    assert recent[0]["content"] == "hello"
    assert recent[1]["content"] == "hi"

def test_memory_search():
    memory = Memory()
    memory.add("user", "find python job")
    memory.add("agent", "python job found")
    memory.add("user", "find java job")
    results = memory.search("python")
    assert len(results) == 2

def test_message_protocol():
    msg = Message(
        sender="A",
        receiver="B",
        content="hello",
        type="task",
        metadata={},
        timestamp=123.0
    )
    d = msg.to_dict()
    msg2 = Message.from_dict(d)
    assert msg2.sender == "A"
    assert msg2.receiver == "B"
    assert msg2.content == "hello"
    assert msg2.type == "task"

def test_agent_registry():
    agent = DummyAgent(name="test", tools=[], memory=Memory())
    registry = AgentRegistry()
    registry.register(agent)
    assert registry.get_agent("test") is agent
    assert "test" in registry.list_agents()

def test_tool_calling():
    tool = Tool(
        name="add",
        func=dummy_func,
        description="Add two numbers",
        parameters={"x": (int, ...), "y": (int, ...)}
    )
    agent = DummyAgent(name="test", tools=[tool], memory=Memory())
    result = agent.call_tool("add", x=1, y=2)
    assert result == 3

def test_agent_extensibility():
    class CustomAgent(AgentBase):
        def run(self, task: str, context: dict) -> str:
            return "custom"
    agent = CustomAgent(name="custom", tools=[], memory=Memory())
    assert agent.run("t", {}) == "custom"
