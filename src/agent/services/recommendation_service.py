from typing import List, Dict, Any

def recommend_jobs(matched_jobs: List[Dict[str, Any]], preferences: Dict[str, Any], top_n: int = 3) -> List[Dict[str, Any]]:
    """
    根據匹配分數與用戶偏好推薦職缺
    """
    location_pref = preferences.get("location")
    remote_pref = preferences.get("remote")
    recommendations = []
    for job in matched_jobs:
        if location_pref and job.get("location") == location_pref:
            recommendations.append(job)
        elif remote_pref and job.get("remote") is True:
            recommendations.append(job)
        if len(recommendations) >= top_n:
            break
    # 若不足 top_n，補齊
    if len(recommendations) < top_n:
        for job in matched_jobs:
            if job not in recommendations:
                recommendations.append(job)
            if len(recommendations) >= top_n:
                break
    return recommendations
