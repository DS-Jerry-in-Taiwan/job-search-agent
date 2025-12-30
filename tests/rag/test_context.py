import pytest
from src.rag.context.assembler import ContextAssembler

def test_skill_match_score():
    assembler = ContextAssembler()
    assert assembler._skill_match_score(["python", "sql"], ["python", "java"]) == 50.0
    assert assembler._skill_match_score([], ["python"]) == 0.0
    assert assembler._skill_match_score(["python"], []) == 0.0

def test_assemble_context():
    assembler = ContextAssembler()
    jobs = [
        {"title": "AI工程師", "skills": ["python", "sql"], "rerank_score": 0.9},
        {"title": "後端工程師", "skills": ["java"], "rerank_score": 0.8},
        {"title": "資料科學家", "skills": ["python", "ml"], "rerank_score": 0.7},
    ]
    user_profile = {"skills": ["python", "sql", "ml"]}
    context = assembler.assemble("查詢", jobs, user_profile)
    assert "jobs" in context
    assert "analysis" in context
    assert context["jobs"][0]["title"] == "AI工程師"
    assert context["analysis"]["best_job"] == "AI工程師"
    assert context["analysis"]["match_scores"][0] == 100.0
