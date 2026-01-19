from src.state.schema import AgentState

def conversation_node(state: AgentState) -> AgentState:
    """
    真實對話回應節點
    根據當前意圖與上下文，生成回應訊息
    輸入: state["conversation"]["current_intent"], state["conversation"]["context"]
    輸出: state["conversation"]["messages"] append, next_action
    """
    intent = state["conversation"].get("current_intent", "")
    context = state["conversation"].get("context", {})
    user_message = context.get("user_message", "")

    if intent == "greet":
        reply = "您好！請問需要什麼求職協助？"
    elif intent == "ask_recommendation":
        jobs = state.get("job_state", {}).get("recommendations", [])
        if jobs:
            reply = f"為您推薦以下職缺：{', '.join(j.get('id', '未知職缺') for j in jobs)}"
        else:
            reply = "目前沒有適合您的推薦職缺。"
    elif intent == "ask_skill_advice":
        advice = state.get("user_profile", {}).get("skill_analysis", "")
        reply = f"建議：{advice}" if advice else "可補強技能，提升競爭力。"
    elif intent == "goodbye":
        reply = "感謝您的使用，祝您求職順利！"
    else:
        reply = f"收到您的訊息：{user_message}"

    # append message
    if "messages" not in state["conversation"]:
        state["conversation"]["messages"] = []
    state["conversation"]["messages"].append({"role": "assistant", "content": reply})
    state["next_action"] = "end" if intent == "goodbye" else ""
    state["system"]["current_node"] = "conversation"
    return state
