✅ **完美！提供第 3 份文件內容**

***

## ✍️ **【第 3 份檔案內容】**

### **檔案：`docs/agent_context/phase4/03_agent_roles_context.md`**

**完整複製以下內容貼入**：

```markdown
# Phase 4 - Agent 角色與職責

**階段**: Day 1 步驟3 - Nodes 定義  
**團隊模式**: 4 Agent 協作（架構師主導）

---

## 🎪 Agent 團隊總覽

在 Nodes 定義階段，4 個 Agent 的角色如下：

| Agent | 角色 | 核心職責 | 產出物 |
|-------|------|---------|--------|
| **@INFRA** | 環境工程師 | 建立目錄與基礎檔案 | 目錄結構 + 9檔案 |
| **@ARCH** | 架構設計師 | 設計8個Nodes架構 | Nodes設計規格 |
| **@CODER** | 程式實現工程師 | 實現8個Nodes | 完整程式碼 |
| **@ANALYST** | 品質分析師 | 驗證與測試 | 測試報告 |

---

## 🔧 @INFRA - 環境工程師

### **角色定位**
負責建立 Nodes 定義所需的基礎環境，確保目錄結構正確、檔案就位。

### **核心職責**

1. **建立目錄結構**
   ```
   src/nodes/          # Nodes 實現目錄
   tests/nodes/        # Nodes 測試目錄
   ```

2. **建立基礎檔案 (9個)**
   ```
   src/nodes/__init__.py
   src/nodes/resume_parser.py
   src/nodes/job_matcher.py
   src/nodes/conversation.py
   src/nodes/router.py
   src/nodes/utils.py
   tests/nodes/test_resume_parser.py
   tests/nodes/test_job_matcher.py
   docs/design/nodes_design.md
   ```

3. **驗證 Phase 3 依賴**
   - Phase 3 State Schema 可用
   - `from src.state.schema import AgentState` 正常
   - Phase 2 Mock 數據存在 (`data/mock/jobs/mock_jobs.json`)

### **輸入**
- Phase 3 產出：`src/state/schema.py`, `src/state/operations.py`
- Phase 2 產出：`data/mock/jobs/mock_jobs.json`
- 專案根目錄路徑

### **輸出**
- ✅ 完整的目錄結構
- ✅ 9 個基礎檔案已建立
- ✅ 環境驗證通過

### **驗證標準**
```
# 檢查目錄
ls -la src/nodes/
ls -la tests/nodes/

# 檢查 Phase 3 State 可用
python -c "from src.state.schema import AgentState; print('OK')"

# 檢查 Phase 2 數據存在
ls -lh data/mock/jobs/mock_jobs.json
```

### **執行時間**: ~2 分鐘

---

## 🏗️ @ARCH - 架構設計師

### **角色定位**
**Phase 4 的核心 Agent**，負責設計 8 個核心 Nodes 的完整架構，這是 LangGraph 工作流程的執行核心。

### **核心職責**

#### **1. 設計 8 個核心 Nodes**

**業務邏輯 Nodes (4個)**

##### **Node 1: resume_parser_node**
**職責**: 解析 PDF 履歷 → UserProfileState

**設計規格**:
```
def resume_parser_node(state: AgentState) -> AgentState:
    """
    輸入: state["user_profile"]["resume_text"]
    輸出: 更新完整的 UserProfileState
    
    處理流程:
    1. 讀取 PDF 檔案 (PyPDF2)
    2. 提取技能關鍵字
    3. 提取工作年資
    4. 提取學歷
    5. 更新 parsed_at
    """
```

**關鍵欄位**:
- `skills`: List[str]
- `experience_years`: int
- `education`: str
- `parsed_at`: datetime

---

##### **Node 2: job_matcher_node**
**職責**: 履歷匹配職缺 → JobState

**設計規格**:
```
def job_matcher_node(state: AgentState) -> AgentState:
    """
    輸入: state["user_profile"]["skills"]
    輸出: state["job_state"]["matched_jobs"], ["match_scores"]
    
    處理流程:
    1. 載入 data/mock/jobs/mock_jobs.json
    2. 計算每個職缺的匹配分數
    3. 篩選匹配度 >= 0.3 的職缺
    4. 排序並更新 JobState
    """
```

**匹配邏輯**:
- 技能匹配度 = (用戶技能 ∩ 職缺需求) / 用戶技能數
- 閾值：>= 0.3 才加入 matched_jobs

---

##### **Node 3: skill_analyzer_node**
**職責**: 深度分析技能 → 增強 skills 清單

**設計規格**:
```
def skill_analyzer_node(state: AgentState) -> AgentState:
    """
    輸入: state["user_profile"]["resume_text"]
    輸出: 更新 state["user_profile"]["skills"]
    
    處理流程:
    1. NLP 分析履歷文本
    2. 提取技術關鍵字
    3. 分類技能等級
    """
