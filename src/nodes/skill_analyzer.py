from src.state.schema import AgentState

def skill_analyzer(state: AgentState) -> AgentState:
    """
    真實技能分析節點
    根據履歷技能，分析技能短板、推薦提升方向
    輸入: state["user_profile"]["skills"]
    輸出: state["user_profile"]["skill_analysis"], next_action="decision"
    """
    try:
        skills = set(state["user_profile"].get("skills", []))
        from src.agent.services.skill_service import analyze_skills
        suggestion = analyze_skills(skills)
        state["user_profile"]["skill_analysis"] = suggestion
        state["system"]["debug_skill_analysis"] = state["user_profile"]["skill_analysis"]
        state["system"]["debug_skill_analyzer_state"] = str(state)
        state["system"]["current_node"] = "skill_analyzer"
        # 執行完推進到 decision
        state["next_action"] = "decision"
        return state
    except Exception as e:
        state["system"]["error_type"] = "SKILL_ANALYSIS_ERROR"
        state["system"]["error_message"] = f"技能分析失敗: {e}"
        state["system"]["retry_flag"] = True
        state["system"]["last_failed_node"] = "skill_analyzer"
        state["next_action"] = "error_handler"
        state["system"]["current_node"] = "skill_analyzer"
        return state
