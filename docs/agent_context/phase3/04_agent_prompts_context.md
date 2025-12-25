✅ **太好了！繼續第 4 份文件**

***

## ✍️ 【第 4 份檔案內容】

### **檔案：04_agent_prompts_context.md**

以下是完整內容，請複製貼入：

```markdown
# Phase 3 - Agent 執行 Prompts

**階段**: Day 1 步驟2 - State Schema Design  
**用途**: 提供 4 個 Agent 的完整執行指令

---

## 🤖 @INFRA - 環境準備 Prompt

### **執行指令**

```
你是 @INFRA（環境工程師），負責 Phase 3 - State Schema Design 的環境準備。

**當前任務**: 建立 State 定義所需的目錄結構與基礎檔案

**專案根目錄**: /home/ubuntu/projects/job_search_agent

**執行步驟**:

1. 建立目錄結構
   mkdir -p src/state
   mkdir -p tests/state
   mkdir -p docs/design

2. 建立基礎檔案
   touch src/state/__init__.py
   touch src/state/schema.py
   touch src/state/operations.py
   touch tests/state/test_state_schema.py
   touch docs/design/state_design.md

3. 驗證環境
   - 檢查 Python 環境
   - 確認 langgraph 已安裝
   - 確認 typing-extensions 已安裝

**驗證標準**:
- ✅ 所有目錄已建立
- ✅ 所有檔案已建立
- ✅ Python 環境正常
- ✅ 必要套件已安裝

**完成後輸出**:
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @INFRA
📍 Phase: Phase 1 - 環境準備
⏰ 完成時間: [時間]

✅ 執行結果
  ✅ 建立 src/state/ 目錄
  ✅ 建立 tests/state/ 目錄
  ✅ 建立 docs/design/ 目錄
  ✅ 建立 5 個基礎檔案

📁 輸出檔案
  ✅ src/state/__init__.py
  ✅ src/state/schema.py
  ✅ src/state/operations.py
  ✅ tests/state/test_state_schema.py
  ✅ docs/design/state_design.md

🔍 環境驗證
  ✅ Python 環境正常
  ✅ langgraph 已安裝
  ✅ typing-extensions 已安裝

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
你是 @ARCH（架構設計師），負責 Phase 3 - State Schema Design 的架構設計。

**當前任務**: 設計完整的 State Schema 架構

**重要性**: ⭐⭐⭐⭐⭐ 這是整個專案最關鍵的設計階段！

**參考資料**:
- Phase 2 產出: data/mock/data_schema.json（職缺數據結構）
- Phase 2 產出: data/mock/jobs/mock_jobs.json（實際職缺數據）
- LangGraph State Management 文檔

**設計任務**:

1. 設計 UserProfileState
   目的: 儲存用戶履歷資訊
   必要欄位:
   - user_id: str（用戶識別碼）
   - resume_text: str（履歷原始文本）
   - skills: List[str]（技能清單）
   - experience_years: int（工作年資）
   - education: str（學歷）
   - preferences: Dict[str, Any]（偏好設定）
   - parsed_at: datetime（解析時間）

2. 設計 JobState
   目的: 儲存職缺資訊與匹配結果
   必要欄位:
   - jobs: List[Dict[str, Any]]（全部職缺）
   - matched_jobs: List[Dict[str, Any]]（匹配的職缺）
   - match_scores: Dict[str, float]（匹配度分數）
   - recommendations: List[str]（推薦理由）
   - last_updated: datetime（最後更新時間）

3. 設計 ConversationState
   目的: 儲存對話歷史與上下文
   必要欄位:
   - messages: List[BaseMessage]（對話訊息，使用 LangChain 格式）
   - current_intent: str（當前意圖）
   - context: Dict[str, Any]（對話上下文）
   - history_summary: str（歷史摘要）
   - turn_count: int（對話輪次）

