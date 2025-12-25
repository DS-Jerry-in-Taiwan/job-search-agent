# ✅ **很好！繼續第 2 份文件**

***

## ✍️ **【第 2 份檔案內容】**

### **檔案：`docs/agent_context/phase5/02_dev_flow_context.md`**

**完整複製以下內容貼入**：

```markdown
# Phase 5 - Graph 構建開發流程

**階段**: Day 1 步驟4 - Graph 構建  
**執行模式**: 自動執行（無 Checkpoint）  
**預估時間**: 10-12 分鐘

---

## 🚀 開發流程總覽

```
Phase 1 (INFRA)  → Phase 2 (ARCH)     → Phase 3 (CODER)    → Phase 4 (ANALYST)
環境準備          Graph架構設計         程式實現              測試驗證
~2分鐘            ~3分鐘               ~4分鐘                ~3分鐘

⚠️ 注意: Phase 5 無 Checkpoint，全程自動執行
```

---

## 📋 Phase 1: 環境準備 (@INFRA)

### **目標**
建立 Graph 構建所需的目錄結構與基礎檔案

### **執行步驟**

1. **建立目錄結構**
```
mkdir -p src/graph
mkdir -p tests/graph
```

2. **建立基礎檔案**
```
touch src/graph/__init__.py
touch src/graph/workflow.py
touch tests/graph/__init__.py
touch tests/graph/test_workflow.py
touch docs/design/graph_design.md
```

3. **驗證依賴可用**
```
# 檢查 Phase 3 State
python -c "from src.state.schema import AgentState; print('✅ State OK')"

# 檢查 Phase 4 Nodes
python -c "from src.nodes import resume_parser_node, router_node; print('✅ Nodes OK')"

# 檢查 LangGraph
python -c "from langgraph.graph import StateGraph, END; print('✅ LangGraph OK')"
```

### **驗證標準**
- ✅ 目錄結構正確
- ✅ 5 個檔案已建立
- ✅ Phase 3-4 產出可用
- ✅ LangGraph 已安裝

### **預期輸出**
```
src/graph/ (2個檔案)
tests/graph/ (2個檔案)
docs/design/graph_design.md
Phase 3-4 依賴 ✅ 可用
LangGraph ✅ 可用
```

### **預估時間**: ~2 分鐘

---

## 🏗️ Phase 2: Graph 架構設計 (@ARCH)

### **目標**
設計完整的 LangGraph 工作流程架構

### **設計任務**

#### **任務1: StateGraph 結構設計**

```
# src/graph/workflow.py
from langgraph.graph import StateGraph, END
from src.state.schema import AgentState

def create_workflow() -> StateGraph:
    """建立 LangGraph 工作流程
    
    架構設計:
    1. 使用 AgentState 作為 State Schema
    2. 加入 8 個 Nodes
    3. 定義固定 Edges
    4. 定義條件路由
    5. 設定入口點
    """
    workflow = StateGraph(AgentState)
    
    # ... (後續實現)
    
    return workflow
```

#### **任務2: Nodes 加入設計**

```
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

# 加入 8 個 Nodes
workflow.add_node("resume_parser", resume_parser_node)
workflow.add_node("job_matcher", job_matcher_node)
workflow.add_node("skill_analyzer", skill_analyzer_node)
workflow.add_node("recommendation", recommendation_node)
workflow.add_node("conversation", conversation_node)
workflow.add_node("router", router_node)
workflow.add_node("error_handler", error_handler_node)
workflow.add_node("finalizer", finalizer_node)
```

#### **任務3: Edges 定義設計**

**固定 Edges**:
```
# 明確的前後關係
workflow.add_edge("resume_parser", "router")
workflow.add_edge("job_matcher", "recommendation")
workflow.add_edge("recommendation", "router")
workflow.add_edge("conversation", "router")
workflow.add_edge("error_handler", "router")
workflow.add_edge("finalizer", END)
```

**條件 Edges**:
```
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

#### **任務4: 入口與編譯設計**

```
# 設定入口點
workflow.set_entry_point("resume_parser")

# 編譯 Graph
app = workflow.compile()

return app
```

### **設計驗證標準**
- ✅ StateGraph 建立邏輯正確
- ✅ 8個Nodes加入設計完整
- ✅ Edges定義清晰
- ✅ 條件路由邏輯正確
- ✅ 入口點設定合理

### **工作流程示意圖**

```
                START (entry_point)
                  ↓
        [resume_parser_node]
                  ↓
            [router_node] ━━━━━━━━━┓
                  ↓                 ↓
        [job_matcher_node]    (條件判斷)
                  ↓                 ↓
      [recommendation_node]   [conversation_node]
                  ↓                 ↓
            [router_node] ←━━━━━━━━┛
                  ↓
         [finalizer_node]
                  ↓
                 END
```