```

---

##### **Node 4: recommendation_node**
**職責**: 生成推薦理由 → recommendations

**設計規格**:
```
def recommendation_node(state: AgentState) -> AgentState:
    """
    輸入: state["job_state"]["matched_jobs"]
    輸出: state["job_state"]["recommendations"]
    
    處理流程:
    1. 分析前5名匹配職缺
    2. 生成推薦理由
    3. 更新 recommendations
    """
```

---

**工作流程控制 Nodes (4個)**

##### **Node 5: conversation_node**
**職責**: 生成對話回應 → ConversationState.messages

**設計規格**:
```
def conversation_node(state: AgentState) -> AgentState:
    """
    輸入: state["conversation"]["messages"], ["current_intent"]
    輸出: 新增 AIMessage 到 messages
    
    處理流程:
    1. 分析用戶最後訊息
    2. 根據 intent 生成回應
    3. 新增到 messages
    """
```

**支援 Intents**:
- `job_search`: 職缺搜尋回應
- `skill_analysis`: 技能分析回應
- `general`: 一般對話回應

---

##### **Node 6: router_node**
**職責**: 工作流程路由器 → 決定下一步

**設計規格**:
```
def router_node(state: AgentState) -> str:
    """
    輸入: state 整體狀態
    輸出: 下一個 node 名稱 (str)
    
    路由邏輯:
    - "resume_parser": 履歷未解析
    - "job_matcher": 履歷已解析但未匹配
    - "conversation": 需要對話回應
    - "__end__": 工作流程結束
    """
```

**關鍵**: 這是 LangGraph 唯一返回 `str` 的 Node！

---

##### **Node 7: error_handler_node**
**職責**: 錯誤處理與重試 → SystemState

**設計規格**:
```
def error_handler_node(state: AgentState) -> AgentState:
    """
    輸入: state["system"]["error_message"]
    輸出: 更新 retry_count, workflow_status
    
    處理流程:
    1. 檢查 error_message
    2. 判斷是否需要重試
    3. 超過3次則標記失敗
    """
```

**重試策略**:
- 最多重試 3 次
- 超過則 `workflow_status = "failed"`

---

##### **Node 8: finalizer_node**
**職責**: 工作流程結束 → is_complete=True

**設計規格**:
```
def finalizer_node(state: AgentState) -> AgentState:
    """
    輸入: state 整體狀態
    輸出: state["is_complete"] = True
    
    處理流程:
    1. 標記完成
    2. 更新 workflow_status
    """
```

---

#### **2. 設計原則**

1. **LangGraph 規範**
   - 所有 Node 函數簽名: `def node(state: AgentState) -> AgentState`
   - 唯一例外: `router_node` 返回 `str`
   - 必須返回修改後的 state

2. **State 整合**
   - 依賴 Phase 3 的 AgentState
   - 正確更新對應的子狀態 (UserProfile, JobState, Conversation, System)
   - 不破壞其他欄位

3. **錯誤處理**
   - 所有 Node 都應該處理可能的異常
   - 更新 `system.error_message`
   - 配合 error_handler_node

4. **可測試性**
   - 每個 Node 都是純函數
   - 容易編寫單元測試
   - Mock 依賴清晰

### **輸入**
- Phase 3 的 State Schema 設計
- Phase 2 的 Mock 數據結構
- @INFRA 建立的檔案結構

### **輸出**
- ✅ 8個Nodes設計規格完整
- ✅ 函數簽名符合LangGraph規範
- ✅ 設計文檔草稿

### **⏸️ Checkpoint 1 準備**
@ARCH 完成設計後，需要人工確認：
- 8個Nodes設計是否完整？
- 函數簽名是否符合LangGraph規範？
- State Schema整合是否正確？
- 工作流程邏輯是否合理？

### **執行時間**: ~4 分鐘

---

## 💻 @CODER - 程式實現工程師

### **角色定位**
將 @ARCH 的設計轉化為可執行的程式碼，實現 8 個 Nodes 與測試案例。

### **核心職責**

#### **1. 實現 6 個核心檔案**

##### **resume_parser.py**
- 實現 `resume_parser_node()`
- 實現 `extract_skills_from_text()` 輔助函數
- 處理 PDF 讀取 (PyPDF2)
- Mock 實現先用假數據

##### **job_matcher.py**
- 實現 `job_matcher_node()`
- 實現 `calculate_match_score()` 輔助函數
- 載入 Mock 數據
- 計算匹配分數邏輯

##### **conversation.py**
- 實現 `conversation_node()`
- 實現 `generate_job_search_response()`
- 實現 `generate_skill_analysis_response()`
- 使用 LangChain BaseMessage

##### **router.py**
- 實現 `router_node()` (返回 str)
- 實現 `error_handler_node()`
- 實現 `finalizer_node()`
- 路由邏輯清晰

##### **utils.py**
- 實現 `skill_analyzer_node()`
- 實現 `recommendation_node()`
- 輔助函數

##### **__init__.py**
- 導出所有 Nodes
- 方便其他模組使用

#### **2. 實現測試案例**

##### **test_resume_parser.py**
```
def test_resume_parser_node():
    """測試履歷解析"""
    
