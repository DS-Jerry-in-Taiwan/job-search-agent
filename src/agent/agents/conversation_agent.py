from typing import Dict, Any, Optional

class ConversationAgent:
    """
    對話 Agent，負責意圖判斷與回覆生成
    """
    def ml_model_predict(self, user_message: str) -> Optional[Dict[str, object]]:
        # stub for ML model prediction
        return None

    def call_llm_intent(self, user_message: str) -> Optional[str]:
        # stub for LLM intent inference
        return None

    def intent_classifier(
        self, user_message: str, enable_rule: bool = True, 
        enable_ml: bool = False, enable_llm: bool = False, logger=None
    ) -> Dict[str, object]:
        GREET_WORDS= ["你好", "您好", "hi", "hello"]
        GOODBYE_WORDS = ["謝謝", "再見", "bye", "感謝"]
        RECOMMEND_WORDS = ["推薦", "適合", "介紹"]
        SKILL_WORDS = ["技能", "分析", "缺乏", "補強"]
        RESUME_WORDS = ["年", "工程師", "履歷"]
        user_message_lower = user_message.lower()
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
        if enable_ml:
            intent = self.ml_model_predict(user_message_lower)
            if intent and intent.get("confidence", 0) > 0.7:
                if logger: logger.info(f"ML intent: {intent}")
                return {"intent": intent.get("label"), "confidence": intent.get("confidence")}
        if enable_llm:
            intent = self.call_llm_intent(user_message_lower)
            if intent:
                if logger: logger.info(f"LLM intent: {intent}")
                return {"intent": intent, "confidence": 0.7}
        if logger: logger.info("Fallback to manual review for intent classification.")
        return {"intent": "manual_review", "confidence": 0.0}

    def converse(self, state: Dict[str, Any]) -> Dict[str, Any]:
        user_message = state.get("conversation", {}).get("user_message", "")
        intent_result = self.intent_classifier(user_message)
        intent = intent_result["intent"]
        confidence = intent_result["confidence"]
        reply = f"收到您的訊息：{user_message}（判斷意圖：{intent}，信心度：{confidence}）"
        state["conversation"]["reply"] = reply
        state["conversation"]["current_intent"] = intent
        state["conversation"]["intent_confidence"] = confidence
        state["system"]["current_node"] = "conversation"
        return state
