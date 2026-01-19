import pytest
from src.langgraph.graph import state_graph, workflow_registry
from src.state.schema import AgentState

def make_full_state(user_message):
    return AgentState(
        user_profile={},
        job_state={},
        conversation={
            "current_intent": "general",
            "turn_count": 0,
            "context": {"user_message": user_message},
            "messages": []
        },
        system={},
        session_id="workflow_e2e"
    )

def test_workflow_e2e_high_score():
    resume_text = "3年Python工程師經驗，熟悉AI、JavaScript"
    state = make_full_state(resume_text)
    app = workflow_registry["default"].compile()
    result = app.invoke(state)
    assert "decision_result" in result
    assert result["decision_result"]["final_score"] >= 0.8
    assert result["is_complete"] or result["system"].get("workflow_status") == "completed"

def test_workflow_e2e_mid_score():
    resume_text = "2年Java工程師經驗，略懂AI"
    state = make_full_state(resume_text)
    app = workflow_registry["default"].compile()
    result = app.invoke(state)
    assert "decision_result" in result
    assert 0.4 <= result["decision_result"]["final_score"] < 0.8
    assert result["is_complete"] or result["system"].get("workflow_status") == "completed"
