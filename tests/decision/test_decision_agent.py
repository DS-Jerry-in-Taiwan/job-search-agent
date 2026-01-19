import pytest
from src.decision.decision_agent import run_decision_agent

def test_decision_agent_min_max():
    case_id = "case001"
    raw_scores = {"skill_match": 60, "experience_match": 80, "preference_match": 70}
    weights = {"skill": 0.5, "experience": 0.3, "preference": 0.2}
    result = run_decision_agent(case_id, raw_scores, weights, normalization_method="min-max")
    assert result["case_id"] == case_id
    # 期望值修正：根據 min-max 計算，應為 0.4
    assert abs(result["final_score"] - 0.4) < 1e-6
    assert result["normalization_method"] == "min-max"
    assert "action_plan" in result

def test_decision_agent_z_score():
    case_id = "case002"
    raw_scores = {"skill_match": 60, "experience_match": 80, "preference_match": 70}
    weights = {"skill": 0.5, "experience": 0.3, "preference": 0.2}
    result = run_decision_agent(case_id, raw_scores, weights, normalization_method="z-score")
    assert result["case_id"] == case_id
    assert result["normalization_method"] == "z-score"
    assert "action_plan" in result

def test_decision_agent_softmax():
    case_id = "case003"
    raw_scores = {"skill_match": 60, "experience_match": 80, "preference_match": 70}
    weights = {"skill": 0.5, "experience": 0.3, "preference": 0.2}
    result = run_decision_agent(case_id, raw_scores, weights, normalization_method="softmax")
    assert result["case_id"] == case_id
    assert result["normalization_method"] == "softmax"
    assert "action_plan" in result

def test_decision_agent_ratio():
    case_id = "case004"
    raw_scores = {"skill_match": 60, "experience_match": 80, "preference_match": 70}
    weights = {"skill": 0.5, "experience": 0.3, "preference": 0.2}
    result = run_decision_agent(case_id, raw_scores, weights, normalization_method="ratio")
    assert result["case_id"] == case_id
    assert result["normalization_method"] == "ratio"
    assert "action_plan" in result

def test_decision_agent_weight_normalization():
    case_id = "case005"
    raw_scores = {"skill_match": 60, "experience_match": 80, "preference_match": 70}
    weights = {"skill": 5, "experience": 3, "preference": 2}
    result = run_decision_agent(case_id, raw_scores, weights)
    assert abs(sum(result["weights"].values()) - 1.0) < 1e-6

def test_decision_agent_action_plan_custom():
    case_id = "case006"
    raw_scores = {"skill_match": 60, "experience_match": 80, "preference_match": 70}
    weights = {"skill": 0.5, "experience": 0.3, "preference": 0.2}
    custom_plan = [
        {"step": "A", "description": "descA"},
        {"step": "B", "description": "descB"}
    ]
    result = run_decision_agent(case_id, raw_scores, weights, action_plan_steps=custom_plan)
    assert result["action_plan"] == custom_plan
