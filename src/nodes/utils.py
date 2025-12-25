from src.state.schema import AgentState

def skill_analyzer_node(state: AgentState) -> AgentState:
    """
    深度分析技能 → 增強 skills 清單

    輸入: state["user_profile"]["resume_text"]
    輸出: 更新 state["user_profile"]["skills"]

    處理流程:
    1. NLP 分析履歷文本
    2. 提取技術關鍵字
    3. 分類技能等級
    """
    # Mock 實作：根據現有技能增強
    base_skills = state["user_profile"]["skills"]
    enhanced_skills = base_skills.copy()
    if "Python" in base_skills:
        enhanced_skills.extend(["Django", "Flask"])
    if "JavaScript" in base_skills:
        enhanced_skills.extend(["TypeScript", "Node.js"])
    state["user_profile"]["skills"] = list(set(enhanced_skills))
    state["system"]["current_node"] = "skill_analyzer"
    return state

def recommendation_node(state: AgentState) -> AgentState:
    """
    生成推薦理由 → recommendations

    輸入: state["job_state"]["matched_jobs"]
    輸出: state["job_state"]["recommendations"]

    處理流程:
    1. 分析前5名匹配職缺
    2. 生成推薦理由
    3. 更新 recommendations
    """
    matched = state["job_state"]["matched_jobs"][:5]
    recommendations = []
    for job in matched:
        job_id = job.get("job_id") or job.get("id")
        score = state["job_state"]["match_scores"].get(str(job_id), 0)
        reason = f"推薦 {job.get('title', '未知職缺')}：匹配度 {score*100:.0f}%"
        recommendations.append(reason)
    state["job_state"]["recommendations"] = recommendations
    state["system"]["current_node"] = "recommendation"
    return state
