# Job Search Agent - Workflow & Module Integration (2026版)

## 整併設計原則

- 主流程以 StateGraph/LangGraph nodes 為核心，流程導向、單一職責。
- agent_nodes.py 作為 plugin/子流程，僅由 router/decision node 分流調用，支援多 agent/多任務。
- 所有重複邏輯（如職缺搜尋、薪資分析、履歷優化等）統一抽象於 `src/agent/services/`，供 nodes 與 agent_nodes 共用。
- 每個 node 只負責流程調度與狀態更新，具體業務邏輯統一在 service 層維護。

---

## 新版流程圖（文字版）

```
[Entry: conversation_node]
      ↓
[resume_parser_node] → [job_matcher_node] → [decision_node]
      ↓                        ↓                ↓
[router_node] ──→─┬─→─ [agent_nodes plugin] (多任務/多agent)
                 │
                 └─→─ [recommendation_node]
                 └─→─ [skill_analyzer_node]
                 └─→─ [manual_review_node]
                 └─→─ [error_handle_node]
                 └─→─ [finalizer_node] → END
```

- router_node/decision_node 根據 state 分流，必要時調用 agent_nodes plugin。
- plugin 內部根據 tasks 動態分派 agent，結果寫入 state["results"]。

---

## 模組循序圖（文字版）

```
[workflow entry]
    ↓
[conversation_node] → [resume_parser_node] → [job_matcher_node]
    ↓
[decision_node]
    ↓
[router_node]
    ├─→ [recommendation_node]
    ├─→ [skill_analyzer_node]
    ├─→ [manual_review_node]
    ├─→ [error_handle_node]
    ├─→ [finalizer_node]
    └─→ [agent_nodes plugin]
            ↓
        [JobSearchAgent.run()] / [SalaryAnalyzerAgent.run()] / ...
            ↓
        [service 層邏輯]
            ↓
        [state["results"] 更新]
```

---

## 實作建議

1. **src/agent/services/**  
   - 將職缺搜尋、薪資分析、履歷優化等共用邏輯抽象為 service。
   - nodes 及 agent_nodes plugin 均調用 service 層。

2. **src/langgraph/agent_nodes.py**  
   - 保持任務導向設計，根據 state["tasks"] 分派 agent。
   - plugin 只由 router/decision node 分流調用。

3. **src/graph/workflow.py**  
   - workflow 以 nodes 為主，plugin/子流程僅在必要時分流。

4. **docs/design/graph_design.md**  
   - 持續補充架構設計、分流策略、維護原則，方便團隊協作。

---

## 主流框架設計參考

- 類似 Airflow DAG、Prefect Flow：主流程明確，plugin/operator 可動態擴展。
- 類似 FastAPI/Flask Blueprint：主路由清晰，plugin/子模組可獨立維護。

---

## 維護與擴展原則

- 主流程清晰、單一職責。
- plugin/子流程獨立，僅由主流程分流調用。
- 業務邏輯統一於 service 層，減少重複維護。
- 文檔同步設計原則，方便新成員理解與擴展。
