from src.state.schema import AgentState
from typing import Dict, Any, List
from datetime import datetime
import json
from pathlib import Path

def calculate_match_score(user_skills: set, job_skills: set) -> float:
    if not user_skills or not job_skills:
        return 0.0
    matched = user_skills & job_skills
    return round(len(matched) / len(job_skills), 2)

def job_matcher_node(state: AgentState, jobs_path: str = None) -> AgentState:
    """
    真實職缺匹配節點
    根據履歷技能與職缺需求，計算匹配分數，排序推薦
    輸入: state["user_profile"]["skills"]
    輸出: state["job_state"]["matched_jobs"], match_scores, last_updated
    jobs_path: 可選，指定職缺資料路徑（for 測試）
    """
    user_skills = set(s.lower() for s in state["user_profile"].get("skills", []))
    if jobs_path is None:
        jobs_path_obj = Path("data/mock/jobs/mock_jobs.json")
    else:
        jobs_path_obj = Path(jobs_path)
    if not jobs_path_obj.exists():
        state["system"]["error_message"] = "職缺資料不存在"
        return state

    with open(jobs_path_obj, "r", encoding="utf-8") as f:
        jobs = json.load(f)

    matched_jobs: List[Dict[str, Any]] = []
    match_scores: Dict[str, float] = {}

    for job in jobs:
        job_skills = set(s.lower() for s in job.get("requirements", []))
        score = calculate_match_score(user_skills, job_skills)
        job_id = job.get("job_id") or job.get("id")
        if score >= 0.3:
            matched_jobs.append(job)
            match_scores[job_id] = score

    matched_jobs.sort(key=lambda j: match_scores.get(j.get("job_id") or j.get("id"), 0.0), reverse=True)

    state["job_state"]["jobs"] = jobs
    state["job_state"]["matched_jobs"] = matched_jobs
    state["job_state"]["match_scores"] = match_scores
    state["job_state"]["last_updated"] = datetime.now()
    state["system"]["current_node"] = "job_matcher"
    return state
