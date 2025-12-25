import pytest
from src.state.operations import create_initial_state
from src.nodes.resume_parser import resume_parser_node
from src.nodes.job_matcher import job_matcher_node, calculate_match_score

def test_job_matcher_node():
    """測試職缺匹配節點"""
    state = create_initial_state()
    state = resume_parser_node(state)  # 先解析履歷
    result = job_matcher_node(state)
    assert result["job_state"]["matched_jobs"]
    assert result["job_state"]["match_scores"]
    assert len(result["job_state"]["jobs"]) > 0
    assert result["system"]["current_node"] == "job_matcher"

def test_calculate_match_score():
    """測試匹配分數計算"""
    user_skills = {"python", "docker"}
    job = {"job_id": "001", "requirements": "Python Docker Kubernetes"}
    score = calculate_match_score(user_skills, job)
    assert 0.0 <= score <= 1.0
    assert score > 0  # 應該有匹配
