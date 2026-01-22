# Job Search Agent - Multi-Agent Workflow Platform

## 專案簡介

Job Search Agent 是一個基於 LangGraph 的多智能體（Multi-Agent）協作平台，專為履歷解析、職缺推薦與職涯輔導等場景設計。專案結合多個專業 Agent，透過可視化流程圖與 API 整合，實現自動化履歷處理、技能分析、職缺匹配與推薦等功能。

---

## 2026/01 架構重大調整

- **Plugin-based Agent Workflow**：核心流程全面遷移為 plugin 架構，所有智能體節點統一由 `src/agent/plugins/agent_nodes.py` 調度，易於擴充與維護。
- **Service Layer 拆分**：每個 Agent 對應獨立 Service，職責單一、可測試性提升（如 `src/agent/services/skill_service.py`）。
- **decision_result 輸出統一**：所有流程結果的決策分數與建議，統一輸出於 `result["decision_result"]`，便於前後端與測試驗收。
- **測試與 CI 強化**：`tests/graph/test_workflow.py` 等測試已對應新版資料結構，驗收標準明確。
- **.gitignore 完善**：敏感、暫存、mock、資料、環境檔案等已預設排除。

---

## 開發應用場景

- **履歷解析與結構化**：自動解析 PDF 履歷，提取結構化資訊（基本資料、技能、經歷等）。
- **技能分析與職缺推薦**：根據履歷內容分析技能，智能推薦最適合的職缺。
- **多 Agent 協作**：每個節點對應一個專業 Agent（如 resume_parser、skill_analyzer、job_matcher、recommendation、router 等），可擴充更多智能體。
- **流程可視化**：內建 mermaid.js 流程圖前端 demo，方便開發者與用戶理解整體協作流程。
- **API 整合**：RESTful API 支援前後端分離，易於與第三方平台或 UI 整合。

## 架構說明

```
+-------------------+      +-------------------+      +-------------------+
|   Resume Parser   | -->  |  Skill Analyzer   | -->  |   Job Matcher     |
+-------------------+      +-------------------+      +-------------------+
         |                                                    |
         v                                                    v
+-------------------+      +-------------------+      +-------------------+
| Recommendation    | -->  |      Router       | -->  |   Conversation    |
+-------------------+      +-------------------+      +-------------------+
```

- **Plugin Node 調度**：所有流程節點統一由 `src/agent/plugins/agent_nodes.py` 管理，支援自定義與熱插拔。
- **Service Layer**：如 `src/agent/services/`，每個業務邏輯獨立，便於單元測試與維護。
- **StateGraph（LangGraph）**：負責定義 Agent 節點、流程邏輯與狀態傳遞。
- **API 層**：FastAPI 提供 /graph/visualize 等端點，支援流程查詢與前端渲染。
- **前端 demo**：ui/graph_demo.html + mermaid.js，動態渲染 workflow 流程圖。
- **測試覆蓋**：tests/ 目錄下涵蓋 API、流程、節點調用等單元與整合測試。

## 快速啟動

1. 安裝依賴
   ```
   pip install -r requirements.txt
   ```

2. 啟動 API 服務
   ```
   uvicorn src.api.main:app --reload --port 8000
   ```

3. 開啟前端 demo
   ```
   # 用瀏覽器打開 ui/graph_demo.html
   ```

4. 查看流程圖與節點狀態

## 適用對象

- AI/ML 工程師、資料科學家
- HR Tech/職涯平台開發團隊
- 需要多 Agent 協作與流程自動化的應用場景

## 特色

- 多 Agent 協作與可擴充性
- Plugin/service 架構，維護與擴展容易
- decision_result 輸出統一，驗收與串接更方便
- 流程圖可視化，易於理解與維護
- 完整 API/前端/測試整合
- 支援自定義 workflow 與多場景應用

---
