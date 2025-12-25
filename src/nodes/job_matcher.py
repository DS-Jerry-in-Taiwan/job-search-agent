from src.state.schema import AgentState
from typing import Dict, Set, Any
from datetime import datetime

import json
from pathlib import Path

def job_matcher_node(state: AgentState) -> AgentState:
    """
    履歷匹配職缺 → JobState

    輸入: state["user_profile"]["skills"]
    輸出: state["job_state"]["matched_jobs"], ["match_scores"]

    處理流程:
    1. 載入 data/mock/jobs/mock_jobs.json
    2. 計算每個職缺的匹配分數
    3. 篩選匹配度 >= 0.3 的職缺
    4. 排序並更新 JobState
    """
    status = state["job_state"].get("status")

    if status == "uninitialized":
        # 尚未載入，載入 mock_jobs.json
        jobs_path = Path("data/mock/jobs/mock_jobs.json")
        with open(jobs_path, "r", encoding="utf-8") as f:
            jobs = json.load(f)
        state["job_state"]["jobs"] = jobs
        state["job_state"]["status"] = "ready" if jobs else "empty"
        # 若載入後為空，直接回傳
        if not jobs:
            state["job_state"]["matched_jobs"] = []
            state["job_state"]["match_scores"] = {}
            state["job_state"]["last_updated"] = datetime.now()
            state["system"]["current_node"] = "job_matcher"
            return state
        all_jobs = jobs
    elif status == "empty":
        # 測試或外部明確指定為空
        state["job_state"]["matched_jobs"] = []
        state["job_state"]["match_scores"] = {}
        state["job_state"]["last_updated"] = datetime.now()
        state["system"]["current_node"] = "job_matcher"
        return state
    elif status == "ready":
        all_jobs = state["job_state"].get("jobs", [])
    else:
        raise ValueError(f"Unknown job_state status: {status}")



    user_skills = set(s.lower() for s in state["user_profile"]["skills"])
    matched_jobs: list[dict[str, Any]] = []
    match_scores: Dict[str, float] = {}

    for job in all_jobs:
        score = calculate_match_score(user_skills, job)
        if score >= 0.3:
            matched_jobs.append(job)
            job_id = job.get("job_id") or job.get("id")
            match_scores[job_id] = round(score, 2)

    def get_job_id(job: dict[str, Any]) -> str:
        job_id = job.get("job_id")
        if isinstance(job_id, str):
            return job_id
        id_val = job.get("id")
        if isinstance(id_val, str):
            return id_val
        return ""
    matched_jobs.sort(key=lambda j: match_scores.get(get_job_id(j), 0.0), reverse=True)

    state["job_state"]["jobs"] = all_jobs
    state["job_state"]["matched_jobs"] = matched_jobs
    state["job_state"]["match_scores"] = match_scores
    state["job_state"]["last_updated"] = datetime.now()
    state["system"]["current_node"] = "job_matcher"
    return state

def calculate_match_score(user_skills: Set[str], job: Dict[str, Any]) -> float:
    """
    計算匹配分數 (0.0 - 1.0)

    :param user_skills: 用戶技能集合
    :param job: 職缺字典
    :return: 匹配分數
    """
    job_requirements = job.get("requirements", "")
    if isinstance(job_requirements, list):
        job_skills = set(s.lower() for s in job_requirements)
    elif isinstance(job_requirements, str):
        job_skills = set(job_requirements.lower().split())
    else:
        job_skills = set()
    if not user_skills:
        return 0.0
    matched_skills = user_skills & job_skills
    skill_score = len(matched_skills) / len(user_skills)
    return min(skill_score, 1.0)