### **預估時間**: ~3 分鐘

---

## 💻 Phase 3: 程式實現 (@CODER)

### **目標**
實現完整的 LangGraph 工作流程與測試案例

### **執行步驟**

#### **步驟1: 實現 workflow.py**

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
    
    # 4. 定義條件 Edges (router 的條件路由)
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

# 建立全局實例（可選）
graph_app = create_workflow()
```

#### **步驟2: 實現 __init__.py**

```
# src/graph/__init__.py
"""Graph 模組 - LangGraph 工作流程"""

from .workflow import create_workflow, graph_app

__all__ = ["create_workflow", "graph_app"]
```

#### **步驟3: 實現測試案例**

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
    
    # 執行並追蹤路由
    result = app.invoke(state)
    
    # 驗證最終狀態
    assert result["system"]["current_node"] in ["finalizer", "conversation"]
```

#### **步驟4: 撰寫設計文檔**

```
# docs/design/graph_design.md

# LangGraph 工作流程設計

## 架構概覽
完整的 AI Agent 工作流程，使用 LangGraph 實現。

## Nodes 清單
1. resume_parser - 履歷解析
2. job_matcher - 職缺匹配
3. skill_analyzer - 技能分析
4. recommendation - 推薦生成
5. conversation - 對話生成
6. router - 條件路由
7. error_handler - 錯誤處理
8. finalizer - 流程結束

## Edges 定義
...（詳細說明）...

## 使用範例
...（使用範例）...
```

### **預估時間**: ~4 分鐘

---

## 🧪 Phase 4: 測試驗證 (@ANALYST)

### **目標**
驗證 Graph 的正確性、完整性與品質

### **驗證任務**

#### **任務1: 執行測試套件**

```
# 執行所有 Graph 測試
pytest tests/graph/ -v --cov=src/graph

# 預期結果: 4+ 測試通過
```

**驗證標準**:
- ✅ 所有測試通過
- ✅ 測試覆蓋率 > 80%

#### **任務2: 端到端測試**

```
# 完整工作流程測試
from src.graph import create_workflow
from src.state.operations import create_initial_state

app = create_workflow()
state = create_initial_state()

# 執行
result = app.invoke(state)

# 驗證
print(f"✅ 履歷解析: {len(result['user_profile']['skills'])} 個技能")
print(f"✅ 職缺匹配: {len(result['job_state']['matched_jobs'])} 個職缺")
print(f"✅ 工作流程: {result['system']['workflow_status']}")
print(f"✅ 完成狀態: {result['is_complete']}")
```

**驗證標準**:
- ✅ 工作流程可以完整執行
- ✅ State 正確傳遞
- ✅ 最終狀態符合預期

#### **任務3: 類型檢查**

```
mypy src/graph/ --strict
```

**驗證標準**:
- ✅ 類型檢查 100% 通過

#### **任務4: Graph 視覺化（可選）**

```
# 視覺化 Graph 結構
from IPython.display import Image, display

app = create_workflow()
display(Image(app.get_graph().draw_mermaid_png()))
```

#### **任務5: 程式碼品質檢查**

**檢查項目**:
- [ ] workflow.py 結構清晰
- [ ] Nodes 加入順序合理
- [ ] Edges 定義完整
- [ ] 條件路由邏輯正確
- [ ] 文檔完整

#### **任務6: 生成測試報告**

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
✅ Edges 定義完整
✅ 條件路由正確
✅ Graph 編譯成功
✅ 端到端測試通過

建議:
- 無重大問題
- 可進入 Phase 6 (測試與優化)

結論:
✅ Phase 5 (Graph 構建) 驗證通過
```

### **預估時間**: ~3 分鐘

---

## 🔄 完整執行流程

```
1. @INFRA 執行
   └─ 輸出: 環境準備完成報告

2. @ARCH 執行  
   └─ 輸出: Graph 架構設計完成

3. @CODER 執行
   └─ 輸出: 程式碼實現完成

4. @ANALYST 執行
   └─ 輸出: 測試驗證報告

5. Phase 5 完成
   └─ 輸出: 完整交付記錄
```

**總時間: 10-12 分鐘**

---

## ⚠️ 重要提醒

```
Phase 5 特點:
✅ 無 Checkpoint（自動執行）
✅ 依賴 Phase 3-4 產出
✅ 產出檔案少但關鍵
✅ 端到端測試為主

與 Phase 4 差異:
- Phase 4: 雙 Checkpoint + 16-20分鐘
- Phase 5: 無 Checkpoint + 10-12分鐘
```

---
