
## ✍️ 【第 2 份檔案內容】

### **檔案：02_dev_flow_context.md**

以下是完整內容，請複製貼入：

```markdown
# Phase 3 - State 定義開發流程

**階段**: Day 1 步驟2 - State Schema Design  
**執行模式**: 混合模式（Checkpoint 1 和 2）  
**預估時間**: 15-20 分鐘

---

## 🚀 開發流程總覽

```
Phase 1 (INFRA)  → Phase 2 (ARCH)     → Phase 3 (CODER)    → Phase 4 (ANALYST)
環境準備          架構設計             程式實現              測試驗證
~2分鐘            ~3分鐘               ~5分鐘                ~3分鐘
                 [Checkpoint 1] ⏸️                         [Checkpoint 2] ⏸️
```

---

## 📋 Phase 1: 環境準備 (@INFRA)

### **目標**
建立 State Schema 開發所需的目錄結構與基礎檔案

### **執行步驟**

1. **建立目錄結構**
```
mkdir -p src/state
mkdir -p tests/state
mkdir -p docs/design
```

2. **建立基礎檔案**
```
touch src/state/__init__.py
touch src/state/schema.py
touch src/state/operations.py
touch tests/state/test_state_schema.py
touch docs/design/state_design.md
```

3. **安裝必要套件**
```
# 確認已安裝
pip list | grep -E "langgraph|typing-extensions"
```

### **驗證標準**
- ✅ 目錄結構正確
- ✅ 所有檔案已建立
- ✅ Python 環境正常

### **預期輸出**
```
src/state/
├── __init__.py
├── schema.py
└── operations.py

tests/state/
└── test_state_schema.py

docs/design/
└── state_design.md
```

### **預估時間**: ~2 分鐘

---

## 🏗️ Phase 2: 架構設計 (@ARCH)

### **目標**
設計完整的 State Schema 架構，定義所有 TypedDict 結構

### **執行步驟**

#### **步驟1: 設計 UserProfileState**
```
# src/state/schema.py 的初步設計

from typing import TypedDict, List, Dict, Any, Optional
from datetime import datetime

class UserProfileState(TypedDict):
    """用戶履歷狀態"""
    user_id: str
    resume_text: str
    skills: List[str]
    experience_years: int
    education: str
    preferences: Dict[str, Any]
    parsed_at: datetime
```

#### **步驟2: 設計 JobState**
```
class JobState(TypedDict):
    """職缺管理狀態"""
    jobs: List[Dict[str, Any]]
    matched_jobs: List[Dict[str, Any]]
    match_scores: Dict[str, float]
    recommendations: List[str]
    last_updated: datetime
```

#### **步驟3: 設計 ConversationState**
```
from langchain_core.messages import BaseMessage

class ConversationState(TypedDict):
    """對話上下文狀態"""
    messages: List[BaseMessage]
    current_intent: str
    context: Dict[str, Any]
    history_summary: str
    turn_count: int
```

#### **步驟4: 設計 SystemState**
```
class SystemState(TypedDict):
    """系統執行狀態"""
    current_node: str
    workflow_status: str
    error_message: Optional[str]
    retry_count: int
    metadata: Dict[str, Any]
```

#### **步驟5: 設計整合 AgentState**
```
class AgentState(TypedDict):
    """整合的 Agent 狀態"""
    user_profile: UserProfileState
    job_state: JobState
    conversation: ConversationState
    system: SystemState
    next_action: str
    is_complete: bool
```

### **設計原則**

1. **單一職責**
   - 每個 State 只負責一個領域
   - 避免跨領域的欄位混合

2. **可擴展性**
   - 使用 Dict[str, Any] 預留擴展空間
   - 必要欄位與可選欄位明確區分

3. **類型安全**
   - 所有欄位都有明確的類型註解
   - 使用 Optional 標註可選欄位

4. **符合規範**
   - 遵循 LangGraph State 規範
   - 使用 TypedDict 而非普通 dict

### **驗證標準**
- ✅ 4 大 State 定義完整
- ✅ 類型註解清晰
- ✅ 欄位命名一致
- ✅ 符合 LangGraph 規範
- ✅ 預留擴展空間

### **⏸️ Checkpoint 1: 架構設計確認**

**人工確認項目**:
- [ ] UserProfileState 欄位是否完整？
- [ ] JobState 是否支援匹配度計算？
- [ ] ConversationState 是否支援多輪對話？
- [ ] SystemState 是否支援錯誤處理？
- [ ] AgentState 整合是否合理？

**決策選項**:
- ✅ 確認通過 → 進入 Phase 3
- 🔍 詳細檢查 → 展示完整 schema 設計
- ❌ 問題：[描述] → 暫停並修正
- 🔄 重新設計 → @ARCH 重新執行

### **預估時間**: ~3 分鐘

---

## 💻 Phase 3: 程式實現 (@CODER)

### **目標**
實現 State Schema 定義與相關操作函數

### **執行步驟**

#### **步驟1: 實現 schema.py**

**完整實現 4 大 State + AgentState**

```
# src/state/schema.py

from typing import TypedDict, List, Dict, Any, Optional
from datetime import datetime
from langchain_core.messages import BaseMessage

class UserProfileState(TypedDict):
    """用戶履歷狀態
    
    儲存用戶的履歷資訊、技能清單與偏好設定
    """
    user_id: str                          # 用戶唯一識別碼
    resume_text: str                      # 履歷原始文本
    skills: List[str]                     # 技能清單
    experience_years: int                 # 工作年資
    education: str                        # 學歷
    preferences: Dict[str, Any]           # 偏好設定
    parsed_at: datetime                   # 解析時間

# ... (其他 State 定義)