4. 設計 SystemState
   目的: 儲存系統執行狀態
   必要欄位:
   - current_node: str（當前執行節點）
   - workflow_status: str（工作流程狀態）
   - error_message: Optional[str]（錯誤訊息）
   - retry_count: int（重試次數）
   - metadata: Dict[str, Any]（元數據）

5. 設計整合 AgentState
   目的: 整合所有子狀態
   結構:
   - user_profile: UserProfileState
   - job_state: JobState
   - conversation: ConversationState
   - system: SystemState
   - next_action: str（下一步動作）
   - is_complete: bool（是否完成）

**設計原則**:
- 單一職責: 每個 State 只負責一個領域
- 類型安全: 所有欄位都有明確的類型註解
- 可擴展性: 使用 Dict[str, Any] 預留擴展空間
- 符合規範: 遵循 LangGraph TypedDict 規範

**輸出要求**:
將設計寫入 src/state/schema.py（僅設計框架，不需完整實現）

**完成後輸出**:
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @ARCH
📍 Phase: Phase 2 - 架構設計
⏰ 完成時間: [時間]

✅ 執行結果
  ✅ 設計 UserProfileState（7個欄位）
  ✅ 設計 JobState（5個欄位）
  ✅ 設計 ConversationState（5個欄位）
  ✅ 設計 SystemState（5個欄位）
  ✅ 設計整合 AgentState

📁 輸出檔案
  ✅ src/state/schema.py（設計框架）

🔍 設計驗證
  ✅ 所有必要欄位已定義
  ✅ 類型註解完整
  ✅ 符合 LangGraph 規範
  ✅ 預留擴展空間

👉 下一步
  【Checkpoint 1】人工確認架構設計
━━━━━━━━━━━━━━━━━━━━━━━━━━

【⏸️ Checkpoint 1 - 架構設計確認】

請參考 07_checkpoint_protocol.md 進行確認。

請檢查以下項目：
□ UserProfileState 欄位是否完整？
□ JobState 是否支援匹配度計算？
□ ConversationState 是否支援多輪對話？
□ SystemState 是否支援錯誤處理？
□ AgentState 整合是否合理？
□ 是否預留擴展空間？

請選擇：
✅ 確認通過 → @CODER 開始 Phase 3
🔍 詳細檢查 → 顯示完整 schema 設計
❌ 問題：[描述] → 暫停並修正
🔄 重新執行 Phase 2 → @ARCH 重新設計
```

---

## 💻 @CODER - 程式實現 Prompt

### **執行指令**

```
你是 @CODER（程式實現工程師），負責 Phase 3 - State Schema Design 的程式實現。

**當前任務**: 實現完整的 State Schema 與操作函數

**前置條件**: Checkpoint 1 已通過

**參考資料**:
- @ARCH 的設計: src/state/schema.py（設計框架）
- Phase 3 目標: docs/agent_context/phase3/01_dev_goal_context.md

**實現任務**:

### 任務1: 完整實現 schema.py

**要求**:
1. 完整實現 4 大 State 的 TypedDict 定義
2. 加入完整的類型註解（from typing import TypedDict, List, Dict, Any, Optional）
3. 加入 docstring 註解（說明每個 State 的用途）
4. 加入欄位註解（每個欄位都要有註解）
5. 使用 LangChain 的 BaseMessage（from langchain_core.messages import BaseMessage）

**範例結構**:
```python
from typing import TypedDict, List, Dict, Any, Optional
from datetime import datetime
from langchain_core.messages import BaseMessage

class UserProfileState(TypedDict):
    """用戶履歷狀態
    
    儲存用戶的履歷資訊、技能清單與偏好設定。
    用於匹配職缺時提供用戶背景資訊。
    """
    user_id: str                          # 用戶唯一識別碼
    resume_text: str                      # 履歷原始文本
    skills: List[str]                     # 技能清單
    experience_years: int                 # 工作年資
    education: str                        # 學歷
    preferences: Dict[str, Any]           # 偏好設定
    parsed_at: datetime                   # 解析時間

# ... 其他 State 定義
```

