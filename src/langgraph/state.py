from typing import TypedDict, List, Dict, Any, Annotated
from langchain_core.messages import BaseMessage
from operator import add

class AgentState(TypedDict):
    """
    JobSearch Agent 的狀態定義

    這個狀態包含了整個 Agent 系統運行所需的所有資訊。
    使用 TypedDict 確保類型安全。
    """

    # === 對話管理 ===
    messages: Annotated[List[BaseMessage], add]
    """對話歷史訊息列表，使用 Annotated[..., add] 表示新訊息會自動累加到列表中。"""

    # === 使用者輸入 ===
    query: str
    """使用者的原始查詢"""

    session_id: str
    """會話 ID，用於多輪對話追蹤和 Checkpoint"""

    user_id: str
    """使用者 ID，用於多使用者支援"""

    # === 意圖與任務 ===
    intents: List[str]
    """識別出的意圖列表，例如: ['search_job', 'analyze_salary', 'prepare_interview']"""

    tasks: List[Dict[str, Any]]
    """根據意圖拆解的任務列表，每個任務包含 intent/params 等"""

    # === Agent 執行 ===
    current_agent: str
    """當前執行的 Agent 名稱"""

    results: List[Dict[str, Any]]
    """各 Agent 的執行結果"""

    # === 上下文管理 ===
    context: Dict[str, Any]
    """對話上下文資訊，包含歷史摘要、提及職缺、偏好等"""

    # === 輸出 ===
    final_response: str
    """最終回應給使用者的訊息"""

    # === 錯誤處理 ===
    error: str
    """錯誤訊息（如果有）"""

    retry_count: int
    """重試次數，用於錯誤恢復"""

def create_initial_state(query: str, user_id: str = "default") -> AgentState:
    """
    創建初始狀態

    Args:
        query: 使用者查詢
        user_id: 使用者 ID

    Returns:
        初始化的 AgentState
    """
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
