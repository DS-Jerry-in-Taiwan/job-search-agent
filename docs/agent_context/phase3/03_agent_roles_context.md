✅ **太好了！繼續第 3 份文件**

***

## ✍️ 【第 3 份檔案內容】

### **檔案：03_agent_roles_context.md**

以下是完整內容，請複製貼入：

```markdown
# Phase 3 - Agent 角色與職責

**階段**: Day 1 步驟2 - State Schema Design  
**團隊模式**: 4 Agent 協作（架構師主導）

---

## 🎪 Agent 團隊總覽

在 State 定義階段，4 個 Agent 的角色如下：

| Agent | 角色 | 核心職責 | 產出物 |
|-------|------|---------|--------|
| **@INFRA** | 環境工程師 | 建立目錄與基礎檔案 | 目錄結構 |
| **@ARCH** | 架構設計師 | 設計 State Schema | schema.py 設計 |
| **@CODER** | 程式實現工程師 | 實現程式碼與測試 | 完整程式碼 |
| **@ANALYST** | 品質分析師 | 驗證與測試 | 測試報告 |

---

## 🔧 @INFRA - 環境工程師

### **角色定位**
負責建立 State 定義所需的基礎環境，確保目錄結構正確、檔案就位。

### **核心職責**

1. **建立目錄結構**
   ```
   src/state/          # State 定義目錄
   tests/state/        # State 測試目錄
   docs/design/        # 設計文檔目錄
   ```

2. **建立基礎檔案**
   - `src/state/__init__.py`
   - `src/state/schema.py`
   - `src/state/operations.py`
   - `tests/state/test_state_schema.py`
   - `docs/design/state_design.md`

3. **驗證環境**
   - Python 環境正常
   - 必要套件已安裝（langgraph, typing-extensions）
   - 可以正常 import

### **輸入**
- Phase 2 產出的 `data/mock/data_schema.json`（參考）
- 專案根目錄路徑

### **輸出**
- ✅ 完整的目錄結構
- ✅ 所有基礎檔案已建立
- ✅ 環境驗證通過

### **驗證標準**
```
# 檢查目錄
ls -la src/state/
ls -la tests/state/

# 檢查 Python 環境
python -c "import typing; print('OK')"
```

### **執行時間**: ~2 分鐘

---

## 🏗️ @ARCH - 架構設計師

### **角色定位**
**Phase 3 的核心 Agent**，負責設計完整的 State Schema 架構，這是整個專案最關鍵的設計階段。

### **核心職責**

#### **1. 設計 UserProfileState**

**設計考量**:
- 需要儲存哪些履歷資訊？
- 如何支援從 PDF 解析的數據？
- 如何預留擴展空間？

**設計產出**:
```
class UserProfileState(TypedDict):
    user_id: str                    # 必要：唯一識別
    resume_text: str                # 必要：原始履歷
    skills: List[str]               # 必要：技能清單
    experience_years: int           # 必要：年資
    education: str                  # 必要：學歷
    preferences: Dict[str, Any]     # 可選：偏好設定
    parsed_at: datetime             # 必要：解析時間
```

#### **2. 設計 JobState**

**設計考量**:
- 如何儲存職缺清單？
- 如何區分全部職缺與匹配職缺？
- 如何儲存匹配度計算結果？

**設計產出**:
```
class JobState(TypedDict):
    jobs: List[Dict[str, Any]]           # 全部職缺
    matched_jobs: List[Dict[str, Any]]   # 匹配的職缺
    match_scores: Dict[str, float]       # 匹配度
    recommendations: List[str]           # 推薦理由
    last_updated: datetime               # 更新時間
```

#### **3. 設計 ConversationState**

**設計考量**:
- 如何支援多輪對話？
- 如何儲存對話歷史？
- 如何追蹤當前意圖？

**設計產出**:
```
from langchain_core.messages import BaseMessage

class ConversationState(TypedDict):
    messages: List[BaseMessage]     # 對話訊息
    current_intent: str             # 當前意圖
    context: Dict[str, Any]         # 上下文
    history_summary: str            # 歷史摘要
    turn_count: int                 # 對話輪次
```

#### **4. 設計 SystemState**

**設計考量**:
- 如何追蹤執行流程？
- 如何處理錯誤？
- 如何避免無限循環？

**設計產出**:
```
class SystemState(TypedDict):
    current_node: str                   # 當前節點
    workflow_status: str                # 流程狀態
    error_message: Optional[str]        # 錯誤訊息
    retry_count: int                    # 重試次數
    metadata: Dict[str, Any]            # 元數據