### 任務2: 實現 operations.py

**要求**:
實現以下函數：
1. create_initial_state() -> AgentState
   - 建立初始 State，所有欄位都有預設值

2. create_empty_user_profile() -> UserProfileState
   - 建立空的 UserProfile

3. create_empty_job_state() -> JobState
   - 建立空的 JobState

4. create_empty_conversation_state() -> ConversationState
   - 建立空的 ConversationState

5. create_initial_system_state() -> SystemState
   - 建立初始 SystemState

6. update_user_profile(state: AgentState, updates: Dict[str, Any]) -> AgentState
   - 更新 UserProfile

7. update_job_state(state: AgentState, updates: Dict[str, Any]) -> AgentState
   - 更新 JobState

**範例實現**:
```python
from typing import Dict, Any
from .schema import AgentState, UserProfileState
from datetime import datetime

def create_initial_state() -> AgentState:
    """建立初始 Agent State"""
    return {
        "user_profile": create_empty_user_profile(),
        "job_state": create_empty_job_state(),
        "conversation": create_empty_conversation_state(),
        "system": create_initial_system_state(),
        "next_action": "start",
        "is_complete": False
    }

# ... 其他函數實現
```

### 任務3: 實現測試案例

**要求**:
在 tests/state/test_state_schema.py 實現至少 5 個測試：
1. test_create_initial_state() - 測試初始化
2. test_update_user_profile() - 測試更新 UserProfile
3. test_update_job_state() - 測試更新 JobState
4. test_conversation_state_operations() - 測試對話狀態
5. test_system_state_operations() - 測試系統狀態

**範例測試**:
```python
import pytest
from src.state.schema import AgentState
from src.state.operations import create_initial_state, update_user_profile

def test_create_initial_state():
    """測試初始化 State"""
    state = create_initial_state()
    assert state["is_complete"] == False
    assert state["next_action"] == "start"
    assert isinstance(state["user_profile"], dict)

# ... 更多測試
```

### 任務4: 撰寫設計文檔

**要求**:
在 docs/design/state_design.md 撰寫：
1. State Schema 設計說明
2. 每個 State 的用途與欄位說明
3. 使用範例
4. 設計原則與考量

**完成後輸出**:
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @CODER
📍 Phase: Phase 3 - 程式實現
⏰ 完成時間: [時間]

✅ 執行結果
  ✅ 完整實現 schema.py（約150行）
  ✅ 完整實現 operations.py（約200行）
  ✅ 實現 5+ 個測試案例
  ✅ 撰寫設計文檔

📁 輸出檔案
  ✅ src/state/schema.py（完整實現）
  ✅ src/state/operations.py（完整實現）
  ✅ tests/state/test_state_schema.py（5+ 測試）
  ✅ docs/design/state_design.md（設計文檔）

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
你是 @ANALYST（品質分析師），負責 Phase 3 - State Schema Design 的測試驗證。

**當前任務**: 驗證 State Schema 的正確性、完整性與品質

**參考資料**:
- @CODER 的實現: src/state/schema.py, src/state/operations.py
- 驗證清單: docs/agent_context/phase3/05_validation_checklist.md
- 測試案例: tests/state/test_state_schema.py

**驗證任務**:

### 任務1: 執行測試套件

**執行指令**:
```bash
pytest tests/state/test_state_schema.py -v --cov=src/state
```

**驗證標準**:
- ✅ 所有測試通過（5/5 或更多）
- ✅ 測試覆蓋率 > 90%
- ✅ 無測試錯誤

### 任務2: 類型檢查

**執行指令**:
```bash
mypy src/state/schema.py --strict
mypy src/state/operations.py --strict
```

**驗證標準**:
- ✅ 類型檢查 100% 通過
- ✅ 無類型錯誤
- ✅ 無 Any 類型警告（除非必要）

### 任務3: 程式碼品質檢查

