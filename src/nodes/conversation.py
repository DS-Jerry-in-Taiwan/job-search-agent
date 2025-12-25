from src.state.schema import AgentState

from langchain_core.messages import AIMessage
def conversation_node(state: AgentState) -> AgentState:
    """
    生成對話回應 → ConversationState.messages

    輸入: state["conversation"]["messages"], ["current_intent"]
    輸出: 新增 AIMessage 到 messages

    處理流程:
    1. 分析用戶最後訊息
    2. 根據 intent 生成回應
    3. 新增到 messages

    支援 Intents:
    - job_search: 職缺搜尋回應
    - skill_analysis: 技能分析回應
    - general: 一般對話回應
    """
    intent = state["conversation"]["current_intent"]
    if intent == "job_search":
        matched_count = len(state["job_state"]["matched_jobs"])
        response = f"找到 {matched_count} 個符合的職缺！"
    elif intent == "skill_analysis":
        skills = state["user_profile"]["skills"]
        response = f"您的技能清單：{', '.join(skills)}"
    else:
        response = "您好！我是職涯搜尋 AI 助手，請問需要什麼幫助？"
    ai_message = AIMessage(content=response)
    state["conversation"]["messages"].append(ai_message)
    state["conversation"]["turn_count"] += 1
    state["system"]["current_node"] = "conversation"
    return state
