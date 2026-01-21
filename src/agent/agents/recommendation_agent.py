from typing import List, Dict, Any

class RecommendationAgent:
    """
    推薦職缺 Agent，根據匹配分數與用戶偏好推薦職缺
    """
    def recommend(self, matched_jobs: List[Dict[str, Any]], preferences: Dict[str, Any], top_n: int = 3) -> List[Dict[str, Any]]:
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
        if len(recommendations) < top_n:
            for job in matched_jobs:
                if job not in recommendations:
                    recommendations.append(job)
                if len(recommendations) >= top_n:
                    break
        return recommendations
