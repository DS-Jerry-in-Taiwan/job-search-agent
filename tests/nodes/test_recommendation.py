import pytest
from src.nodes.recommendation import recommendation_node

def test_recommendation_node_pref_location():
    state = {
        "user_profile": {"preferences": {"location": "台北", "remote": True}},
        "job_state": {
            "matched_jobs": [
                {"id": "job_1", "location": "台北", "remote": True},
                {"id": "job_2", "location": "高雄", "remote": True},
                {"id": "job_3", "location": "台北", "remote": False},
                {"id": "job_4", "location": "新竹", "remote": False}
            ]
        },
        "system": {}
    }
    out = recommendation_node(state)
    rec_ids = [j["id"] for j in out["job_state"]["recommendations"]]
    # 台北優先，remote次之，補齊3個
    assert rec_ids[0] == "job_1"
    assert rec_ids[1] == "job_3" or rec_ids[1] == "job_2"
    assert len(rec_ids) == 3
    assert out["system"]["current_node"] == "recommendation"

def test_recommendation_node_no_pref():
    state = {
        "user_profile": {"preferences": {}},
        "job_state": {
            "matched_jobs": [
                {"id": "job_1", "location": "台北", "remote": True},
                {"id": "job_2", "location": "高雄", "remote": True},
                {"id": "job_3", "location": "台中", "remote": False}
            ]
        },
        "system": {}
    }
    out = recommendation_node(state)
    rec_ids = [j["id"] for j in out["job_state"]["recommendations"]]
    assert len(rec_ids) == 3
    assert out["system"]["current_node"] == "recommendation"
