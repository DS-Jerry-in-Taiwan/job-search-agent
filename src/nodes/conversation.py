from src.state.schema import AgentState
from typing import Dict, Optional

def ml_model_predict(use_message: str) -> Optional[Dict[str, object]]:
    # stub for ML model prediction
    return None


def call_llm_intent(user_message: str) -> Optional[str]:
    # stub for LLM intent inference
    return None

def intent_classifier(
    user_massage: str, enable_rule: bool, 
    enable_ml: bool, enable_llm: bool, logger=None
    ) -> Dict[str, object]:
    """
    multi-layer intent classification
    """
    GREET_WORDS= ["你好", "您好", "hi", "hello"]
    GOODBYE_WORDS = ["謝謝", "再見", "bye", "感謝"]
    RECOMMEND_WORDS = ["推薦", "適合", "介紹"]
    SKILL_WORDS = ["技能", "分析", "缺乏", "補強"]
    RESUME_WORDS = ["年", "工程師", "履歷"]
    
    # 1. rule-based intent classification
    user_message_lower = user_massage.lower()
    if enable_rule:
        if any(word in user_message_lower for word in GREET_WORDS):
            if logger: logger.info("Rule-based intent: greet")
            return {"intent": "greet", "confidence": 1.0}
        elif any(word in user_message_lower for word in GOODBYE_WORDS):
            if logger: logger.info("Rule-based intent: goodbye")
            return {"intent": "goodbye", "confidence": 1.0}
        elif any(word in user_message_lower for word in RECOMMEND_WORDS):
            if logger: logger.info("Rule-based intent: ask_recommendation")
            return {"intent": "ask_recommendation", "confidence": 1.0}
        elif any(word in user_message_lower for word in SKILL_WORDS):
            if logger: logger.info("Rule-based intent: ask_skill_advice")
            return {"intent": "ask_skill_advice", "confidence": 1.0}
        elif any(word in user_message_lower for word in RESUME_WORDS):
            if logger: logger.info("Rule-based intent: provide_resume")
            return {"intent": "provide_resume", "confidence": 1.0}
    
    # 2. ML/NLP-based intent classification
    if enable_ml:
        intent = ml_model_predict(user_message_lower)
        if intent and intent["confidence"] > 0.7:
            if logger: logger.info(f"ML intent: {intent}")
            return {"intent": intent.label, "confidence": intent.confidence}
    
    # 3. LLM-based intent classification
    if enable_llm:
        intent = llm_infer_intent(user_message_lower)
        if intent:
            if logger: logger.info(f"LLM intent: {intent}")
            return {"intent": intent, "confidence": 0.7}
    
    # 4. fallback to manual review
    if logger: logger.info("Fallback to manual review for intent classification.")
    return {"intent": "manual_review", "confidence": 0.0}
    

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
    
    # call intent_classifier
    intent_result = intent_classifier(
        user_message,
        enable_rule=True,
        enable_ml=False,
        enable_llm=False,
        logger=None
    )
    
    # get intent
    intent = intent_result.get("intent", "general")
    confidence = intent_result.get("confidence", 0.0)
    
    # set current intent based on intent
    state["conversation"]["current_intent"] = intent
    # next_action 交由 decision node 判斷
        
    # generate reply based on intent
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
    state["system"]["current_node"] = "conversation"
    return state
