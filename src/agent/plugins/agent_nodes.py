"""Agent Plugin Nodes
統一流程調度與狀態管理，直接調用 agent
"""

from typing import Dict, Any, Set, List
from datetime import datetime

from src.agent.agents.skill_agent import SkillAgent
from src.agent.agents.job_match_agent import JobMatchAgent
from src.agent.agents.recommendation_agent import RecommendationAgent
from src.agent.agents.finalizer_agent import FinalizerAgent
from src.agent.agents.interview_coach_agent import InterviewCoachAgent
from src.agent.agents.job_search_agent import JobSearchAgent
from src.agent.agents.resume_optimizer_agent import ResumeOptimizerAgent
from src.agent.agents.salary_analyzer_agent import SalaryAnalyzerAgent
from src.agent.agents.manual_review_agent import ManualReviewAgent
from src.agent.agents.resume_parser_agent import ResumeParserAgent
from src.agent.agents.conversation_agent import ConversationAgent
from src.agent.agents.decision_agent import DecisionAgent

def decision_node(state: Dict[str, Any]) -> Dict[str, Any]:
    agent = DecisionAgent()
    # 完全比照 src/nodes/decision.py 的分支與狀態設置
    # waiting for manual review
    if state.get("system", {}).get("manual_review_status") == "pending":
        if "conversation" in state and "messages" in state["conversation"]:
            state["conversation"]["messages"].append({
                "role": "assistant",
                "content": "請稍候，人工審核中，審核完成後會自動通知您。"
            })
        state["next_action"] = "finalizer"
        state["system"]["current_node"] = "decision"
        return state

    # manual review logic
    if state.get("next_action") == "manual_review":
        state["next_action"] = "finalizer"
        state["system"]["current_node"] = "decision"
        return state

    # error_handle_node logic
    error_msg = state.get("system", {}).get("error_message", "")
    if error_msg:
        if "已超過最大重試次數" in error_msg:
            state['next_action'] = 'finalizer'
            state["system"]["current_node"] = "decision"
            return state
        else:
            state["next_action"] = "conversation"
        state["system"]["error_message"] = ""
        state["system"]["current_node"] = "decision"
        return state

    # if job_state is empty, end workflow directly
    if state["job_state"].get("status") == "empty":
        state["next_action"] = "finalizer"
        state["system"]["current_node"] = "decision"
        return state

    print("--------------------------------")
    print(state.get("next_action","no next action"))

    # 決策分流與分數計算
    if (
        state["user_profile"].get("parsed_at")
        and state["job_state"].get("matched_jobs")
        and not state.get("decision_result")
    ):
        raw_scores = {
            "skill_match": state["user_profile"].get("skill_score", 60),
            "experience_match": state["user_profile"].get("exp_score", 70),
            "preference_match": state["user_profile"].get("pref_score", 65)
        }
        weights = {"skill": 0.2, "experience": 0.6, "preference": 1.0}
        decision_result = agent.decide(
            case_id=state.get("session_id", "default"),
            raw_scores=raw_scores,
            weights=weights,
            normalization_method="min-max"
        )
        state["decision_result"] = decision_result
        state["system"]["decision_result"] = decision_result
        if decision_result["final_score"] > 0.7:
            if not state["user_profile"].get("skill_analysis"):
                state["next_action"] = "skill_analyzer"
            else:
                state["next_action"] = "finalizer"
        elif decision_result["final_score"] > 0.6:
            state["next_action"] = "recommendation"
        else:
            state["next_action"] = "finalizer"
        state["system"]["current_node"] = "decision"
        return state

    # manual decision logic
    if state.get("system", {}).get("need_manual_review", False):
        state["next_action"] = "manual_review"
        state["system"]["current_node"] = "decision"
        return state

    # 僅在尚未解析履歷或尚未匹配職缺時才分流
    if not state["user_profile"].get("parsed_at"):
        state["conversation"]["current_intent"] = "general"
        state["next_action"] = "resume_parser"
        state["system"]["current_node"] = "decision"
        return state
    if not state["job_state"].get("matched_jobs"):
        state["conversation"]["current_intent"] = "job_search"
        state["next_action"] = "job_matcher"
        state["system"]["current_node"] = "decision"
        return state

    # 其他情境
    if state["conversation"]["current_intent"] == "skill_analysis":
        state["next_action"] = "conversation"
        state["system"]["current_node"] = "decision"
        return state
    if state["conversation"].get("turn_count", 0) < 3:
        state["conversation"]["current_intent"] = "general"
        state["next_action"] = "conversation"
        state["system"]["current_node"] = "decision"
        return state

    # 預設推進到 finalizer
    state["next_action"] = "finalizer"
    state["system"]["current_node"] = "decision"
    return state

def conversation_node(state: Dict[str, Any]) -> Dict[str, Any]:
    agent = ConversationAgent()
    state = agent.converse(state)
    return state