```

#### **5. 設計整合 AgentState**

**設計考量**:
- 如何整合 4 大 State？
- 如何定義共用欄位？
- 如何符合 LangGraph 規範？

**設計產出**:
```
class AgentState(TypedDict):
    user_profile: UserProfileState
    job_state: JobState
    conversation: ConversationState
    system: SystemState
    next_action: str                # 下一步動作
    is_complete: bool               # 是否完成
```

### **設計原則**

1. **單一職責原則**
   - 每個 State 只負責一個領域
   - 避免跨領域欄位

2. **開放封閉原則**
   - 使用 Dict[str, Any] 預留擴展
   - 必要欄位明確定義

3. **類型安全**
   - 所有欄位都有類型註解
   - 使用 Optional 標註可選欄位

4. **符合規範**
   - 遵循 LangGraph 規範
   - 使用 TypedDict

### **輸入**
- Phase 2 的 `data_schema.json`（職缺數據結構參考）
- @INFRA 建立的檔案結構
- LangGraph State Management 文檔

### **輸出**
- ✅ 完整的 State Schema 設計
- ✅ 所有欄位定義清晰
- ✅ 設計文檔草稿

### **⏸️ Checkpoint 1 準備**
@ARCH 完成設計後，需要人工確認：
- Schema 設計是否完整？
- 欄位定義是否合理？
- 是否預留擴展空間？
- 是否符合 LangGraph 規範？

### **執行時間**: ~3 分鐘

---

## 💻 @CODER - 程式實現工程師

### **角色定位**
將 @ARCH 的設計轉化為可執行的程式碼，實現 State Schema 與操作函數。

### **核心職責**

#### **1. 實現 schema.py**

**任務**:
- 將 @ARCH 的設計轉為完整程式碼
- 加入完整的類型註解
- 加入 docstring 註解

**實現範例**:
```
from typing import TypedDict, List, Dict, Any, Optional
from datetime import datetime
from langchain_core.messages import BaseMessage

class UserProfileState(TypedDict):
    """用戶履歷狀態
    
    儲存用戶的履歷資訊、技能清單與偏好設定。
    用於匹配職缺時提供用戶背景資訊。
    
    Attributes:
        user_id: 用戶唯一識別碼
        resume_text: 履歷原始文本（從 PDF 解析）
        skills: 技能清單（如 ["Python", "AI", "LangChain"]）
        experience_years: 工作年資
        education: 學歷（如 "Bachelor's Degree"）
        preferences: 偏好設定（如薪資範圍、工作地點）
        parsed_at: 履歷解析時間
    """
    user_id: str
    resume_text: str
    skills: List[str]
    experience_years: int
    education: str
    preferences: Dict[str, Any]
    parsed_at: datetime

# ... 其他 State 定義
```

#### **2. 實現 operations.py**

**任務**:
- 實現 State 初始化函數
- 實現 State 更新函數
- 實現 State 驗證函數

**實現範例**:
```
from typing import Dict, Any
from .schema import AgentState, UserProfileState
from datetime import datetime

def create_initial_state() -> AgentState:
    """建立初始 Agent State
    
    Returns:
        完整的初始 AgentState，所有欄位都有預設值
    """
    return {
        "user_profile": create_empty_user_profile(),
        "job_state": create_empty_job_state(),
        "conversation": create_empty_conversation_state(),
        "system": create_initial_system_state(),
        "next_action": "start",
        "is_complete": False
    }

def update_user_profile(
    state: AgentState, 
    updates: Dict[str, Any]
) -> AgentState:
    """更新 UserProfile State
    
    Args:
        state: 當前 AgentState
        updates: 要更新的欄位
        
    Returns:
        更新後的 AgentState
    """
    updated_profile = {**state["user_profile"], **updates}
    return {**state, "user_profile": updated_profile}

# ... 更多操作函數
```

#### **3. 實現測試案例**

**任務**:
- 測試 State 初始化
- 測試 State 更新
- 測試類型檢查
- 測試邊界條件

**實現範例**:
```
import pytest
from src.state.schema import AgentState
from src.state.operations import create_initial_state, update_user_profile

def test_create_initial_state():
    """測試初始化 State"""
    state = create_initial_state()
    assert state["is_complete"] == False
    assert state["next_action"] == "start"
    assert isinstance(state["user_profile"], dict)

