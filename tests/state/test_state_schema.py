import pytest
from src.state.schema import AgentState
from src.state.operations import (
    create_initial_state,
    update_user_profile,
    update_job_state,
    update_conversation_state,
    update_system_state,
)

def test_create_initial_state():
    """測試初始化 AgentState"""
    state = create_initial_state()
    assert isinstance(state, dict)
    assert state["is_complete"] is False
    assert state["next_action"] == "start"
    assert isinstance(state["user_profile"], dict)
    assert isinstance(state["job_state"], dict)
    assert isinstance(state["conversation"], dict)
    assert isinstance(state["system"], dict)

def test_update_user_profile():
    """測試更新 UserProfileState"""
    state = create_initial_state()
    updated = update_user_profile(state, {
        "user_id": "test_user",
        "skills": ["Python", "AI"]
    })
    assert updated["user_profile"]["user_id"] == "test_user"
    assert "Python" in updated["user_profile"]["skills"]

def test_update_job_state():
    """測試更新 JobState"""
    state = create_initial_state()
    updated = update_job_state(state, {
        "jobs": [{"id": "job_001", "title": "AI Engineer"}],
        "match_scores": {"job_001": 0.85}
    })
    assert len(updated["job_state"]["jobs"]) == 1
    assert updated["job_state"]["match_scores"]["job_001"] == 0.85

def test_update_conversation_state():
    """測試更新 ConversationState"""
    state = create_initial_state()
    updated = update_conversation_state(state, {
        "current_intent": "apply_job",
        "turn_count": 1
    })
    assert updated["conversation"]["current_intent"] == "apply_job"
    assert updated["conversation"]["turn_count"] == 1

def test_update_system_state():
    """測試更新 SystemState"""
    state = create_initial_state()
    updated = update_system_state(state, {
        "current_node": "job_match",
        "workflow_status": "running",
        "retry_count": 2
    })
    assert updated["system"]["current_node"] == "job_match"
    assert updated["system"]["workflow_status"] == "running"
    assert updated["system"]["retry_count"] == 2
