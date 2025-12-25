from typing import TypedDict, List, Dict, Any, Optional
from datetime import datetime
from langchain_core.messages import BaseMessage

class UserProfileState(TypedDict):
    """用戶履歷狀態
    儲存用戶的履歷資訊、技能清單與偏好設定。
    """
    user_id: str                          # 用戶唯一識別碼
    resume_text: str                      # 履歷原始文本
    skills: List[str]                     # 技能清單
    experience_years: int                 # 工作年資
    education: str                        # 學歷
    preferences: Dict[str, Any]           # 偏好設定
    parsed_at: datetime                   # 解析時間

class JobState(TypedDict):
    """職缺管理狀態
    儲存全部職缺、匹配職缺、匹配度分數與推薦理由。
    """
    jobs: List[Dict[str, Any]]            # 職缺清單
    matched_jobs: List[Dict[str, Any]]    # 匹配的職缺
    match_scores: Dict[str, float]        # 匹配度分數
    recommendations: List[str]            # 推薦理由
    last_updated: datetime                # 最後更新時間

class ConversationState(TypedDict):
    """對話上下文狀態
    儲存對話訊息、意圖、上下文與摘要。
    """
    messages: List[BaseMessage]           # 對話訊息列表
    current_intent: str                   # 當前意圖
    context: Dict[str, Any]               # 對話上下文
    history_summary: str                  # 歷史摘要
    turn_count: int                       # 對話輪次

class SystemState(TypedDict):
    """系統執行狀態
    追蹤執行節點、流程狀態、錯誤與元數據。
    """
    current_node: str                     # 當前執行節點
    workflow_status: str                  # 工作流程狀態
    error_message: Optional[str]          # 錯誤訊息
    retry_count: int                      # 重試次數
    metadata: Dict[str, Any]              # 元數據

class AgentState(TypedDict):
    """整合的 Agent 狀態
    包含所有子狀態，作為 LangGraph 的主要狀態結構。
    """
    user_profile: UserProfileState
    job_state: JobState
    conversation: ConversationState
    system: SystemState
    next_action: str                      # 下一步動作
    is_complete: bool                     # 是否完成