class AgentState(TypedDict):
    """整合的 Agent 狀態
    
    包含所有子狀態，作為 LangGraph 的主要狀態結構
    """
    user_profile: UserProfileState
    job_state: JobState
    conversation: ConversationState
    system: SystemState
    next_action: str
    is_complete: bool
```

#### **步驟2: 實現 operations.py**

**State 初始化與操作函數**

```
# src/state/operations.py

from typing import Dict, Any
from .schema import AgentState, UserProfileState, JobState, ConversationState, SystemState
from datetime import datetime

def create_initial_state() -> AgentState:
    """建立初始 State"""
    return {
        "user_profile": create_empty_user_profile(),
        "job_state": create_empty_job_state(),
        "conversation": create_empty_conversation_state(),
        "system": create_initial_system_state(),
        "next_action": "start",
        "is_complete": False
    }

def create_empty_user_profile() -> UserProfileState:
    """建立空的 UserProfile"""
    # 實現...

def update_user_profile(state: AgentState, updates: Dict[str, Any]) -> AgentState:
    """更新 UserProfile"""
    # 實現...

# ... (其他操作函數)
```

#### **步驟3: 實現測試案例**

```
# tests/state/test_state_schema.py

import pytest
from src.state.schema import AgentState
from src.state.operations import create_initial_state, update_user_profile

def test_create_initial_state():
    """測試初始化 State"""
    state = create_initial_state()
    assert state["is_complete"] == False
    assert state["next_action"] == "start"

def test_update_user_profile():
    """測試更新 UserProfile"""
    state = create_initial_state()
    updated = update_user_profile(state, {
        "user_id": "test_user",
        "skills": ["Python", "AI"]
    })
    assert updated["user_profile"]["user_id"] == "test_user"

# ... (更多測試)
```

#### **步驟4: 撰寫文檔**

```
# docs/design/state_design.md

# State Schema 設計文檔

## 概述
本文檔說明 job_search_agent 的 State Schema 設計...

## UserProfileState
用途：儲存用戶履歷資訊...

## 使用範例
...
```

### **驗證標準**
- ✅ schema.py 實現完整
- ✅ operations.py 函數正常
- ✅ 測試案例可執行
- ✅ 文檔撰寫完成
- ✅ 類型檢查通過

### **預估時間**: ~5 分鐘

---

## 🧪 Phase 4: 測試驗證 (@ANALYST)

### **目標**
驗證 State Schema 的正確性與完整性

### **執行步驟**

#### **步驟1: 執行測試套件**
```
pytest tests/state/test_state_schema.py -v
```

#### **步驟2: 類型檢查**
```
mypy src/state/schema.py --strict
```

#### **步驟3: 驗證序列化**
```
# 測試 State 可以被序列化
import json
from src.state.operations import create_initial_state

state = create_initial_state()
# 嘗試序列化（會失敗因為 datetime）
# 需要實現序列化函數
```

#### **步驟4: 文檔檢查**
- [ ] 所有欄位都有註解
- [ ] 提供使用範例
- [ ] 設計原則說明清楚

### **驗證清單**

**功能驗證**:
- [ ] State 初始化正常
- [ ] State 更新正常
- [ ] 類型檢查通過
- [ ] 測試 100% 通過

**品質驗證**:
- [ ] 命名一致性
- [ ] 類型安全性
- [ ] 文檔完整性
- [ ] 程式碼可讀性

### **預期輸出**

```
tests/state/test_state_schema.py::test_create_initial_state PASSED
tests/state/test_state_schema.py::test_update_user_profile PASSED
tests/state/test_state_schema.py::test_job_state_operations PASSED
tests/state/test_state_schema.py::test_conversation_state PASSED
tests/state/test_state_schema.py::test_system_state PASSED

========================= 5 passed in 0.5s =========================

Success: no issues found in 1 source file
```

### **⏸️ Checkpoint 2: 測試驗證確認**

**人工確認項目**:
- [ ] 測試 100% 通過
- [ ] 類型檢查通過
- [ ] 文檔完整
- [ ] 程式碼品質達標

**決策選項**:
- ✅ 確認通過 → Phase 3 完成，進入 Step 9
- 🔍 詳細檢查 → 展示測試報告
- ❌ 問題：[描述] → 暫停並修正
- 🔄 重新執行 → 返回 Phase 3

### **預估時間**: ~3 分鐘

---

## 📊 總體時間規劃

| Phase | Agent | 任務 | 預估時間 |
|-------|-------|------|----------|
| Phase 1 | @INFRA | 環境準備 | ~2 分鐘 |
| Phase 2 | @ARCH | 架構設計 | ~3 分鐘 |
| - | - | Checkpoint 1 | ~2 分鐘 |
| Phase 3 | @CODER | 程式實現 | ~5 分鐘 |
| Phase 4 | @ANALYST | 測試驗證 | ~3 分鐘 |
| - | - | Checkpoint 2 | ~2 分鐘 |
| **總計** | | | **15-20 分鐘** |

---

## 🎯 成功標準

**Phase 完成條件**:
- ✅ 4 個 Phase 全部執行完成
- ✅ 2 個 Checkpoint 全部通過
- ✅ 所有驗證項目達標
- ✅ 交付物齊全

**品質標準**:
- ✅ 測試覆蓋率 > 90%
- ✅ 類型檢查 100% 通過
- ✅ 文檔完整度 100%
- ✅ 程式碼可讀性 A 級

---

## 📁 產出物檢查清單

```
□ src/state/schema.py (完整實現)
□ src/state/operations.py (完整實現)
□ tests/state/test_state_schema.py (5+ 測試案例)
□ docs/design/state_design.md (設計文檔)
□ docs/agent_context/phase3/06_delivery_record.md (交付記錄)
```

---
