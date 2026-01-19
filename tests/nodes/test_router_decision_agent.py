import pytest
from src.nodes.router import router_node

def make_state(skill_score, exp_score, pref_score):
    return {
        "user_profile": {
            "parsed_at": "2025-12-31T00:00:00",
            "skill_score": skill_score,
            "exp_score": exp_score,
            "pref_score": pref_score
        },
        "job_state": {
            "matched_jobs": ["job1"],
            "status": "active"
        },
        "conversation": {
            "current_intent": "general",
            "turn_count": 0
        },
        "system": {},
        "session_id": "test_session"
    }

def test_router_decision_high_score():
    # 三個分數都高且相等，min-max 正規化後皆為 1.0，final_score = 1.0
    state = make_state(90, 90, 90)
    out = router_node(state)
    assert out["decision_result"]["final_score"] == 1.0
    assert out["next_action"] == "skill_analyzer"

def test_router_decision_mid_score():
    # 一高兩中，最高為 1.0，其餘為 0.0，final_score = 0.5
    state = make_state(80, 60, 60)
    out = router_node(state)
    assert abs(out["decision_result"]["final_score"] - 0.5) < 1e-6
    assert out["next_action"] == "apply_job"

def test_router_decision_low_score():
    # 一高兩低，最高為 1.0，其餘為 0，final_score = 0.5
    state = make_state(90, 30, 30)
    out = router_node(state)
    assert abs(out["decision_result"]["final_score"] - 0.5) < 1e-6
    assert out["next_action"] == "apply_job"

def test_router_decision_very_low_score():
    # 兩低一中，最高為 1.0，其餘為 0，final_score = 0.5
    state = make_state(30, 10, 10)
    out = router_node(state)
    assert abs(out["decision_result"]["final_score"] - 0.5) < 1e-6
    assert out["next_action"] == "apply_job"
