import pytest
from src.state.operations import create_initial_state
from src.nodes.utils import recommendation_node

def test_recommendation_node_basic():
    """測試推薦理由產生"""
    state = create_initial_state()
    # 模擬已匹配職缺與分數
    state["job_state"]["matched_jobs"] = [
        {"id": "job_001", "title": "AI工程師"},
        {"id": "job_002", "title": "後端工程師"},
    ]
    state["job_state"]["match_scores"] = {
        "job_001": 0.85,
        "job_002": 0.6,
    }
    result = recommendation_node(state)
    assert len(result["job_state"]["recommendations"]) == 2
    assert "AI工程師" in result["job_state"]["recommendations"][0]
    assert "85%" in result["job_state"]["recommendations"][0]
    assert result["system"]["current_node"] == "recommendation"

def test_recommendation_node_empty():
    """測試無匹配職缺時推薦為空"""
    state = create_initial_state()
    state["job_state"]["matched_jobs"] = []
    state["job_state"]["match_scores"] = {}
    result = recommendation_node(state)
    assert result["job_state"]["recommendations"] == []
    assert result["system"]["current_node"] == "recommendation"
