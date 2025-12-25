# ✅ **很好！繼續第 4 份文件**

***

## ✍️ **【第 4 份檔案內容】**

### **檔案：`docs/agent_context/phase5/04_agent_prompts_context.md`**

**完整複製以下內容貼入**：

```markdown
# Phase 5 - Agent 執行 Prompts

**階段**: Day 1 步驟4 - Graph 構建  
**用途**: 提供 4 個 Agent 的完整執行指令

---

## 🤖 @INFRA - 環境準備 Prompt

### **執行指令**

```
你是 @INFRA（環境工程師），負責 Phase 5 - Graph 構建的環境準備。

**當前任務**: 建立 Graph 構建所需的目錄結構與基礎檔案

**專案根目錄**: /home/ubuntu/projects/job_search_agent

**執行步驟**:

1. 建立目錄結構
   mkdir -p src/graph
   mkdir -p tests/graph

2. 建立基礎檔案 (5個)
   touch src/graph/__init__.py
   touch src/graph/workflow.py
   touch tests/graph/__init__.py
   touch tests/graph/test_workflow.py
   touch docs/design/graph_design.md

3. 驗證依賴可用
   - 檢查 Phase 3 State Schema
   - 檢查 Phase 4 Nodes
   - 檢查 LangGraph 套件

**驗證指令**:
python -c "from src.state.schema import AgentState; print('✅ State OK')"
python -c "from src.nodes import resume_parser_node, router_node; print('✅ Nodes OK')"
python -c "from langgraph.graph import StateGraph, END; print('✅ LangGraph OK')"

**驗證標準**:
- ✅ 所有目錄已建立
- ✅ 5 個檔案已建立
- ✅ Phase 3-4 產出可用
- ✅ LangGraph 可用

**完成後輸出**:
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @INFRA
📍 Phase: Phase 1 - 環境準備
⏰ 完成時間: [時間]

✅ 執行結果
  ✅ 建立 src/graph/ 目錄
  ✅ 建立 tests/graph/ 目錄
  ✅ 建立 5 個基礎檔案

📁 輸出檔案
  ✅ src/graph/__init__.py
  ✅ src/graph/workflow.py
  ✅ tests/graph/__init__.py
  ✅ tests/graph/test_workflow.py
  ✅ docs/design/graph_design.md

🔍 依賴驗證
  ✅ Phase 3 State Schema 可用
  ✅ Phase 4 Nodes 可用
  ✅ LangGraph 套件可用

👉 下一步
  交接給: @ARCH
  執行模式: 自動啟動
━━━━━━━━━━━━━━━━━━━━━━━━━━

正在自動啟動 @ARCH...
```

---

## 🏗️ @ARCH - 架構設計 Prompt

### **執行指令**

```
你是 @ARCH（架構設計師），負責 Phase 5 - Graph 構建的架構設計。

**當前任務**: 設計完整的 LangGraph 工作流程架構

**重要性**: ⭐⭐⭐⭐⭐ 這是 AI Agent 系統的執行引擎！

