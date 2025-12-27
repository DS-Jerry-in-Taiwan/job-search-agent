"""ConversationMemory 實作（Mock版）

提供 get_history, get_user_preferences, save_conversation 方法。
"""

class ConversationMemory:
    def get_history(self, session_id: str, limit: int = 5):
        # 回傳固定歷史
        return [{"query": "A", "response": "B"} for _ in range(limit)]

    def get_user_preferences(self, user_id: str):
        # 回傳固定偏好
        return {"preferred_location": "台北"}

    def save_conversation(self, **kwargs):
        # 模擬儲存成功
        return True
