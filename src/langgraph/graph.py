from langgraph.graph import StateGraph, END
from .state import AgentState
from .nodes import (
    load_context_node,
    identify_intent_node,
    decompose_tasks_node,
    integrate_results_node,
    update_memory_node
)
from .agent_nodes import (
    job_search_node,
    salary_analyze_node,
    interview_coach_node,
    resume_optimize_node
)

def route_to_agents(state: AgentState) -> str:
    """根據意圖路由到相應的 Agent Node

    根據第一個任務的 intent 分流到不同 Agent 節點。
    """
    if not state["tasks"]:
        return "integrate_results"
    intent = state["tasks"][0].get("intent")
    intent_mapping = {
        "search_job": "job_search",
        "analyze_salary": "salary_analyze",
        "prepare_interview": "interview_coach",
        "optimize_resume": "resume_optimize"
    }
    return intent_mapping.get(intent, "integrate_results")

def create_workflow() -> StateGraph:
    """創建 LangGraph 工作流程

    Returns:
        未編譯的 StateGraph
    """
    workflow = StateGraph(AgentState)
    workflow.add_node("load_context", load_context_node)
    workflow.add_node("identify_intent", identify_intent_node)
    workflow.add_node("decompose_tasks", decompose_tasks_node)
    workflow.add_node("job_search", job_search_node)
    workflow.add_node("salary_analyze", salary_analyze_node)
    workflow.add_node("interview_coach", interview_coach_node)
    workflow.add_node("resume_optimize", resume_optimize_node)
    workflow.add_node("integrate_results", integrate_results_node)
    workflow.add_node("update_memory", update_memory_node)

    workflow.set_entry_point("load_context")
    workflow.add_edge("load_context", "identify_intent")
    workflow.add_edge("identify_intent", "decompose_tasks")
    workflow.add_conditional_edges(
        "decompose_tasks",
        route_to_agents,
        {
            "job_search": "job_search",
            "salary_analyze": "salary_analyze",
            "interview_coach": "interview_coach",
            "resume_optimize": "resume_optimize",
            "integrate_results": "integrate_results"
        }
    )
    workflow.add_edge("job_search", "integrate_results")
    workflow.add_edge("salary_analyze", "integrate_results")
    workflow.add_edge("interview_coach", "integrate_results")
    workflow.add_edge("resume_optimize", "integrate_results")
    workflow.add_edge("integrate_results", "update_memory")
    workflow.add_edge("update_memory", END)
    return workflow
