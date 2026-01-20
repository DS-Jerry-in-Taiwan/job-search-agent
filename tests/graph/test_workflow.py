import pytest
from src.langgraph.graph import workflow_registry
from src.state.schema import AgentState

def make_full_state(user_message, next_action=None):
    state = AgentState(
        user_profile={
            "resume_path": "data/raw/resumes/Li-Yue-Jun-v4.pdf"
        },
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
    if next_action:
        state["next_action"] = next_action
    return state

def test_workflow_e2e_high_score():
    resume_text = "3年Python工程師經驗，熟悉AI、JavaScript"
    state = make_full_state(resume_text)
    app = workflow_registry["default"]
    result = app.invoke(state)
    print(result['next_action'])
    # 支援 decision_result 在 result["system"] 或 result["decision_result"]
    assert "decision_result" in result or ("system" in result and "decision_result" in result["system"])
    if "decision_result" in result:
        dr = result["decision_result"]
    elif "system" in result and "decision_result" in result["system"]:
        dr = result["system"]["decision_result"]
    else:
        dr = None
    assert dr is not None
    assert dr["final_score"] >= 0.8
    assert result.get("is_complete") or result["system"].get("workflow_status") in ("completed", "finished")

# def test_workflow_e2e_mid_score():
#     resume_text = "2年Java工程師經驗，略懂AI"
#     state = make_full_state(resume_text)
#     app = workflow_registry["default"]
#     result = app.invoke(state)
#     assert "decision_result" in result
#     assert 0.4 <= result["decision_result"]["final_score"] < 0.8
#     assert result["is_complete"] or result["system"].get("workflow_status") == "completed"

# def test_workflow_e2e_manual_review():
#     # 模擬流程需人工審核
#     state = make_full_state("這是一個需要人工審核的履歷", next_action="manual_review")
#     app = workflow_registry["default"]
#     result = app.invoke(state)
#     # 驗證流程進入 human_review_node 並等待外部觸發
#     assert result.get("system", {}).get("current_node") == "human_review_node"
#     assert result.get("system", {}).get("manual_review_status") in ("pending", None)