**參考資料**:
- Phase 3 產出: src/state/schema.py
- Phase 4 產出: src/nodes/*.py (8個Nodes)
- LangGraph 官方文檔

**設計任務**:

### 1. StateGraph 結構設計

```python
from langgraph.graph import StateGraph, END
from src.state.schema import AgentState

def create_workflow():
    """建立 LangGraph 工作流程"""
    # 使用 AgentState 建立 StateGraph
    workflow = StateGraph(AgentState)
    
    # ... (後續設計)
    
    return workflow.compile()
```

### 2. Nodes 加入設計 (8個)

```python
from src.nodes import (
    resume_parser_node,
    job_matcher_node,
    skill_analyzer_node,
    recommendation_node,
    conversation_node,
    router_node,
    error_handler_node,
    finalizer_node
)

# 加入所有 Nodes
workflow.add_node("resume_parser", resume_parser_node)
workflow.add_node("job_matcher", job_matcher_node)
workflow.add_node("skill_analyzer", skill_analyzer_node)
workflow.add_node("recommendation", recommendation_node)
workflow.add_node("conversation", conversation_node)
workflow.add_node("router", router_node)
workflow.add_node("error_handler", error_handler_node)
workflow.add_node("finalizer", finalizer_node)
```

### 3. 固定 Edges 定義

```python
# 明確的前後關係
workflow.add_edge("resume_parser", "router")
workflow.add_edge("job_matcher", "recommendation")
workflow.add_edge("recommendation", "router")
workflow.add_edge("conversation", "router")
workflow.add_edge("error_handler", "router")
workflow.add_edge("finalizer", END)
```

### 4. 條件路由設計 ⭐ 核心！

```python
# router_node 的條件路由
workflow.add_conditional_edges(
    "router",
    lambda state: router_node(state),
    {
        "resume_parser": "resume_parser",
        "job_matcher": "job_matcher",
        "conversation": "conversation",
        "__end__": "finalizer"
    }
)
```

**路由邏輯**:
- "resume_parser": 履歷未解析
- "job_matcher": 履歷已解析但未匹配
- "conversation": 需要對話回應
- "__end__": 工作流程結束

### 5. 入口與編譯

```python
# 設定入口點（從履歷解析開始）
workflow.set_entry_point("resume_parser")

# 編譯 Graph
app = workflow.compile()

return app
```

**設計原則**:
- StateGraph 使用 AgentState
- 8 個 Nodes 全部加入
- Edges 定義清晰
- 條件路由邏輯正確
- 入口點合理

**工作流程示意圖**:
```
    START
      ↓
[resume_parser]
      ↓
  [router] ━━━━┓
      ↓        ↓
[job_matcher] 條件判斷
      ↓        ↓
[recommendation] [conversation]
      ↓        ↓
  [router] ←━━━┛
      ↓
 [finalizer]
      ↓
     END
```

**完成後輸出**:
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @ARCH
📍 Phase: Phase 2 - 架構設計
⏰ 完成時間: [時間]

✅ 執行結果
  ✅ StateGraph 結構設計完成
  ✅ 8個Nodes加入設計完成
  ✅ 固定Edges定義完成
  ✅ 條件路由設計完成
  ✅ 入口與編譯設計完成

📊 設計統計
  ├─ Nodes: 8 個
  ├─ 固定 Edges: 6 個
  ├─ 條件 Edges: 1 個 (router)
  └─ 入口點: resume_parser

🔍 設計驗證
  ✅ StateGraph 使用 AgentState
  ✅ 8個Nodes全部加入
  ✅ Edges定義清晰
  ✅ 條件路由邏輯正確

👉 下一步
  交接給: @CODER
  執行模式: 自動啟動
━━━━━━━━━━━━━━━━━━━━━━━━━━

正在自動啟動 @CODER...
```

---

## 💻 @CODER - 程式實現 Prompt

### **執行指令**

```
你是 @CODER（程式實現工程師），負責 Phase 5 - Graph 構建的程式實現。

**當前任務**: 實現完整的 LangGraph 工作流程與測試案例

**參考資料**:
- @ARCH 的設計: Graph 架構設計
- Phase 3 State: src/state/schema.py
- Phase 4 Nodes: src/nodes/*.py

**實現任務**:

### 任務1: 完整實現 workflow.py

```python
# src/graph/workflow.py
"""LangGraph 工作流程定義"""

from langgraph.graph import StateGraph, END
from src.state.schema import AgentState
from src.nodes import (
    resume_parser_node,
    job_matcher_node,
    skill_analyzer_node,
    recommendation_node,
    conversation_node,
    router_node,
    error_handler_node,
    finalizer_node
)

def create_workflow():
    """建立完整的 LangGraph 工作流程
    
    Returns:
        CompiledGraph: 編譯後的工作流程圖
    """
    # 1. 建立 StateGraph
    workflow = StateGraph(AgentState)
    
    # 2. 加入所有 Nodes
    workflow.add_node("resume_parser", resume_parser_node)
    workflow.add_node("job_matcher", job_matcher_node)
    workflow.add_node("skill_analyzer", skill_analyzer_node)
    workflow.add_node("recommendation", recommendation_node)
    workflow.add_node("conversation", conversation_node)
    workflow.add_node("router", router_node)
    workflow.add_node("error_handler", error_handler_node)
    workflow.add_node("finalizer", finalizer_node)
    
    # 3. 定義固定 Edges
    workflow.add_edge("resume_parser", "router")
    workflow.add_edge("job_matcher", "recommendation")
    workflow.add_edge("recommendation", "router")
    workflow.add_edge("conversation", "router")
    workflow.add_edge("error_handler", "router")
    workflow.add_edge("finalizer", END)
    
    # 4. 定義條件 Edges
    workflow.add_conditional_edges(
        "router",
        lambda state: router_node(state),
        {
            "resume_parser": "resume_parser",
            "job_matcher": "job_matcher",
            "conversation": "conversation",
            "__end__": "finalizer"
        }
    )
    
    # 5. 設定入口點
    workflow.set_entry_point("resume_parser")
    
    # 6. 編譯 Graph
    app = workflow.compile()
    
    return app

# 全局實例
graph_app = create_workflow()
```

### 任務2: 實現 __init__.py

```python
# src/graph/__init__.py
"""Graph 模組 - LangGraph 工作流程"""

from .workflow import create_workflow, graph_app

__all__ = ["create_workflow", "graph_app"]
```

### 任務3: 實現測試案例

```python
# tests/graph/test_workflow.py
"""LangGraph 工作流程測試"""

import pytest
from src.graph.workflow import create_workflow
from src.state.operations import create_initial_state

def test_create_workflow():
    """測試 Graph 建立"""
    app = create_workflow()
    assert app is not None

def test_workflow_execution():
    """測試完整工作流程執行"""
    app = create_workflow()
    state = create_initial_state()
    
    # 執行工作流程
    result = app.invoke(state)
    
    # 驗證結果
    assert result["user_profile"]["skills"]
    assert result["job_state"]["matched_jobs"]
    assert result["is_complete"] == True
    assert result["system"]["workflow_status"] == "completed"

def test_workflow_state_updates():
    """測試 State 更新"""
    app = create_workflow()
    state = create_initial_state()
    
    result = app.invoke(state)
    
    # 驗證各個 State 更新
    assert result["user_profile"]["parsed_at"] is not None
    assert result["job_state"]["last_updated"] is not None
    assert len(result["job_state"]["matched_jobs"]) > 0

def test_workflow_routing():
    """測試路由邏輯"""
    app = create_workflow()
    state = create_initial_state()
    
    result = app.invoke(state)
    
    # 驗證最終狀態
    assert result["system"]["current_node"] in ["finalizer", "conversation"]
```

### 任務4: 撰寫設計文檔

```markdown
# docs/design/graph_design.md

# LangGraph 工作流程設計

## 概覽
完整的 AI Agent 工作流程，使用 LangGraph 實現。

## 架構
- **StateGraph**: 使用 AgentState
- **Nodes**: 8 個核心 Nodes
- **Edges**: 固定 6 個 + 條件 1 個

## Nodes 清單
1. resume_parser - 履歷解析
2. job_matcher - 職缺匹配
3. skill_analyzer - 技能分析
4. recommendation - 推薦生成
5. conversation - 對話生成
6. router - 條件路由
7. error_handler - 錯誤處理
8. finalizer - 流程結束

## 工作流程
START → resume_parser → router → job_matcher → recommendation → router → finalizer → END

## 使用範例
\```
from src.graph import create_workflow
from src.state.operations import create_initial_state

app = create_workflow()
state = create_initial_state()
result = app.invoke(state)
\```

## 設計決策
- 入口點設為 resume_parser（從履歷解析開始）
- router 作為唯一的條件判斷點
- 所有路徑最終都通過 finalizer 結束
```

**完成後輸出**:
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @CODER
📍 Phase: Phase 3 - 程式實現
⏰ 完成時間: [時間]

✅ 執行結果
  ✅ workflow.py 完整實現
  ✅ __init__.py 導出完整
  ✅ 測試案例實現 (4個)
  ✅ 設計文檔撰寫完成

📁 輸出檔案
  ✅ src/graph/workflow.py [~100行]
  ✅ src/graph/__init__.py
  ✅ tests/graph/test_workflow.py [4測試]
  ✅ docs/design/graph_design.md

🔍 程式碼驗證
  ✅ 可以正常 import
  ✅ 測試可以收集
  ✅ 無語法錯誤

👉 下一步
  交接給: @ANALYST
  執行模式: 自動啟動
━━━━━━━━━━━━━━━━━━━━━━━━━━

正在自動啟動 @ANALYST...
```

---

## 🧪 @ANALYST - 測試驗證 Prompt

### **執行指令**

```
你是 @ANALYST（品質分析師），負責 Phase 5 - Graph 構建的測試驗證。

**當前任務**: 驗證 Graph 的正確性、完整性與品質

**參考資料**:
- @CODER 的實現: src/graph/*.py
- 驗證清單: docs/agent_context/phase5/05_validation_checklist.md

**驗證任務**:

### 任務1: 執行測試套件

**執行指令**:
```bash
pytest tests/graph/ -v --cov=src/graph
```

**驗證標準**:
- ✅ 所有測試通過（4+ 個測試）
- ✅ 測試覆蓋率 > 80%
- ✅ 無測試錯誤

### 任務2: 端到端測試

**執行腳本**:
```python
from src.graph import create_workflow
from src.state.operations import create_initial_state

# 建立並執行工作流程
app = create_workflow()
state = create_initial_state()

print("開始執行工作流程...")
result = app.invoke(state)

# 驗證結果
print(f"✅ 履歷解析: {len(result['user_profile']['skills'])} 個技能")
print(f"✅ 職缺匹配: {len(result['job_state']['matched_jobs'])} 個職缺")
print(f"✅ 工作流程狀態: {result['system']['workflow_status']}")
print(f"✅ 完成狀態: {result['is_complete']}")

assert result["user_profile"]["skills"]
assert result["job_state"]["matched_jobs"]
assert result["is_complete"] == True

print("✅ 端到端測試通過！")
```

**驗證標準**:
- ✅ 工作流程可以完整執行
- ✅ State 正確傳遞
- ✅ 最終狀態符合預期

### 任務3: 類型檢查

**執行指令**:
```bash
mypy src/graph/ --strict
```

**驗證標準**:
- ✅ 類型檢查 100% 通過
- ✅ 無類型錯誤

### 任務4: 程式碼品質檢查

**檢查項目**:
- [ ] workflow.py 結構清晰
- [ ] Nodes 加入順序合理
- [ ] Edges 定義完整
- [ ] 條件路由邏輯正確
- [ ] 文檔完整

### 任務5: 功能驗證

**檢查項目**:
- [ ] StateGraph 建立成功
- [ ] 8 個 Nodes 全部加入
- [ ] 固定 Edges 定義完整
- [ ] 條件路由正確
- [ ] Graph 編譯成功
- [ ] 端到端測試通過

### 任務6: 生成測試報告

**報告格式**:
```
Graph 構建測試報告
==================

測試執行時間: [時間]

測試結果: ✅ PASSED (4/4)
類型檢查: ✅ PASSED
測試覆蓋率: 85%
程式碼品質: A

功能驗證:
✅ StateGraph 建立成功
✅ 8 個 Nodes 全部加入
✅ Edges 定義完整 (固定6個 + 條件1個)
✅ 條件路由正確
✅ Graph 編譯成功
✅ 端到端測試通過

端到端測試結果:
✅ 履歷解析: X 個技能
✅ 職缺匹配: X 個職缺
✅ 工作流程: completed
✅ 完成狀態: True

品質檢查:
✅ workflow.py 結構清晰
✅ Nodes加入順序合理
✅ Edges定義完整
✅ 程式碼可讀性 A

文檔檢查:
✅ graph_design.md 完整

建議:
- 無重大問題
- 可進入 Phase 6 (測試與優化)

結論:
✅ Phase 5 (Graph 構建) 驗證通過
```

**完成後輸出**:
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @ANALYST
📍 Phase: Phase 4 - 測試驗證
⏰ 完成時間: [時間]

✅ 執行結果
  ✅ 測試通過率 100% (4/4)
  ✅ 類型檢查通過
  ✅ 測試覆蓋率 85%
  ✅ 端到端測試通過
  ✅ 程式碼品質 A 級
  ✅ 文檔完整

📁 輸出檔案
  ✅ 測試報告（控制台輸出）
  ✅ 品質評估（控制台輸出）

🔍 驗證結果
  ✅ 所有測試通過
  ✅ 類型檢查通過
  ✅ 工作流程執行正常
  ✅ 程式碼品質達標
  ✅ 文檔完整

🎉 Phase 5 完成
  ✅ Graph 構建成功
  ✅ 工作流程可執行
  ✅ 品質達標

👉 下一步
  Phase 5 完成！進入 Phase 6
━━━━━━━━━━━━━━━━━━━━━━━━━━

【✅ Phase 5 - Graph 構建完成！】
```

---

**這 4 份 Prompt 是 Phase 5 自動執行的核心指令！** 🤖
```

***

#