def test_update_user_profile():
    """測試更新 UserProfile"""
    state = create_initial_state()
    updated = update_user_profile(state, {
        "user_id": "test_user_123",
        "skills": ["Python", "AI"]
    })
    assert updated["user_profile"]["user_id"] == "test_user_123"
    assert "Python" in updated["user_profile"]["skills"]

# ... 更多測試
```

#### **4. 撰寫設計文檔**

**任務**:
- 說明 State Schema 設計
- 提供使用範例
- 記錄設計決策

### **輸入**
- @ARCH 的 State Schema 設計
- Checkpoint 1 通過確認

### **輸出**
- ✅ `src/state/schema.py`（完整實現）
- ✅ `src/state/operations.py`（完整實現）
- ✅ `tests/state/test_state_schema.py`（5+ 測試）
- ✅ `docs/design/state_design.md`（設計文檔）

### **驗證標準**
```
# 程式碼可以正常 import
python -c "from src.state.schema import AgentState; print('OK')"

# 測試可以收集（不一定全部通過）
pytest tests/state/ --collect-only
```

### **執行時間**: ~5 分鐘

---

## 🧪 @ANALYST - 品質分析師

### **角色定位**
驗證 State Schema 的正確性、完整性與品質，確保符合所有驗收標準。

### **核心職責**

#### **1. 執行測試套件**

**任務**:
- 執行所有測試案例
- 確認測試 100% 通過
- 檢查測試覆蓋率

**執行指令**:
```
pytest tests/state/test_state_schema.py -v --cov=src/state
```

**驗證標準**:
- ✅ 所有測試通過
- ✅ 測試覆蓋率 > 90%

#### **2. 類型檢查**

**任務**:
- 執行 mypy 類型檢查
- 確認所有類型註解正確
- 確認沒有類型錯誤

**執行指令**:
```
mypy src/state/schema.py --strict
mypy src/state/operations.py --strict
```

**驗證標準**:
- ✅ 類型檢查 100% 通過
- ✅ 沒有 Any 類型警告（除非必要）

#### **3. 程式碼品質檢查**

**檢查項目**:
- [ ] 命名一致性（snake_case）
- [ ] 註解完整性（所有欄位都有註解）
- [ ] 程式碼可讀性
- [ ] 無冗餘程式碼

#### **4. 文檔檢查**

**檢查項目**:
- [ ] 所有 State 都有說明
- [ ] 所有欄位都有註解
- [ ] 提供使用範例
- [ ] 設計原則清楚

#### **5. 生成測試報告**

**報告內容**:
```
State Schema 測試報告
==================

測試結果: ✅ PASSED (5/5)
類型檢查: ✅ PASSED
測試覆蓋率: 95%
程式碼品質: A

詳細結果:
- test_create_initial_state: PASSED
- test_update_user_profile: PASSED
- test_job_state_operations: PASSED
- test_conversation_state: PASSED
- test_system_state: PASSED

建議:
- 無重大問題
- 可進入下一階段
```

### **輸入**
- @CODER 的完整程式碼
- Phase 3 的驗證清單（05_validation_checklist.md）

### **輸出**
- ✅ 測試報告
- ✅ 品質評估
- ✅ 交付確認

### **⏸️ Checkpoint 2 準備**
@ANALYST 完成驗證後，需要人工確認：
- 測試是否 100% 通過？
- 類型檢查是否通過？
- 文檔是否完整？
- 品質是否達標？

### **執行時間**: ~3 分鐘

---

## 🔄 Agent 協作流程

```
@INFRA (環境準備)
    ↓
    建立目錄與檔案
    ↓
@ARCH (架構設計) ⭐ 核心角色
    ↓
    設計 State Schema
    ↓
    ⏸️ Checkpoint 1 (人工確認)
    ↓
@CODER (程式實現)
    ↓
    實現程式碼與測試
    ↓
@ANALYST (測試驗證)
    ↓
    執行測試與品質檢查
    ↓
    ⏸️ Checkpoint 2 (人工確認)
    ↓
    ✅ Phase 3 完成
```

---

## 🎯 團隊協作原則

1. **明確交接**
   - 每個 Agent 完成後明確輸出產物
   - 下一個 Agent 明確確認輸入

2. **品質優先**
   - 不追求速度，追求品質
   - State 定義錯誤的修正成本極高

3. **人工確認**
   - Checkpoint 1 和 2 必須人工確認
   - 不可自動通過

4. **文檔同步**
   - 程式碼與文檔同步更新
   - 不留技術債

---

**在 State 定義階段，@ARCH 是最關鍵的角色！** 🏗️
```
