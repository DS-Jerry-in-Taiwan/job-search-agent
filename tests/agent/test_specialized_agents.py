import pytest
from src.agent.agents import (
    JobSearchAgent,
    SalaryAnalyzerAgent,
    InterviewCoachAgent,
    ResumeOptimizerAgent,
)

def test_job_search_basic():
    agent = JobSearchAgent()
    result = agent.run("python developer", {"profile": {"skills": ["Python"]}})
    assert isinstance(result, str)

def test_job_search_with_profile():
    agent = JobSearchAgent()
    jobs = agent.call_tool("search_jobs", query="data scientist", user_profile={})
    assert isinstance(jobs, list) or hasattr(jobs, "jobs")

def test_calculate_match_score():
    agent = JobSearchAgent()
    score = agent.call_tool("calculate_match", job={}, profile={})
    assert isinstance(score, float)

def test_salary_range_analysis():
    agent = SalaryAnalyzerAgent()
    result = agent.call_tool("analyze_range", job_title="engineer", location="Taipei")
    assert "median" in result

def test_salary_prediction():
    agent = SalaryAnalyzerAgent()
    salary = agent.call_tool("predict_salary", job_title="engineer", experience=5)
    assert isinstance(salary, int)

def test_negotiation_advice():
    agent = SalaryAnalyzerAgent()
    advice = agent.call_tool("suggest_negotiation", predicted=150, market_range={"median": 150, "p75": 180})
    assert isinstance(advice, str)

def test_generate_questions():
    agent = InterviewCoachAgent()
    questions = agent.call_tool("generate_questions", job_title="engineer", tech_stack=["Python", "SQL"])
    assert isinstance(questions, list)
    assert len(questions) <= 10

def test_evaluate_skills():
    agent = InterviewCoachAgent()
    result = agent.call_tool("evaluate_skills", user_skills=["Python"], required_skills=["Python", "SQL"])
    assert "gaps" in result

def test_preparation_suggestions():
    agent = InterviewCoachAgent()
    suggestion = agent.call_tool("suggest_prep", gaps=["SQL"])
    assert isinstance(suggestion, str)

def test_analyze_resume():
    agent = ResumeOptimizerAgent()
    analysis = agent.call_tool("analyze_resume", resume_text="Python developer resume")
    assert "sections" in analysis

def test_identify_gaps():
    agent = ResumeOptimizerAgent()
    gaps = agent.call_tool("identify_gaps", resume_keywords=["Python"], job_requirements=["Python", "SQL"])
    assert "SQL" in gaps

def test_suggest_improvements():
    agent = ResumeOptimizerAgent()
    suggestion = agent.call_tool("suggest_improvements", gaps=["SQL"])
    assert isinstance(suggestion, str)
