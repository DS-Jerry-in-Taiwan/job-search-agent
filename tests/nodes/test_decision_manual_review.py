import pytest
from src.nodes.decision import decision_node

def test_decision_manual_review_pending_message():
    # 準備一個 state，模擬人工審核 pending 狀態
    state = {
        "system": {
            "manual_review_status": "pending"
        },
        "conversation": {
            "messages": []
        },
        "next_action": ""
    }
    result = decision_node(state)
    # 應該 return，且 messages 有通知
    assert result["system"]["manual_review_status"] == "pending"
    assert any(
        m["content"].startswith("請稍候，人工審核中") for m in result["conversation"]["messages"]
    )

def test_decision_manual_review_next_action():
    # 準備一個 state，模擬剛要進入人工審核
    state = {
        "system": {},
        "conversation": {
            "messages": []
        },
        "next_action": "manual_review"
    }
    result = decision_node(state)
    # 應該直接 return，next_action 不變
    assert result["next_action"] == "manual_review"
    assert result["conversation"]["messages"] == []

def test_decision_normal_flow():
    # 準備一個 state，走正常流程
    state = {
        "system": {},
        "conversation": {
            "messages": [],
            "current_intent": "general",
            "context": {},
            "history_summary": "",
            "turn_count": 0
        },
        "user_profile": {"parsed_at": None},
        "job_state": {"matched_jobs": [], "status": ""},
        "next_action": ""
    }
    result = decision_node(state)
    # 應該設定 next_action 為 resume_parser
    assert result["next_action"] == "resume_parser"

