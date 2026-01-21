from src.state.schema import AgentState

def recommendation_node(state: AgentState) -> AgentState:
    """
    推薦職缺節點：僅負責流程調度，所有功能調用 recommendation_service
    """
    try:
        from src.agent.services.recommendation_service import recommend_jobs
        matched_jobs = state["job_state"].get("matched_jobs", [])
        preferences = state["user_profile"].get("preferences", {})
        recommendations = recommend_jobs(matched_jobs, preferences, top_n=3)
        state["job_state"]["recommendations"] = recommendations
        state["next_action"] = "decision"
        state["system"]["current_node"] = "recommendation"
        return state
    except Exception as e:
        state["system"]["error_type"] = "RECOMMENDATION_ERROR"
        state["system"]["error_message"] = str(e)
        state["system"]["retry_flag"] = True
        state["system"]["last_failed_node"] = "recommendation"
        state["next_action"] = "error_handler"
        return state
