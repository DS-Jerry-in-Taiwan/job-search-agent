from typing import List, Dict, Any
import numpy as np

class ContextAssembler:
    """
    將 Phase 10 檢索結果組裝為 LLM 最佳上下文格式。
    """

    def __init__(self, max_tokens: int = 2000):
        self.max_tokens = max_tokens

    def _skill_match_score(self, user_skills: List[str], job_skills: List[str]) -> float:
        if not user_skills or not job_skills:
            return 0.0
        user_skills_set = set([s.lower() for s in user_skills])
        job_skills_set = set([s.lower() for s in job_skills])
        match_count = len(user_skills_set & job_skills_set)
        total = len(job_skills_set)
        return round(100 * match_count / total, 2) if total > 0 else 0.0

    def assemble(self, query: str, jobs: List[Dict[str, Any]], user_profile: Dict[str, Any]) -> Dict[str, Any]:
        """
        組裝 LLM 上下文，回傳 context 與 metadata。
        """
        user_skills = user_profile.get("skills", [])
        # 計算每個職缺的技能匹配分數
        for job in jobs:
            job_skills = job.get("skills", [])
            job["match_score"] = self._skill_match_score(user_skills, job_skills)
            # 綜合排序分數（假設有 rerank_score）
            job["final_score"] = 0.7 * job.get("rerank_score", 1.0) + 0.3 * (job["match_score"] / 100)
        # 依 final_score 排序
        jobs_sorted = sorted(jobs, key=lambda x: -x["final_score"])
        # 精選 Top-5
        jobs_top = jobs_sorted[:5]
        # 組裝分析
        analysis = {
            "user_skills": user_skills,
            "match_scores": [j["match_score"] for j in jobs_top],
            "best_job": jobs_top[0]["title"] if jobs_top else "",
        }
        # 組裝 context（暫以簡單格式，交由 Formatter 處理）
        context = {
            "query": query,
            "jobs": jobs_top,
            "analysis": analysis
        }
        return context
