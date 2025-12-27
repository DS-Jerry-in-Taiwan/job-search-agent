from typing import Dict, Any
from datetime import datetime
from .state import AgentState

def load_context_node(state: AgentState) -> AgentState:
    """載入對話上下文（Memory 整合版）

    從 ConversationMemory 載入歷史對話和使用者偏好。
    """
    try:
        from src.memory.conversation_memory import ConversationMemory
        memory = ConversationMemory()
        history = memory.get_history(
            session_id=state["session_id"],
            limit=5
        )
        preferences = memory.get_user_preferences(
            user_id=state["user_id"]
        )
        state["context"] = {
            "history": history,
            "user_preferences": preferences,
            "mentioned_jobs": []
        }
    except Exception as e:
        state["context"] = {
            "history": [],
            "user_preferences": {},
            "mentioned_jobs": []
        }
        state["error"] = f"Memory 載入失敗: {str(e)}"
    return state

def identify_intent_node(state: AgentState) -> AgentState:
    """識別使用者意圖（LLM 整合版）

    使用 LLMClient 分析使用者查詢，識別意圖。
    """
    try:
        from src.llm.llm_client import LLMClient
        import json
        llm_client = LLMClient()
        prompt = f"""
分析以下使用者查詢，識別意圖。

可能的意圖:
- search_job: 搜尋職缺、找工作
- analyze_salary: 薪資分析、薪水查詢
- prepare_interview: 面試準備、面試技巧
- optimize_resume: 履歷優化、履歷修改

使用者查詢: {state["query"]}

請以 JSON 格式返回識別的意圖列表:
{{"intents": ["intent1", "intent2"]}}
"""
        response = llm_client.generate(prompt)
        parsed = json.loads(response)
        intents = parsed.get("intents", [])
        state["intents"] = intents
    except Exception as e:
        # 降級：關鍵詞匹配
        query = state["query"].lower()
        intents = []
        if any(k in query for k in ["找工作", "搜尋", "職缺", "jobs"]):
            intents.append("search_job")
        if any(k in query for k in ["薪資", "薪水", "salary"]):
            intents.append("analyze_salary")
        if any(k in query for k in ["面試", "interview"]):
            intents.append("prepare_interview")
        if any(k in query for k in ["履歷", "resume"]):
            intents.append("optimize_resume")
        if not intents:
            intents = ["search_job"]
        state["intents"] = intents
        state["error"] = f"LLM intent識別失敗，使用降級方案: {str(e)}"
    return state

def decompose_tasks_node(state: AgentState) -> AgentState:
    """拆解任務（LLM 整合版）

    使用 LLMClient 提取參數，結構化任務資訊。
    """
    try:
        from src.llm.llm_client import LLMClient
        import json
        llm_client = LLMClient()
        tasks = []
        for intent in state["intents"]:
            prompt = f"""
從以下查詢中提取 {intent} 的參數。

查詢: {state["query"]}

需要提取的參數:
- location: 地點（如：台北、新竹）
- skill: 技能（如：Python、AI）
- experience: 經驗年資（如：3年、5年以上）
- salary_range: 薪資範圍（如：50-80萬）
- job_title: 職位名稱（如：工程師、經理）

以 JSON 格式返回:
{{"location": "...", "skill": "...", ...}}
"""
            response = llm_client.generate(prompt)
            params = json.loads(response)
            tasks.append({
                "intent": intent,
                "query": state["query"],
                "params": params,
                "timestamp": datetime.now().isoformat()
            })
        state["tasks"] = tasks
    except Exception as e:
        # 降級：僅填入基本參數
        tasks = []
        for intent in state["intents"]:
            tasks.append({
                "intent": intent,
                "query": state["query"],
                "params": {},
                "timestamp": datetime.now().isoformat()
            })
        state["tasks"] = tasks
        state["error"] = f"LLM 任務拆解失敗，使用降級方案: {str(e)}"
    return state

def integrate_results_node(state: AgentState) -> AgentState:
    """整合 Agent 執行結果

    將所有 Agent 的執行結果整合成最終回應。
    """
    results = state["results"]
    if not results:
        state["final_response"] = "抱歉，我無法處理您的請求。請提供更多資訊。"
        return state
    response_parts = []
    for r in results:
        agent_name = r.get('agent', 'Unknown')
        result = r.get('result', '')
        response_parts.append(f"【{agent_name}】\n{result}")
    state["final_response"] = "\n\n".join(response_parts)
    return state

def update_memory_node(state: AgentState) -> AgentState:
    """更新對話記憶（Memory 整合版）

    將當前對話儲存到 ConversationMemory。
    """
    try:
        from src.memory.conversation_memory import ConversationMemory
        memory = ConversationMemory()
        memory.save_conversation(
            session_id=state["session_id"],
            user_id=state["user_id"],
            query=state["query"],
            response=state["final_response"],
            intents=state["intents"],
            results=state["results"]
        )
    except Exception as e:
        state["error"] = f"Memory 儲存失敗: {str(e)}"
    return state
