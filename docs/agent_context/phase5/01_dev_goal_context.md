# ✅ **完美！提供第 1 份文件內容**

***

## ✍️ **【第 1 份檔案內容】**

### **檔案：`docs/agent_context/phase5/01_dev_goal_context.md`**

**完整複製以下內容貼入**：

```markdown
# Phase 5 - Graph 構建開發目標

**階段**: Day 1 步驟4 - Graph 構建  
**執行模式**: 自動執行（無 Checkpoint）  
**預估時間**: 10-12 分鐘

---

## 🎯 核心目標

**使用 LangGraph 構建完整的工作流程圖，連接 Phase 4 實現的 8 個 Nodes**

```
Phase 4 產出 (8 Nodes)  →  Phase 5 產出 (完整 Graph)
├─ resume_parser_node      ├─ StateGraph 建立
├─ job_matcher_node        ├─ 8 個 Nodes 加入
├─ skill_analyzer_node     ├─ Edges 定義
├─ recommendation_node     ├─ 條件路由設定
├─ conversation_node       ├─ Graph 編譯
├─ router_node             └─ 完整工作流程測試
├─ error_handler_node
└─ finalizer_node
```

---

## 📊 開發範圍

### **1. 核心任務**

```
✅ 建立 StateGraph
   └─ 使用 AgentState 作為 State Schema

✅ 加入 8 個 Nodes
   ├─ resume_parser_node
   ├─ job_matcher_node
   ├─ skill_analyzer_node
   ├─ recommendation_node
   ├─ conversation_node
   ├─ router_node (條件路由)
   ├─ error_handler_node
   └─ finalizer_node

✅ 定義 Edges (固定連接)
   └─ 明確的前後關係

✅ 定義 Conditional Edges (條件路由)
   └─ router_node 決定下一步

✅ 設定入口與編譯
   └─ set_entry_point() + compile()

✅ 完整測試
   └─ 端到端工作流程驗證
```

### **2. 產出檔案 (4個)**

```
src/graph/
├─ __init__.py           # 導出 Graph
└─ workflow.py           # 核心工作流程 ⭐

tests/graph/
└─ test_workflow.py      # 完整測試

docs/design/
└─ graph_design.md       # 設計文檔
```

---

## 🏗️ LangGraph 架構設計

### **工作流程圖**

```
                    START
                      ↓
              [resume_parser_node]
                      ↓
                [router_node] ────→ 條件判斷
                      ↓
              [job_matcher_node]
                      ↓
           [recommendation_node]
                      ↓
              [conversation_node]
                      ↓
                [router_node] ────→ 條件判斷
                      ↓
               [finalizer_node]
                      ↓
                     END
```

### **條件路由邏輯**

```
# router_node 返回值決定下一步
if not state["user_profile"]["skills"]:
    → "resume_parser"
elif not state["job_state"]["matched_jobs"]:
    → "job_matcher"
elif state["conversation"]["messages"] and not state["is_complete"]:
    → "conversation"
else:
    → "__end__"
```

---

## 📋 詳細目標拆解

### **目標 1: 建立 StateGraph**

```
from langgraph.graph import StateGraph
from src.state.schema import AgentState

# 建立 Graph，指定 State Schema
workflow = StateGraph(AgentState)
```

**驗收標準**:
- ✅ StateGraph 成功建立
- ✅ AgentState 正確綁定

---

### **目標 2: 加入 8 個 Nodes**

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

**驗收標準**:
- ✅ 8 個 Nodes 全部加入
- ✅ Node 名稱與函數正確對應

---

### **目標 3: 定義固定 Edges**

```
# 固定的前後關係
workflow.add_edge("resume_parser", "router")
workflow.add_edge("job_matcher", "recommendation")
workflow.add_edge("recommendation", "router")
workflow.add_edge("conversation", "router")
workflow.add_edge("finalizer", END)
```

**驗收標準**:
- ✅ Edges 定義清晰
- ✅ 邏輯正確

---

### **目標 4: 定義條件路由**

```
from langgraph.graph import END

# 條件路由：router_node 決定下一步
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

**驗收標準**:
- ✅ 條件路由正確設定
- ✅ router_node 返回值對應正確

---

### **目標 5: 設定入口與編譯**

```
# 設定入口點
workflow.set_entry_point("resume_parser")

# 編譯 Graph
app = workflow.compile()
```

**驗收標準**:
- ✅ 入口點正確
- ✅ 編譯無錯誤

---

### **目標 6: 完整測試**

```
from src.state.operations import create_initial_state

# 執行完整工作流程
state = create_initial_state()
result = app.invoke(state)

# 驗證結果
assert result["user_profile"]["skills"]
assert result["job_state"]["matched_jobs"]
assert result["is_complete"] == True
```

**驗收標準**:
- ✅ 工作流程可以完整執行
- ✅ State 正確傳遞
- ✅ 最終狀態符合預期

---

## 🎯 成功標準

```
檔案完整性
├─ src/graph/workflow.py 存在 ✓
├─ src/graph/__init__.py 存在 ✓
├─ tests/graph/test_workflow.py 存在 ✓
└─ docs/design/graph_design.md 存在 ✓

功能完整性
├─ StateGraph 建立成功 ✓
├─ 8 個 Nodes 全部加入 ✓
├─ Edges 定義完整 ✓
├─ 條件路由正確 ✓
├─ Graph 編譯成功 ✓
└─ 端到端測試通過 ✓

程式碼品質
├─ 類型檢查通過 ✓
├─ 測試覆蓋率 >80% ✓
├─ 文檔完整 ✓
└─ 程式碼可讀性 A ✓
```

---

## 🚀 Phase 5 vs Phase 4 對比

| 項目 | Phase 4 (Nodes) | Phase 5 (Graph) |
|------|----------------|-----------------|
| 核心產出 | 8 個 Nodes | 1 個完整 Graph |
| 檔案數 | 9 個 | 4 個 |
| 執行模式 | 雙 Checkpoint | 自動執行 |
| 關鍵技術 | Node 實現 | LangGraph API |
| 測試重點 | 單元測試 | 端到端測試 |
| 預估時間 | 16-20 分鐘 | 10-12 分鐘 |

---

## 📊 Phase 5 在整體流程中的位置

```
Day 1 完整流程:
├─ Phase 2: Mock 數據準備 ✅
├─ Phase 3: State Schema 定義 ✅
├─ Phase 4: Nodes 實現 ✅
├─ Phase 5: Graph 構建 ⏳ ← 目前位置
├─ Phase 6: 測試與優化
└─ Phase 7: 文檔整理

Phase 5 是連接 Nodes 與可執行系統的關鍵橋樑！
```

---

## 🎯 Phase 5 核心價值

```
Phase 4 產出: 8 個獨立的 Nodes（功能單元）
            ↓
Phase 5 任務: 使用 LangGraph 將它們連接起來
            ↓
Phase 5 產出: 完整可執行的工作流程系統

從「零件」到「整車」的關鍵一步！🚗
```

---
