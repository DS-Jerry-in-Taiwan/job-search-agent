import pytest
from src.state.operations import create_initial_state
from src.nodes.utils import skill_analyzer_node

def test_skill_analyzer_node_python():
    """測試技能增強（含 Python）"""
    state = create_initial_state()
    state["user_profile"]["skills"] = ["Python"]
    result = skill_analyzer_node(state)
    assert "Django" in result["user_profile"]["skills"]
    assert "Flask" in result["user_profile"]["skills"]
    assert result["system"]["current_node"] == "skill_analyzer"

def test_skill_analyzer_node_javascript():
    """測試技能增強（含 JavaScript）"""
    state = create_initial_state()
    state["user_profile"]["skills"] = ["JavaScript"]
    result = skill_analyzer_node(state)
    assert "TypeScript" in result["user_profile"]["skills"]
    assert "Node.js" in result["user_profile"]["skills"]
    assert result["system"]["current_node"] == "skill_analyzer"

def test_skill_analyzer_node_no_enhance():
    """測試技能增強（無增強條件）"""
    state = create_initial_state()
    state["user_profile"]["skills"] = ["SQL"]
    result = skill_analyzer_node(state)
    assert set(result["user_profile"]["skills"]) == {"SQL"}
    assert result["system"]["current_node"] == "skill_analyzer"
