import pytest
from src.agent import (
    SupervisorAgent,
    AgentRouter,
    ConversationMemory,
    AgentCollaboration,
    Task,
    Result,
    JobSearchAgent,
    SalaryAnalyzerAgent,
    InterviewCoachAgent,
    ResumeOptimizerAgent,
)

@pytest.fixture
def agents():
    return [
        JobSearchAgent(),
        SalaryAnalyzerAgent(),
        InterviewCoachAgent(),
        ResumeOptimizerAgent(),
    ]

def test_supervisor_intent_recognition(agents):
    supervisor = SupervisorAgent(agents)
    intents = supervisor._identify_intents("我想找台北的 Python 工作並分析薪資")
    assert isinstance(intents, list)

def test_supervisor_task_decomposition(agents):
    supervisor = SupervisorAgent(agents)
    tasks = supervisor._decompose_tasks(["search_job", "analyze_salary"])
    assert isinstance(tasks, list)

def test_supervisor_agent_routing():
    router = AgentRouter()
    assert router.route("search_job") == "JobSearchAgent"
    assert router.route("analyze_salary") == "SalaryAnalyzerAgent"

def test_supervisor_result_integration(agents):
    supervisor = SupervisorAgent(agents)
    result = supervisor._integrate_results([{"output": "A"}, {"output": "B"}])
    assert isinstance(result, str)

def test_router_rule_based():
    router = AgentRouter()
    assert router.route_rule_based("search_job") == "JobSearchAgent"

def test_router_llm_based():
    router = AgentRouter()
    assert router.route_llm_based("unknown_intent") == "JobSearchAgent"

def test_conversation_memory():
    memory = ConversationMemory()
    memory.add_turn("hi", "hello")
    assert len(memory.get_recent_turns()) == 1

def test_multi_turn_conversation():
    memory = ConversationMemory()
    for i in range(10):
        memory.add_turn(f"user{i}", f"agent{i}")
    context = memory.get_context()
    assert "history" in context

import asyncio

@pytest.mark.asyncio
async def test_parallel_execution(agents):
    collab = AgentCollaboration()
    agent_map = {a.name: a for a in agents}
    tasks = [
        Task(task_id="1", intent="search_job", agent_name="JobSearchAgent", input_data={"task": "python"}),
        Task(task_id="2", intent="analyze_salary", agent_name="SalaryAnalyzerAgent", input_data={"task": "engineer"}),
    ]
    results = await collab.execute_parallel(tasks, agent_map)
    assert len(results) == 2

@pytest.mark.asyncio
async def test_sequential_execution(agents):
    collab = AgentCollaboration()
    agent_map = {a.name: a for a in agents}
    tasks = [
        Task(task_id="1", intent="search_job", agent_name="JobSearchAgent", input_data={"task": "python"}),
        Task(task_id="2", intent="analyze_salary", agent_name="SalaryAnalyzerAgent", input_data={"task": "engineer"}),
    ]
    results = await collab.execute_sequential(tasks, agent_map)
    assert len(results) == 2
