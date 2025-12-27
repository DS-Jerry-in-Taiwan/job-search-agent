"""Agent Node 實現

將 Day 3 的專業 Agent 包裝為 LangGraph Node。
設計參考: docs/langgraph/AGENT_NODE_DESIGN.md
"""

from typing import Dict, Any
from datetime import datetime

from src.agent.agents.job_search_agent import JobSearchAgent
from src.agent.agents.salary_analyzer_agent import SalaryAnalyzerAgent
from src.agent.agents.interview_coach_agent import InterviewCoachAgent
from src.agent.agents.resume_optimizer_agent import ResumeOptimizerAgent
from .state import AgentState

def job_search_node(state: AgentState) -> AgentState:
    """JobSearch Agent Node

    包裝 JobSearchAgent，執行職缺搜尋任務。
    """
    agent = JobSearchAgent()
    tasks = [t for t in state["tasks"] if t.get("intent") == "search_job"]

    if not tasks:
        return state

    for task in tasks:
        try:
            result = agent.run(task)
            state["results"].append({
                "agent": "JobSearchAgent",
                "intent": "search_job",
                "result": result,
                "timestamp": datetime.now().isoformat(),
                "status": "success"
            })
        except Exception as e:
            state["error"] = f"JobSearchAgent error: {str(e)}"
            state["results"].append({
                "agent": "JobSearchAgent",
                "intent": "search_job",
                "status": "failed",
                "error": str(e)
            })

    return state

def salary_analyze_node(state: AgentState) -> AgentState:
    """SalaryAnalyzer Agent Node

    包裝 SalaryAnalyzerAgent，執行薪資分析任務。
    """
    agent = SalaryAnalyzerAgent()
    tasks = [t for t in state["tasks"] if t.get("intent") == "analyze_salary"]

    if not tasks:
        return state

    for task in tasks:
        try:
            result = agent.run(task)
            state["results"].append({
                "agent": "SalaryAnalyzerAgent",
                "intent": "analyze_salary",
                "result": result,
                "timestamp": datetime.now().isoformat(),
                "status": "success"
            })
        except Exception as e:
            state["error"] = f"SalaryAnalyzerAgent error: {str(e)}"
            state["results"].append({
                "agent": "SalaryAnalyzerAgent",
                "intent": "analyze_salary",
                "status": "failed",
                "error": str(e)
            })

    return state

def interview_coach_node(state: AgentState) -> AgentState:
    """InterviewCoach Agent Node

    包裝 InterviewCoachAgent，執行面試輔導任務。
    """
    agent = InterviewCoachAgent()
    tasks = [t for t in state["tasks"] if t.get("intent") == "prepare_interview"]

    if not tasks:
        return state

    for task in tasks:
        try:
            result = agent.run(task)
            state["results"].append({
                "agent": "InterviewCoachAgent",
                "intent": "prepare_interview",
                "result": result,
                "timestamp": datetime.now().isoformat(),
                "status": "success"
            })
        except Exception as e:
            state["error"] = f"InterviewCoachAgent error: {str(e)}"
            state["results"].append({
                "agent": "InterviewCoachAgent",
                "intent": "prepare_interview",
                "status": "failed",
                "error": str(e)
            })

    return state

def resume_optimize_node(state: AgentState) -> AgentState:
    """ResumeOptimizer Agent Node

    包裝 ResumeOptimizerAgent，執行履歷優化任務。
    """
    agent = ResumeOptimizerAgent()
    tasks = [t for t in state["tasks"] if t.get("intent") == "optimize_resume"]

    if not tasks:
        return state

    for task in tasks:
        try:
            result = agent.run(task)
            state["results"].append({
                "agent": "ResumeOptimizerAgent",
                "intent": "optimize_resume",
                "result": result,
                "timestamp": datetime.now().isoformat(),
                "status": "success"
            })
        except Exception as e:
            state["error"] = f"ResumeOptimizerAgent error: {str(e)}"
            state["results"].append({
                "agent": "ResumeOptimizerAgent",
                "intent": "optimize_resume",
                "status": "failed",
                "error": str(e)
            })

    return state
