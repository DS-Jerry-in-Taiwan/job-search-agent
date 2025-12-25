✅ **完美！提供第 1 份文件內容**

***

## ✍️ **【第 1 份檔案內容】**

### **檔案：`docs/agent_context/phase4/01_dev_goal_context.md`**

**完整複製以下內容貼入**：

```markdown
# Phase 4 - Nodes 定義開發目標

**階段**: Day 1 步驟3 - Nodes 定義  
**重要性**: ⭐⭐⭐⭐⭐ **LangGraph 工作流程核心！**  
**預估時間**: 16-20 分鐘

---

## 🎯 開發目標

**實現 8 個核心 Nodes，形成完整的職涯搜尋工作流程**：

```
用戶輸入 → 履歷解析 → 職缺匹配 → 技能分析 → 推薦生成[1]
          ↓
     對話生成 ← 路由器 → 錯誤處理 → 工作流程結束[2][3]
```

---

## 🏗️ 8 個核心 Nodes 規格

| # | Node 名稱 | 輸入 State | 輸出 State | 功能描述 |
|---|-----------|------------|------------|----------|
| 1 | `resume_parser_node` | `AgentState` | `UserProfileState` | PDF履歷→結構化資料 |
| 2 | `job_matcher_node` | `UserProfileState + JobState` | `JobState` | 履歷與職缺匹配 |
| 3 | `skill_analyzer_node` | `UserProfileState` | `UserProfileState.skills` | 提取技能清單 |
| 4 | `recommendation_node` | `JobState` | `JobState.recommendations` | 生成推薦理由 |
| 5 | `conversation_node` | `ConversationState` | `ConversationState.messages` | 生成對話回應 |
| 6 | `router_node` | `AgentState` | `AgentState.next_action` | 決定下一步節點 |
| 7 | `error_handler_node` | `SystemState` | `SystemState.error_message` | 錯誤處理與重試 |
| 8 | `finalizer_node` | `AgentState` | `AgentState.is_complete=True` | 工作流程結束 |

---

## 📊 技術規格

### **輸入/輸出規範**
- **輸入**: `AgentState` (從 Phase 3 繼承)
- **輸出**: 修改後的 `AgentState`
- **函數簽名**: `def node(state: AgentState) -> AgentState`
- **框架**: LangGraph Node 規範

### **依賴關係**
```
Phase 3 State Schema ✅ → Phase 4 Nodes → Phase 5 Graph
                     ↑
                data/mock/jobs/ ✅
```

### **品質標準**
```
✅ 8個Nodes 100%實現
✅ 單元測試覆蓋率 >90%
✅ 類型檢查 100%通過
✅ 錯誤處理完整
✅ 文檔完整度 100%
✅ 程式碼品質 A級
```

---

## 📁 產出物清單 (9個檔案)

```
核心程式碼 (6/6)
├── src/nodes/__init__.py
├── src/nodes/resume_parser.py
├── src/nodes/job_matcher.py  
├── src/nodes/conversation.py
├── src/nodes/router.py
└── src/nodes/utils.py

測試檔案 (2/2)
├── tests/nodes/test_resume_parser.py
└── tests/nodes/test_job_matcher.py

文檔 (1/1)
└── docs/design/nodes_design.md
```

---

## 🎪 4 Agent 協作模式

```
@INFRA → @ARCH → @CODER → @ANALYST
  ↓       ↓       ↓         ↓
環境    Nodes    程式碼     測試
準備    設計    實現      驗證
~2分    ~4分    ~6分     ~4分
       ⏸️CP1             ⏸️CP2
```

---

## 🚀 成功標準

```
✅ 8個核心Nodes完整實現
✅ 工作流程邏輯正確
✅ 測試100%通過
✅ 可以串連Phase 3 State
✅ 準備進入Phase 5 Graph

**Phase 4完成 = LangGraph工作流程50%完成！**
```

**這是整個專案的執行核心！品質決定一切！** 🔥
```
