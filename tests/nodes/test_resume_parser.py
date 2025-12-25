import pytest
from src.state.operations import create_initial_state
from src.nodes.resume_parser import resume_parser_node, extract_skills_from_text

def test_resume_parser_node():
    """測試履歷解析節點"""
    state = create_initial_state()
    result = resume_parser_node(state)
    assert result["user_profile"]["skills"]
    assert result["user_profile"]["experience_years"] > 0
    assert result["user_profile"]["parsed_at"] is not None
    assert result["system"]["current_node"] == "resume_parser"

def test_extract_skills_from_text():
    """測試技能提取函數"""
    text = "3 years of Python and Docker experience"
    skills = extract_skills_from_text(text)
    assert "Python" in skills
    assert "Docker" in skills
