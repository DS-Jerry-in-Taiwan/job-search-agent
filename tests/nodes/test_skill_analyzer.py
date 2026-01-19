import pytest
from src.nodes.skill_analyzer import skill_analyzer_node

def make_state(skills):
    return {
        "user_profile": {
            "skills": skills
        },
        "system": {}
    }

def test_skill_analyzer_no_ai():
    state = make_state(["Python", "Docker"])
    out = skill_analyzer_node(state)
    assert out["user_profile"]["skill_analysis"] == "推薦學習 AI/深度學習技能"
    assert out["next_action"] == "job_matcher"

def test_skill_analyzer_no_docker():
    state = make_state(["Python", "AI"])
    out = skill_analyzer_node(state)
    assert out["user_profile"]["skill_analysis"] == "推薦補強 Docker/DevOps 技能"
    assert out["next_action"] == "job_matcher"

def test_skill_analyzer_no_python():
    state = make_state(["AI", "Docker"])
    out = skill_analyzer_node(state)
    assert out["user_profile"]["skill_analysis"] == "推薦學習 Python"
    assert out["next_action"] == "job_matcher"

def test_skill_analyzer_full():
    state = make_state(["Python", "AI", "Docker"])
    out = skill_analyzer_node(state)
    assert out["user_profile"]["skill_analysis"] == "技能組合完整，可進階專案管理"
    assert out["next_action"] == "job_matcher"
