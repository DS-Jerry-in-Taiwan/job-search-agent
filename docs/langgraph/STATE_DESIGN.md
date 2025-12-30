# LangGraph AgentState 設計說明

## 1. 結構定義

```python
from typing import TypedDict, List, Dict, Any, Annotated
from langchain_core.messages import BaseMessage
from operator import add

class AgentState(TypedDict):
    messages: Annotated[List[BaseMessage], add]
    query: str
    session_id: str
    user_id: str
    intents: List[str]
    tasks: List[Dict[str, Any]]
    current_agent: str
    results: List[Dict[str, Any]]
    context: Dict[str, Any]
    final_response: str
    error: str
    retry_count: int
```

## 2. 欄位說明

- **messages**: 對話歷史訊息列表，支援 Annotated[..., add] 自動累加。
- **query**: 使用者原始查詢。
- **session_id**: 會話 ID，追蹤多輪對話。
- **user_id**: 使用者 ID。
- **intents**: 識別出的意圖列表。
- **tasks**: 拆解後的任務列表。
- **current_agent**: 當前執行的 Agent 名稱。
- **results**: 各 Agent 執行結果。
- **context**: 對話上下文資訊（歷史摘要、偏好等）。
- **final_response**: 最終回應訊息。
- **error**: 錯誤訊息。
- **retry_count**: 錯誤重試次數。

## 3. 設計原則

- 使用 TypedDict 保證型別安全
- 欄位設計完整但不冗餘
- 支援多 Agent、任務拆解、上下文管理
- 易於擴展與測試

## 4. 初始狀態工廠

```python
def create_initial_state(query: str, user_id: str = "default") -> AgentState:
    import uuid
    return AgentState(
        messages=[],
        query=query,
        session_id=str(uuid.uuid4()),
        user_id=user_id,
        intents=[],
        tasks=[],
        current_agent="",
        results=[],
        context={},
        final_response="",
        error="",
        retry_count=0
    )
```

## 5. 參考

- Phase12.5_LangGraph_Foundation_HighLevel_Design.md
- docs/agent_context/phase12.5/01_dev_goal_context.md
- docs/agent_context/phase12.5/03_agent_roles_context.md
