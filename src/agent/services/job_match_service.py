from typing import Set, Dict, Any, List

def calculate_match_score(user_skills: Set[str], job_skills: Set[str]) -> float:
    if not user_skills or not job_skills:
        return 0.0
    matched = user_skills & job_skills
    return round(len(matched) / len(job_skills), 2)

def match_jobs(user_skills: Set[str], jobs: List[Dict[str, Any]], min_score: float = 0.3) -> (List[Dict[str, Any]], Dict[str, float]):
    matched_jobs: List[Dict[str, Any]] = []
    match_scores: Dict[str, float] = {}
    for job in jobs:
        job_skills = set(s.lower() for s in job.get("requirements", []))
        score = calculate_match_score(user_skills, job_skills)
        job_id = job.get("job_id") or job.get("id")
        if score >= min_score:
            matched_jobs.append(job)
            match_scores[job_id] = score
    matched_jobs.sort(key=lambda j: match_scores.get(j.get("job_id") or j.get("id"), 0.0), reverse=True)
    return matched_jobs, match_scores
