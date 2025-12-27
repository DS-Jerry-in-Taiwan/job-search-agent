# LangGraph StateGraph 架構設計

## 1. 流程圖

```
Entry Point (初始狀態)
    |
    v
load_context_node
    |
    v
identify_intent_node
    |
    v
decompose_tasks_node
    |
    v
route_to_agents (條件分支)
    ├─→ job_search
    ├─→ salary_analyze
    ├─→ interview_coach
    └─→ resume_optimize
    |
    v
integrate_results_node
    |
    v
update_memory_node
    |
    v
END
```

## 2. 節點說明

- **load_context_node**：載入對話上下文（歷史、偏好）
- **identify_intent_node**：意圖識別（LLM/關鍵詞）
- **decompose_tasks_node**：根據意圖拆解任務
- **route_to_agents**：根據意圖分流到不同 Agent
- **integrate_results_node**：整合所有 Agent 結果
- **update_memory_node**：更新對話記憶

## 3. 路由邏輯

```python
def route_to_agents(state: AgentState) -> str:
    intents = state.get("intents", [])
    if not intents:
        return "integrate_results"
    if "search_job" in intents:
        return "job_search"
    elif "analyze_salary" in intents:
        return "salary_analyze"
    elif "prepare_interview" in intents:
        return "interview_coach"
    elif "optimize_resume" in intents:
        return "resume_optimize"
    else:
        return "integrate_results"
```

## 4. Node 介面標準

```python
def standard_node_template(state: AgentState) -> AgentState:
    try:
        # 驗證輸入
        # 執行邏輯
        # 更新狀態
        # 清除錯誤
        pass
    except Exception as e:
        state["error"] = str(e)
        state["retry_count"] = state.get("retry_count", 0) + 1
    return state
```

## 5. 設計原則

- 流程設計清晰可視化
- Node 保持純函數特性
- 路由邏輯明確
- 錯誤處理優雅降級

## 6. 參考

- Phase12.5_LangGraph_Foundation_HighLevel_Design.md
- docs/agent_context/phase12.5/02_dev_flow_context.md
- docs/agent_context/phase12.5/03_agent_roles_context.md
