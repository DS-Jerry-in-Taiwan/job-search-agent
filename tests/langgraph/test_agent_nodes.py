"""Agent Node 測試"""

import pytest
from src.langgraph.state import AgentState
from src.langgraph.agent_nodes import (
    job_search_node,
    salary_analyze_node,
    interview_coach_node,
    resume_optimize_node
)

def test_job_search_node():
    """測試 job_search_node"""
    state = AgentState(
        messages=[],
        query="找台北的 Python 工程師職缺",
        session_id="test_session",
        user_id="test_user",
        intents=["search_job"],
        tasks=[{
            "intent": "search_job",
            "query": "找台北的 Python 工程師職缺",
            "params": {"location": "台北", "skill": "Python"}
        }],
        current_agent="",
        results=[],
        context={},
        final_response="",
        error="",
        retry_count=0
    )
    result_state = job_search_node(state)
    assert len(result_state["results"]) > 0
    assert result_state["results"][0]["agent"] == "JobSearchAgent"
    assert result_state["results"][0]["intent"] == "search_job"

def test_salary_analyze_node():
    """測試 salary_analyze_node"""
    state = AgentState(
        messages=[],
        query="台北 Python 工程師薪資多少",
        session_id="test_session",
        user_id="test_user",
        intents=["analyze_salary"],
        tasks=[{
            "intent": "analyze_salary",
            "query": "台北 Python 工程師薪資多少",
            "params": {"location": "台北", "skill": "Python"}
        }],
        current_agent="",
        results=[],
        context={},
        final_response="",
        error="",
        retry_count=0
    )
    result_state = salary_analyze_node(state)
    assert len(result_state["results"]) > 0
    assert result_state["results"][0]["agent"] == "SalaryAnalyzerAgent"
    assert result_state["results"][0]["intent"] == "analyze_salary"

def test_interview_coach_node():
    """測試 interview_coach_node"""
    state = AgentState(
        messages=[],
        query="面試技巧與準備",
        session_id="test_session",
        user_id="test_user",
        intents=["prepare_interview"],
        tasks=[{
            "intent": "prepare_interview",
            "query": "面試技巧與準備",
            "params": {}
        }],
        current_agent="",
        results=[],
        context={},
        final_response="",
        error="",
        retry_count=0
    )
    result_state = interview_coach_node(state)
    assert len(result_state["results"]) > 0
    assert result_state["results"][0]["agent"] == "InterviewCoachAgent"
    assert result_state["results"][0]["intent"] == "prepare_interview"

def test_resume_optimize_node():
    """測試 resume_optimize_node"""
    state = AgentState(
        messages=[],
        query="履歷優化建議",
        session_id="test_session",
        user_id="test_user",
        intents=["optimize_resume"],
        tasks=[{
            "intent": "optimize_resume",
            "query": "履歷優化建議",
            "params": {}
        }],
        current_agent="",
        results=[],
        context={},
        final_response="",
        error="",
        retry_count=0
    )
    result_state = resume_optimize_node(state)
    assert len(result_state["results"]) > 0
    assert result_state["results"][0]["agent"] == "ResumeOptimizerAgent"
    assert result_state["results"][0]["intent"] == "optimize_resume"
