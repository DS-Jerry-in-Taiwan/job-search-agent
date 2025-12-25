from typing import Dict, Any
from .schema import AgentState, UserProfileState, JobState, ConversationState, SystemState
from datetime import datetime

def create_empty_user_profile() -> UserProfileState:
    """建立空的 UserProfileState"""
    return {
        "user_id": "",
        "resume_text": "",
        "skills": [],
        "experience_years": 0,
        "education": "",
        "preferences": {},
        "parsed_at": datetime.now()
    }

def create_empty_job_state() -> JobState:
    """建立空的 JobState"""
    return {
        "status": "uninitialized",
        # "jobs": [],
        "matched_jobs": [],
        "match_scores": {},
        "recommendations": [],
        "last_updated": datetime.now()
    }

def create_empty_conversation_state() -> ConversationState:
    """建立空的 ConversationState"""
    return {
        "messages": [],
        "current_intent": "",
        "context": {},
        "history_summary": "",
        "turn_count": 0
    }

def create_initial_system_state() -> SystemState:
    """建立初始 SystemState"""
    return {
        "current_node": "start",
        "workflow_status": "initialized",
        "error_message": None,
        "retry_count": 0,
        "metadata": {}
    }

def create_initial_state() -> AgentState:
    """建立初始 AgentState"""
    return {
        "user_profile": create_empty_user_profile(),
        "job_state": create_empty_job_state(),
        "conversation": create_empty_conversation_state(),
        "system": create_initial_system_state(),
        "next_action": "start",
        "is_complete": False
    }

def update_user_profile(state: AgentState, updates: Dict[str, Any]) -> AgentState:
    """更新 UserProfileState"""
    updated_profile = {**state["user_profile"], **updates}
    return {**state, "user_profile": updated_profile}

def update_job_state(state: AgentState, updates: Dict[str, Any]) -> AgentState:
    """更新 JobState"""
    updated_job = {**state["job_state"], **updates}
    return {**state, "job_state": updated_job}

def update_conversation_state(state: AgentState, updates: Dict[str, Any]) -> AgentState:
    """更新 ConversationState"""
    updated_conv = {**state["conversation"], **updates}
    return {**state, "conversation": updated_conv}

def update_system_state(state: AgentState, updates: Dict[str, Any]) -> AgentState:
    """更新 SystemState"""
    updated_sys = {**state["system"], **updates}
    return {**state, "system": updated_sys}
