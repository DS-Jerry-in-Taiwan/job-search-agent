# State Schema 設計文檔

## 概述
本文件說明 job_search_agent 的 State Schema 設計，作為 Multi-Agent 系統的核心數據結構。

---

## UserProfileState
- 用途：儲存用戶履歷資訊、技能清單、偏好設定
- 欄位：
  - user_id: 用戶唯一識別碼
  - resume_text: 履歷原始文本
  - skills: 技能清單
  - experience_years: 工作年資
  - education: 學歷
  - preferences: 偏好設定
  - parsed_at: 解析時間

## JobState
- 用途：儲存職缺清單、匹配職缺、匹配度分數、推薦理由
- 欄位：
  - jobs: 職缺清單
  - matched_jobs: 匹配職缺
  - match_scores: 匹配度分數
  - recommendations: 推薦理由
  - last_updated: 最後更新時間

## ConversationState
- 用途：儲存對話訊息、意圖、上下文、摘要
- 欄位：
  - messages: 對話訊息列表
  - current_intent: 當前意圖
  - context: 對話上下文
  - history_summary: 歷史摘要
  - turn_count: 對話輪次

## SystemState
- 用途：儲存系統執行狀態、錯誤訊息、元數據
- 欄位：
  - current_node: 當前執行節點
  - workflow_status: 工作流程狀態
  - error_message: 錯誤訊息
  - retry_count: 重試次數
  - metadata: 元數據

## AgentState
- 用途：整合所有子狀態，作為 LangGraph 的主要狀態結構
- 欄位：
  - user_profile: UserProfileState
  - job_state: JobState
  - conversation: ConversationState
  - system: SystemState
  - next_action: 下一步動作
  - is_complete: 是否完成

---

## 設計原則
- 單一職責：每個 State 只負責一個領域
- 類型安全：所有欄位都有明確的類型註解
- 可擴展性：Dict[str, Any] 預留擴展空間
- 符合 LangGraph TypedDict 規範
- 命名一致性：snake_case

---

## 使用範例

```python
from src.state.operations import create_initial_state, update_user_profile

state = create_initial_state()
state = update_user_profile(state, {"user_id": "user_001", "skills": ["Python", "AI"]})
```

---

## 設計決策
- 參考 Phase 2 的職缺數據結構
- 支援多輪對話與系統流程控制
- 預留擴展空間以因應未來需求

---

## 版本
- 2025-12-23 初版