def test_extract_skills():
    """測試技能提取"""
```

##### **test_job_matcher.py**
```
def test_job_matcher_node():
    """測試職缺匹配"""
    
def test_calculate_match_score():
    """測試匹配分數計算"""
```

#### **3. 撰寫設計文檔**
- 說明 8 個 Nodes 的用途
- 提供使用範例
- 記錄設計決策

### **輸入**
- @ARCH 的 Nodes 設計規格
- Checkpoint 1 通過確認

### **輸出**
- ✅ 6 個核心檔案完整實現
- ✅ 2 個測試檔案 (5+ 測試案例)
- ✅ docs/design/nodes_design.md

### **驗證標準**
```
# 程式碼可以正常 import
python -c "from src.nodes.resume_parser import resume_parser_node; print('OK')"

# 測試可以收集
pytest tests/nodes/ --collect-only
```

### **執行時間**: ~6 分鐘

---

## 🧪 @ANALYST - 品質分析師

### **角色定位**
驗證 Nodes 的正確性、完整性與品質，確保符合所有驗收標準。

### **核心職責**

#### **1. 執行測試套件**

**任務**:
- 執行所有測試案例
- 確認測試 100% 通過
- 檢查測試覆蓋率

**執行指令**:
```
pytest tests/nodes/ -v --cov=src/nodes
```

**驗證標準**:
- ✅ 所有測試通過
- ✅ 測試覆蓋率 > 90%

#### **2. 整合測試**

**任務**:
- 測試 Nodes 串連執行
- 驗證 State 正確傳遞
- 確認工作流程邏輯

**執行腳本**:
```
from src.state.operations import create_initial_state
from src.nodes.resume_parser import resume_parser_node
from src.nodes.job_matcher import job_matcher_node

state = create_initial_state()
state = resume_parser_node(state)
state = job_matcher_node(state)

assert state["user_profile"]["skills"]
assert state["job_state"]["matched_jobs"]
print("✅ 整合測試通過")
```

#### **3. 類型檢查**

**執行指令**:
```
mypy src/nodes/ --strict
```

**驗證標準**:
- ✅ 類型檢查 100% 通過
- ✅ 無類型錯誤

#### **4. 程式碼品質檢查**

**檢查項目**:
- [ ] 命名一致性 (snake_case)
- [ ] 函數簽名正確
- [ ] docstring 完整
- [ ] 程式碼可讀性
- [ ] 無冗餘程式碼

#### **5. 文檔檢查**

**檢查項目**:
- [ ] nodes_design.md 存在
- [ ] 所有 Nodes 都有說明
- [ ] 使用範例清楚
- [ ] 設計決策記錄

#### **6. 生成測試報告**

**報告內容**:
```
Nodes 測試報告
==================

測試結果: ✅ PASSED (8/8)
類型檢查: ✅ PASSED
測試覆蓋率: 92%
程式碼品質: A

詳細結果:
- test_resume_parser_node: PASSED
- test_job_matcher_node: PASSED
- test_conversation_node: PASSED
- test_router_node: PASSED
- test_error_handler_node: PASSED
- test_finalizer_node: PASSED
- test_skill_analyzer_node: PASSED
- test_recommendation_node: PASSED

整合測試: ✅ 通過

建議:
- 無重大問題
- 可進入 Phase 5 (Graph 構建)
```

### **輸入**
- @CODER 的完整程式碼
- Phase 4 的驗證清單

### **輸出**
- ✅ 測試報告
- ✅ 品質評估
- ✅ 交付確認

### **⏸️ Checkpoint 2 準備**
@ANALYST 完成驗證後，需要人工確認：
- 測試是否 100% 通過？
- 整合測試是否通過？
- 類型檢查是否通過？
- 文檔是否完整？
- 品質是否達標？

### **執行時間**: ~4 分鐘

---

## 🔄 Agent 協作流程

```
@INFRA (環境準備)
    ↓
    建立目錄與9個檔案
    ↓
@ARCH (Nodes設計) ⭐ 核心角色
    ↓
    設計8個Nodes架構
    ↓
    ⏸️ Checkpoint 1 (人工確認)
    ↓
@CODER (程式實現)
    ↓
    實現8個Nodes與測試
    ↓
@ANALYST (測試驗證)
    ↓
    執行測試與品質檢查
    ↓
    ⏸️ Checkpoint 2 (人工確認)
    ↓
    ✅ Phase 4 完成
```

---

## 🎯 團隊協作原則

1. **明確交接**
   - 每個 Agent 完成後明確輸出產物
   - 下一個 Agent 明確確認輸入

2. **品質優先**
   - Nodes 是工作流程執行核心
   - 設計錯誤修正成本高

3. **人工確認**
   - Checkpoint 1 和 2 必須人工確認
   - 不可自動通過

4. **文檔同步**
   - 程式碼與文檔同步更新
   - 不留技術債

---

**在 Nodes 定義階段，@ARCH 是最關鍵的角色！** 🏗️
```

***
