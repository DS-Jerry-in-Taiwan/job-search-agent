from src.state.schema import AgentState

def skill_analyzer_node(state: AgentState) -> AgentState:
    """
    真實技能分析節點
    根據履歷技能，分析技能短板、推薦提升方向
    輸入: state["user_profile"]["skills"]
    輸出: state["user_profile"]["skill_analysis"], next_action="job_matcher"
    """
    skills = set(state["user_profile"].get("skills", []))
    # 假設有AI、Python、Docker等技能，推薦不同提升方向
    if "AI" not in skills:
        suggestion = "推薦學習 AI/深度學習技能"
    elif "Docker" not in skills:
        suggestion = "推薦補強 Docker/DevOps 技能"
    elif "Python" not in skills:
        suggestion = "推薦學習 Python"
    else:
        suggestion = "技能組合完整，可進階專案管理"
    state["user_profile"]["skill_analysis"] = suggestion
    state["next_action"] = "job_matcher"
    state["system"]["current_node"] = "skill_analyzer"
    return state