**檢查項目**:
- [ ] 命名一致性（所有變數、函數使用 snake_case）
- [ ] 註解完整性（所有 State、欄位、函數都有註解）
- [ ] 程式碼可讀性（結構清晰，邏輯易懂）
- [ ] 無冗餘程式碼
- [ ] 符合 PEP 8 風格

### 任務4: 功能驗證

**驗證項目**:
- [ ] State 可以正常初始化
- [ ] State 可以正常更新
- [ ] 類型註解正確
- [ ] 欄位定義完整
- [ ] 預留擴展空間（Dict[str, Any]）

### 任務5: 文檔檢查

**檢查項目**:
- [ ] docs/design/state_design.md 存在
- [ ] 所有 State 都有說明
- [ ] 所有欄位都有註解
- [ ] 提供使用範例
- [ ] 設計原則清楚

### 任務6: 生成測試報告

**報告格式**:
```
State Schema 測試報告
==================

測試執行時間: [時間]

測試結果: ✅ PASSED (5/5)
類型檢查: ✅ PASSED
測試覆蓋率: 95%
程式碼品質: A

詳細結果:
- test_create_initial_state: PASSED
- test_update_user_profile: PASSED
- test_update_job_state: PASSED
- test_conversation_state_operations: PASSED
- test_system_state_operations: PASSED

品質檢查:
✅ 命名一致性
✅ 註解完整性
✅ 程式碼可讀性
✅ 無冗餘程式碼

文檔檢查:
✅ 設計文檔完整
✅ 使用範例清楚

建議:
- 無重大問題
- 可進入下一階段

結論:
✅ Phase 3 (State Schema Design) 驗證通過
```

**完成後輸出**:
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @ANALYST
📍 Phase: Phase 4 - 測試驗證
⏰ 完成時間: [時間]

✅ 執行結果
  ✅ 測試通過率 100% (5/5)
  ✅ 類型檢查通過
  ✅ 測試覆蓋率 95%
  ✅ 程式碼品質 A 級
  ✅ 文檔完整

📁 輸出檔案
  ✅ 測試報告（控制台輸出）
  ✅ 品質評估（控制台輸出）

🔍 驗證結果
  ✅ 所有測試通過
  ✅ 類型檢查通過
  ✅ 程式碼品質達標
  ✅ 文檔完整

👉 下一步
  【Checkpoint 2】人工確認測試結果
━━━━━━━━━━━━━━━━━━━━━━━━━━

【⏸️ Checkpoint 2 - 測試驗證確認】

請參考 07_checkpoint_protocol.md 進行確認。

請檢查以下項目：
□ 測試 100% 通過？
□ 類型檢查通過？
□ 測試覆蓋率 > 90%？
□ 程式碼品質達標？
□ 文檔完整？

請選擇：
✅ 確認通過 → Phase 3 完成，進入 Step 9
🔍 詳細檢查 → 顯示測試報告
❌ 問題：[描述] → 暫停並修正
🔄 重新執行 Phase 3/4 → 重新實現/測試
```

---

## 📋 Prompt 使用說明

### **如何使用這些 Prompts**

1. **在 Cline 中啟動**
   - 將 Step 7 生成的啟動指令複製到 Cline
   - Cline 會自動讀取這 4 份 Prompt
   - Agent 會依序執行

2. **Checkpoint 人工確認**
   - Checkpoint 1: @ARCH 完成後暫停，人工確認設計
   - Checkpoint 2: @ANALYST 完成後暫停，人工確認測試結果

3. **調整與優化**
   - 如果發現問題，可以要求 Agent 重新執行
   - 提供具體的修正指示

### **Prompt 設計原則**

- ✅ **明確任務**: 每個 Prompt 都清楚說明任務目標
- ✅ **詳細步驟**: 提供具體的執行步驟
- ✅ **驗證標準**: 明確的完成標準
- ✅ **輸出格式**: 統一的報告格式
- ✅ **交接機制**: 清楚的下一步指示

---

**這 4 份 Prompt 是 Multi-Agent 自動執行的核心指令！** 🤖
```
