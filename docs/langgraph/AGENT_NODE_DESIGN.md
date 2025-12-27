# Phase 12.5-1 Agent Node 設計文檔

## 1. Agent Node 包裝模式

### 統一介面
- 每個 Agent Node 接收 AgentState，返回更新後的 AgentState。
- 任務過濾：根據 intent 過濾 state["tasks"]。
- 錯誤處理：try/except 捕獲 Agent 執行異常，記錄到 state["error"]。
- 結果聚合：將 Agent 執行結果追加到 state["results"]。

### 4 個 Agent Node
- job_search_node(state): 包裝 JobSearchAgent，intent="search_job"
- salary_analyze_node(state): 包裝 SalaryAnalyzerAgent，intent="analyze_salary"
- interview_coach_node(state): 包裝 InterviewCoachAgent，intent="prepare_interview"
- resume_optimize_node(state): 包裝 ResumeOptimizerAgent，intent="optimize_resume"

## 2. LLM 整合策略

### 意圖識別 Prompt
```
分析以下使用者查詢，識別意圖。

可能的意圖:
- search_job: 搜尋職缺、找工作
- analyze_salary: 薪資分析、薪水查詢
- prepare_interview: 面試準備、面試技巧
- optimize_resume: 履歷優化、履歷修改

使用者查詢: {query}

請以 JSON 格式返回識別的意圖列表:
{"intents": ["intent1", "intent2"]}
```

### 任務拆解 Prompt
```
從以下查詢中提取 {intent} 的參數。

查詢: {query}

需要提取的參數:
- location: 地點（如：台北、新竹）
- skill: 技能（如：Python、AI）
- experience: 經驗年資（如：3年、5年以上）
- salary_range: 薪資範圍（如：50-80萬）
- job_title: 職位名稱（如：工程師、經理）

以 JSON 格式返回:
{"location": "...", "skill": "...", ...}
```

## 3. Memory 整合策略

### 載入記憶
- 從 ConversationMemory 讀取 session_id 對應的最近 5 輪歷史
- 讀取 user_id 對應的使用者偏好
- 更新 state["context"]

### 儲存記憶
- save_conversation(session_id, user_id, query, response, intents, results)
- 更新對話內容與偏好

## 4. 設計原則

- Node 函數皆為純函數，無副作用
- 錯誤處理優雅降級
- 類型註解完整
- 文檔字串完整

## 5. 參考

- Phase13_Agent_Wrapping_HighLevel_Design.md
- docs/agent_context/phase12_5_1/03_agent_roles_context.md
- docs/agent_context/phase12_5_1/04_agent_prompts_context.md
