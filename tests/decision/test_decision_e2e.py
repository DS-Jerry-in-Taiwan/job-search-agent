import pytest
from src.decision.decision_agent import run_decision_agent

def simulate_upstream_resume_parser():
    # 模擬履歷解析與前置資料流
    return {
        "case_id": "e2e_case_01",
        "resume": {
            "skills": ["Python", "SQL"],
            "years_experience": 5,
            "preferences": {"location": "Taipei"}
        },
        "job": {
            "required_skills": ["Python", "SQL"],
            "min_experience": 3,
            "location": "Taipei"
        }
    }

def upstream_to_decision_input(upstream_data):
    # 根據上游資料流自動計算分數
    skill_match = 1.0 if set(upstream_data["resume"]["skills"]) >= set(upstream_data["job"]["required_skills"]) else 0.5
    experience_match = min(upstream_data["resume"]["years_experience"] / upstream_data["job"]["min_experience"], 1.0)
    preference_match = 1.0 if upstream_data["resume"]["preferences"]["location"] == upstream_data["job"]["location"] else 0.0
    raw_scores = {
        "skill_match": skill_match * 100,
        "experience_match": experience_match * 100,
        "preference_match": preference_match * 100
    }
    weights = {"skill": 0.5, "experience": 0.3, "preference": 0.2}
    return upstream_data["case_id"], raw_scores, weights

def test_decision_agent_e2e():
    upstream_data = simulate_upstream_resume_parser()
    case_id, raw_scores, weights = upstream_to_decision_input(upstream_data)
    result = run_decision_agent(case_id, raw_scores, weights, normalization_method="min-max")
    print("-----")
    print(result)  # 用於調試
    print("-----")
    assert result["case_id"] == case_id
    assert result["final_score"] >= 0.0 and result["final_score"] <= 1.0
    assert "action_plan" in result
    assert result["normalized_scores"]["skill"] == 1.0
    assert result["normalized_scores"]["experience"] == 1.0
    assert result["normalized_scores"]["preference"] == 1.0
