from src.state.schema import AgentState

def recommendation_node(state: AgentState) -> AgentState:
    """
    真實推薦職缺節點
    根據匹配分數、用戶偏好推薦職缺，並設置 next_action="router"
    輸入: state["job_state"]["matched_jobs"], state["user_profile"]["preferences"]
    輸出: state["job_state"]["recommendations"], next_action="router"
    """
    matched_jobs = state["job_state"].get("matched_jobs", [])
    preferences = state["user_profile"].get("preferences", {})
    location_pref = preferences.get("location")
    remote_pref = preferences.get("remote")
    # 推薦邏輯：優先推薦地點符合且支援 remote 的職缺
    recommendations = []
    for job in matched_jobs:
        if location_pref and job.get("location") == location_pref:
            recommendations.append(job)
        elif remote_pref and job.get("remote") is True:
            recommendations.append(job)
        if len(recommendations) >= 3:
            break
    # 若不足3個，補齊
    if len(recommendations) < 3:
        for job in matched_jobs:
            if job not in recommendations:
                recommendations.append(job)
            if len(recommendations) >= 3:
                break
    state["job_state"]["recommendations"] = recommendations
    state["next_action"] = "router"
    state["system"]["current_node"] = "recommendation"
    return state
