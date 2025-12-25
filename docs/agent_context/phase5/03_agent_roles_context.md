# ✅ **很好！繼續第 3 份文件**

***

## ✍️ **【第 3 份檔案內容】**

### **檔案：`docs/agent_context/phase5/03_agent_roles_context.md`**

**完整複製以下內容貼入**：

```markdown
# Phase 5 - Agent 角色與職責

**階段**: Day 1 步驟4 - Graph 構建  
**團隊模式**: 4 Agent 協作（自動執行）

---

## 🎪 Agent 團隊總覽

在 Graph 構建階段，4 個 Agent 的角色如下：

| Agent | 角色 | 核心職責 | 產出物 |
|-------|------|---------|--------|
| **@INFRA** | 環境工程師 | 建立目錄與基礎檔案 | 目錄結構 + 5檔案 |
| **@ARCH** | 架構設計師 | 設計Graph架構 | Graph設計規格 |
| **@CODER** | 程式實現工程師 | 實現完整Graph | 完整程式碼 |
| **@ANALYST** | 品質分析師 | 驗證與測試 | 測試報告 |

⚠️ **Phase 5 特點**: 無 Checkpoint，全程自動執行

---

## 🔧 @INFRA - 環境工程師

### **角色定位**
負責建立 Graph 構建所需的基礎環境，確保目錄結構正確、檔案就位。

### **核心職責**

1. **建立目錄結構**
   ```
   src/graph/          # Graph 實現目錄
   tests/graph/        # Graph 測試目錄
   ```

2. **建立基礎檔案 (5個)**
   ```
   src/graph/__init__.py
   src/graph/workflow.py
   tests/graph/__init__.py
   tests/graph/test_workflow.py
   docs/design/graph_design.md
   ```

3. **驗證依賴可用**
   - Phase 3 State Schema 可用
   - Phase 4 Nodes 可用
   - LangGraph 已安裝

### **輸入**
- Phase 3 產出：`src/state/schema.py`
- Phase 4 產出：`src/nodes/*.py`
- LangGraph 套件

### **輸出**
- ✅ 完整的目錄結構
- ✅ 5 個基礎檔案已建立
- ✅ 依賴驗證通過

### **驗證標準**
```
# 檢查目錄
ls -la src/graph/ tests/graph/

# 檢查依賴
python -c "from src.state.schema import AgentState; print('✅ State OK')"
python -c "from src.nodes import router_node; print('✅ Nodes OK')"
python -c "from langgraph.graph import StateGraph; print('✅ LangGraph OK')"
```

### **執行時間**: ~2 分鐘

---

## 🏗️ @ARCH - 架構設計師

### **角色定位**
設計 LangGraph 工作流程的完整架構，這是 AI Agent 系統的執行引擎。

### **核心職責**

#### **1. StateGraph 結構設計**

**設計目標**: 使用 AgentState 建立 StateGraph

```
from langgraph.graph import StateGraph, END
from src.state.schema import AgentState

workflow = StateGraph(AgentState)
```

**設計要點**:
- ✅ State Schema 使用 Phase 3 的 AgentState
- ✅ StateGraph 正確初始化

---

#### **2. Nodes 加入設計**

**設計目標**: 將 Phase 4 的 8 個 Nodes 加入 Graph

```
from src.nodes import (
    resume_parser_node,      # Node 1
    job_matcher_node,        # Node 2
    skill_analyzer_node,     # Node 3
    recommendation_node,     # Node 4
    conversation_node,       # Node 5
    router_node,             # Node 6 (條件路由)
    error_handler_node,      # Node 7
    finalizer_node           # Node 8
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

**設計要點**:
- ✅ 8 個 Nodes 全部加入
- ✅ Node 名稱（字串）與函數正確對應
- ✅ Node 順序清晰

---

#### **3. Edges 定義設計**

**固定 Edges 設計**:

```
# 明確的前後關係
workflow.add_edge("resume_parser", "router")
workflow.add_edge("job_matcher", "recommendation")
workflow.add_edge("recommendation", "router")
workflow.add_edge("conversation", "router")
workflow.add_edge("error_handler", "router")
workflow.add_edge("finalizer", END)
```

**設計邏輯**:
- `resume_parser` → `router`: 解析後進入路由判斷
- `job_matcher` → `recommendation`: 匹配後生成推薦
- `recommendation` → `router`: 推薦後進入路由判斷
- `conversation` → `router`: 對話後進入路由判斷
- `error_handler` → `router`: 錯誤處理後重新路由
- `finalizer` → `END`: 結束流程

---

#### **4. 條件路由設計** ⭐ 核心！

**設計目標**: router_node 根據 State 決定下一步

```
# 條件路由邏輯
workflow.add_conditional_edges(
    "router",                          # 從哪個 Node 開始
    lambda state: router_node(state),  # 路由函數
    {                                   # 路由映射
        "resume_parser": "resume_parser",
        "job_matcher": "job_matcher",
        "conversation": "conversation",
        "__end__": "finalizer"
    }
)
```

**路由邏輯**:
```
# router_node 返回值決定下一步
if not state["user_profile"]["skills"]:
    → "resume_parser"      # 履歷未解析，重新解析
    
elif not state["job_state"]["matched_jobs"]:
    → "job_matcher"        # 職缺未匹配，執行匹配
    
elif state["conversation"]["messages"] and not state["is_complete"]:
    → "conversation"       # 需要對話回應
    
else:
    → "__end__"            # 結束流程
```

**設計要點**:
- ✅ router_node 返回 str（特殊Node）
- ✅ 返回值與映射字典一致
- ✅ 邏輯清晰無死循環

---

#### **5. 入口與編譯設計**

```
# 設定入口點
workflow.set_entry_point("resume_parser")

# 編譯 Graph
app = workflow.compile()

return app
```

**設計要點**:
- ✅ 入口點設為 `resume_parser`（從履歷解析開始）
- ✅ compile() 生成可執行的 Graph

---

#### **6. 工作流程示意圖**

```
                    START
                      ↓
              [resume_parser_node]
                      ↓
                [router_node] ━━━━━━━━┓
                      ↓                ↓
              [job_matcher_node]    條件判斷
                      ↓                ↓
           [recommendation_node]  [conversation_node]
                      ↓                ↓
                [router_node] ←━━━━━━━┛
                      ↓
               [finalizer_node]
                      ↓
                     END
```

---

### **設計原則**

1. **明確的流程邏輯**
   - 從履歷解析開始
   - 通過路由器判斷下一步
   - 最終進入結束節點

2. **條件路由清晰**
   - router_node 是唯一的決策點
   - 所有邏輯集中在一個地方

3. **錯誤處理機制**
   - error_handler_node 處理錯誤
   - 處理後重新進入 router

4. **可擴展性**
   - 新增 Node 只需 add_node + add_edge
   - 修改邏輯只需調整 router_node

### **輸入**
- Phase 4 的 8 個 Nodes
- Phase 3 的 AgentState
- @INFRA 建立的檔案結構

### **輸出**
- ✅ 完整的 Graph 架構設計
- ✅ Nodes/Edges 定義清晰
- ✅ 條件路由邏輯正確

### **執行時間**: ~3 分鐘

---

## 💻 @CODER - 程式實現工程師

### **角色定位**
將 @ARCH 的設計轉化為可執行的程式碼，實現完整的 LangGraph 工作流程。

### **核心職責**

#### **1. 實現 workflow.py**

**完整實現**:

```
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
        
    工作流程:
        1. resume_parser: 解析履歷
        2. router: 條件判斷
        3. job_matcher: 匹配職缺
        4. recommendation: 生成推薦
        5. conversation: 對話回應
        6. finalizer: 結束流程
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

# 建立全局實例（方便直接使用）
graph_app = create_workflow()
```

#### **2. 實現 __init__.py**

```
# src/graph/__init__.py
"""Graph 模組 - LangGraph 工作流程"""

from .workflow import create_workflow, graph_app

__all__ = ["create_workflow", "graph_app"]
```

#### **3. 實現測試案例**

```
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
    assert result["system"]["workflow_status"] == "completed"
```

#### **4. 撰寫設計文檔**

```
# docs/design/graph_design.md

# LangGraph 工作流程設計

## 概覽
完整的 AI Agent 工作流程，使用 LangGraph 實現。

## 架構
- StateGraph: 使用 AgentState
- Nodes: 8 個核心 Nodes
- Edges: 固定 + 條件路由

## 使用範例
...
```

### **輸入**
- @ARCH 的 Graph 設計規格

### **輸出**
- ✅ src/graph/workflow.py 完整實現
- ✅ src/graph/__init__.py 導出完整
- ✅ tests/graph/test_workflow.py (4+ 測試)
- ✅ docs/design/graph_design.md

### **驗證標準**
```
# 可以正常 import
python -c "from src.graph import create_workflow; print('OK')"

# 測試可以收集
pytest tests/graph/ --collect-only
```

### **執行時間**: ~4 分鐘

---

## 🧪 @ANALYST - 品質分析師

### **角色定位**
驗證 Graph 的正確性、完整性與品質，確保工作流程可以正常執行。

### **核心職責**

#### **1. 執行測試套件**

```
pytest tests/graph/ -v --cov=src/graph
```

**驗證標準**:
- ✅ 所有測試通過 (4+)
- ✅ 測試覆蓋率 > 80%

#### **2. 端到端測試**

```
from src.graph import create_workflow
from src.state.operations import create_initial_state

app = create_workflow()
state = create_initial_state()

# 執行完整工作流程
result = app.invoke(state)

# 驗證結果
assert result["user_profile"]["skills"]
assert result["job_state"]["matched_jobs"]
assert result["is_complete"] == True

print("✅ 端到端測試通過")
```

#### **3. 類型檢查**

```
mypy src/graph/ --strict
```

**驗證標準**:
- ✅ 類型檢查 100% 通過

#### **4. 程式碼品質檢查**

- [ ] workflow.py 結構清晰
- [ ] Nodes 加入順序合理
- [ ] Edges 定義完整
- [ ] 條件路由邏輯正確
- [ ] 文檔完整

#### **5. 生成測試報告**

```
Graph 構建測試報告
==================

測試結果: ✅ PASSED (4/4)
類型檢查: ✅ PASSED
測試覆蓋率: 85%
程式碼品質: A

功能驗證:
✅ StateGraph 建立成功
✅ 8 個 Nodes 全部加入
✅ Edges 定義完整
✅ 條件路由正確
✅ Graph 編譯成功
✅ 端到端測試通過

建議:
- 無重大問題
- 可進入 Phase 6

結論:
✅ Phase 5 (Graph 構建) 驗證通過
```

### **執行時間**: ~3 分鐘

---

## 🔄 Agent 協作流程

```
@INFRA (環境準備)
    ↓
    建立目錄與5個檔案
    ↓
@ARCH (Graph架構設計)
    ↓
    設計StateGraph架構
    ↓
@CODER (程式實現)
    ↓
    實現完整Graph與測試
    ↓
@ANALYST (測試驗證)
    ↓
    執行測試與品質檢查
    ↓
    ✅ Phase 5 完成
```

**⚠️ 無 Checkpoint，全程自動執行！**

---

## 🎯 團隊協作原則

1. **流暢執行**
   - 無 Checkpoint 打斷
   - Agent 自動交接

2. **依賴明確**
   - 必須依賴 Phase 3-4 產出
   - LangGraph 必須已安裝

3. **品質保證**
   - 端到端測試為主
   - 類型檢查確保正確性

4. **文檔同步**
   - 程式碼與文檔同步更新

---

**Phase 5 讓 AI Agent 真正「動起來」！** 🚀
```