def resume_parser_node(state: Dict[str, Any]) -> Dict[str, Any]:
    agent = ResumeParserAgent()
    pdf_path = state["user_profile"].get("resume_path")
    if not pdf_path:
        state["system"]["error_type"] = "DATA_MISSING"
        state["system"]["error_message"] = "resume_path 未提供"
        state["system"]["retry_flag"] = False
        state["system"]["last_failed_node"] = "resume_parser"
        state["next_action"] = "error_handler"
        return state
    try:
        parsed = agent.parse(pdf_path)
    except Exception as e:
        state["system"]["error_type"] = "PARSE_ERROR"
        state["system"]["error_message"] = str(e)
        state["system"]["retry_flag"] = True
        state["system"]["last_failed_node"] = "resume_parser"
        state["next_action"] = "error_handler"
        return state
    state["user_profile"].update(parsed)
    state["system"]["current_node"] = "resume_parser"
    state["next_action"] = "decision"
    return state

def skill_analyze_node(state: Dict[str, Any]) -> Dict[str, Any]:
    agent = SkillAgent()
    skills = set(state["user_profile"].get("skills", []))
    advice = agent.analyze(skills)
    state["user_profile"]["skill_analysis"] = advice
    state["system"]["current_node"] = "skill_analyzer"
    return state

def job_match_node(state: Dict[str, Any]) -> Dict[str, Any]:
    agent = JobMatchAgent()
    user_skills = set(s.lower() for s in state["user_profile"].get("skills", []))
    jobs = state["job_state"].get("jobs", [])
    # fallback: 自動載入 mock jobs
    if not jobs:
        import json
        from pathlib import Path
        jobs_path = Path("data/mock/jobs/mock_jobs.json")
        if jobs_path.exists():
            with open(jobs_path, "r", encoding="utf-8") as f:
                jobs = json.load(f)
            state["job_state"]["jobs"] = jobs
    matched_jobs, match_scores = agent.match_jobs(user_skills, jobs)
    state["job_state"]["matched_jobs"] = matched_jobs
    state["job_state"]["match_scores"] = match_scores
    state["system"]["current_node"] = "job_matcher"
    return state

def recommendation_node(state: Dict[str, Any]) -> Dict[str, Any]:
    agent = RecommendationAgent()
    matched_jobs = state["job_state"].get("matched_jobs", [])
    preferences = state["user_profile"].get("preferences", {})
    recommendations = agent.recommend(matched_jobs, preferences, top_n=3)
    state["job_state"]["recommendations"] = recommendations
    state["system"]["current_node"] = "recommendation"
    return state

def finalizer_node(state: Dict[str, Any]) -> Dict[str, Any]:
    agent = FinalizerAgent()
    # 保證 decision_result 進入 finalizer 時寫入 result["system"] 並同步到頂層
    if "decision_result" in state:
        state["system"]["decision_result"] = state["decision_result"]
        state["decision_result"] = state["decision_result"]
    elif "decision_result" in state.get("system", {}):
        state["decision_result"] = state["system"]["decision_result"]
    state = agent.finalize(state)
    return state

def interview_coach_node(state: Dict[str, Any]) -> Dict[str, Any]:
    agent = InterviewCoachAgent()
    interview_context = state.get("interview_context", {})
    result = agent.coach(interview_context)
    state["interview_context"]["coach_result"] = result
    state["system"]["current_node"] = "interview_coach"
    return state

def job_search_node(state: Dict[str, Any]) -> Dict[str, Any]:
    agent = JobSearchAgent()
    search_params = state.get("job_search_params", {})
    result = agent.search(search_params)
    state["job_state"]["search_result"] = result
    state["system"]["current_node"] = "job_search"
    return state

def resume_optimize_node(state: Dict[str, Any]) -> Dict[str, Any]:
    agent = ResumeOptimizerAgent()
    resume_data = state.get("resume_data", {})
    result = agent.optimize(resume_data)
    state["resume_data"]["optimized"] = result
    state["system"]["current_node"] = "resume_optimizer"
    return state
def salary_analyze_node(state: Dict[str, Any]) -> Dict[str, Any]:
    agent = SalaryAnalyzerAgent()
    salary_context = state.get("salary_context", {})
    result = agent.analyze(salary_context)
    state["salary_context"]["analyze_result"] = result
    state["system"]["current_node"] = "salary_analyzer"
    return state
from src.agent.agents.router_agent import RouterAgent

def router_node(state: Dict[str, Any]) -> Dict[str, Any]:
    agent = RouterAgent()
    return agent.route(state)
from src.agent.agents.error_handler_agent import ErrorHandlerAgent

def error_handler_node(state: Dict[str, Any]) -> Dict[str, Any]:
    agent = ErrorHandlerAgent()
    return agent.handle(state)

def manual_review_node(state: Dict[str, Any]) -> Dict[str, Any]:
    agent = ManualReviewAgent()
    state = agent.review(state)
    return state
