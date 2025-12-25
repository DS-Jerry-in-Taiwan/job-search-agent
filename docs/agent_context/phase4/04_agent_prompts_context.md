✅ **完美！提供第 4 份文件內容**

***

## ✍️ **【第 4 份檔案內容】**

### **檔案：`docs/agent_context/phase4/04_agent_prompts_context.md`**

**完整複製以下內容貼入**：

```markdown
# Phase 4 - Agent 執行 Prompts

**階段**: Day 1 步驟3 - Nodes 定義  
**用途**: 提供 4 個 Agent 的完整執行指令

---

## 🤖 @INFRA - 環境準備 Prompt

### **執行指令**

```
你是 @INFRA（環境工程師），負責 Phase 4 - Nodes 定義的環境準備。

**當前任務**: 建立 Nodes 定義所需的目錄結構與基礎檔案

**專案根目錄**: /home/ubuntu/projects/job_search_agent

**執行步驟**:

1. 建立目錄結構
   mkdir -p src/nodes
   mkdir -p tests/nodes

2. 建立基礎檔案 (9個)
   touch src/nodes/__init__.py
   touch src/nodes/resume_parser.py
   touch src/nodes/job_matcher.py
   touch src/nodes/conversation.py
   touch src/nodes/router.py
   touch src/nodes/utils.py
   touch tests/nodes/test_resume_parser.py
   touch tests/nodes/test_job_matcher.py
   touch docs/design/nodes_design.md

3. 驗證 Phase 3 依賴
   - 檢查 State Schema 可用
   - 檢查 Phase 2 Mock 數據存在

**驗證指令**:
python -c "from src.state.schema import AgentState; print('✅ State Schema OK')"
ls -lh data/mock/jobs/mock_jobs.json

**驗證標準**:
- ✅ 所有目錄已建立
- ✅ 9 個檔案已建立
- ✅ Phase 3 State 可用
- ✅ Phase 2 數據存在

**完成後輸出**:
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @INFRA
📍 Phase: Phase 1 - 環境準備
⏰ 完成時間: [時間]

✅ 執行結果
  ✅ 建立 src/nodes/ 目錄
  ✅ 建立 tests/nodes/ 目錄
  ✅ 建立 9 個基礎檔案

📁 輸出檔案
  ✅ src/nodes/__init__.py
  ✅ src/nodes/resume_parser.py
  ✅ src/nodes/job_matcher.py
  ✅ src/nodes/conversation.py
  ✅ src/nodes/router.py
  ✅ src/nodes/utils.py
  ✅ tests/nodes/test_resume_parser.py
  ✅ tests/nodes/test_job_matcher.py
  ✅ docs/design/nodes_design.md

🔍 環境驗證
  ✅ Phase 3 State Schema 可用
  ✅ Phase 2 Mock 數據存在

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
你是 @ARCH（架構設計師），負責 Phase 4 - Nodes 定義的架構設計。

**當前任務**: 設計 8 個核心 Nodes 的完整架構

**重要性**: ⭐⭐⭐⭐⭐ 這是 LangGraph 工作流程的執行核心！

**參考資料**:
- Phase 3 產出: src/state/schema.py, src/state/operations.py
- Phase 2 產出: data/mock/jobs/mock_jobs.json
- LangGraph Nodes 規範

**設計任務**:

### 1. 設計業務邏輯 Nodes (4個)

**Node 1: resume_parser_node**
```python
def resume_parser_node(state: AgentState) -> AgentState:
    """解析 PDF 履歷 → UserProfileState
    
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

**Node 2: job_matcher_node**
```python
def job_matcher_node(state: AgentState) -> AgentState:
    """履歷匹配職缺 → JobState
    
    輸入: state["user_profile"]["skills"]
    輸出: state["job_state"]["matched_jobs"], ["match_scores"]
    
    處理流程:
    1. 載入 data/mock/jobs/mock_jobs.json
    2. 計算每個職缺的匹配分數
    3. 篩選匹配度 >= 0.3 的職缺
    4. 排序並更新 JobState
    
    匹配邏輯:
    - 技能匹配度 = (用戶技能 ∩ 職缺需求) / 用戶技能數
    """
```

**Node 3: skill_analyzer_node**
```python
def skill_analyzer_node(state: AgentState) -> AgentState:
    """深度分析技能 → 增強 skills 清單"""
```

**Node 4: recommendation_node**
```python
def recommendation_node(state: AgentState) -> AgentState:
    """生成推薦理由 → recommendations"""
```

### 2. 設計工作流程控制 Nodes (4個)

**Node 5: conversation_node**
```python
def conversation_node(state: AgentState) -> AgentState:
    """生成對話回應 → ConversationState.messages
    
    處理流程:
    1. 分析用戶最後訊息
    2. 根據 current_intent 生成回應
    3. 新增 AIMessage 到 messages
    
    支援 Intents:
    - job_search: 職缺搜尋回應
    - skill_analysis: 技能分析回應
    - general: 一般對話回應
    """
```

**Node 6: router_node** ⭐ 特殊！
```python
def router_node(state: AgentState) -> str:
    """工作流程路由器 → 決定下一步
    
    返回值 (str):
    - "resume_parser": 履歷未解析
    - "job_matcher": 履歷已解析但未匹配
    - "conversation": 需要對話回應
    - "__end__": 工作流程結束
    
    ⚠️ 注意: 這是唯一返回 str 的 Node！
    """
```

**Node 7: error_handler_node**
```python
def error_handler_node(state: AgentState) -> AgentState:
    """錯誤處理與重試 → SystemState
    
    處理流程:
    1. 檢查 error_message
    2. 判斷是否需要重試
    3. 超過3次則標記失敗
    
    重試策略:
    - 最多重試 3 次
    - 超過則 workflow_status = "failed"
    """
```

**Node 8: finalizer_node**
```python
def finalizer_node(state: AgentState) -> AgentState:
    """工作流程結束 → is_complete=True
    
    處理流程:
    1. 標記完成
    2. 更新 workflow_status
    """
```

**設計原則**:
- LangGraph 規範: 函數簽名 `def node(state: AgentState) -> AgentState`
- 唯一例外: router_node 返回 str
- State 整合: 正確更新 UserProfile, JobState, Conversation, System
- 錯誤處理: 更新 system.error_message
- 可測試性: 純函數，易於測試

**輸出要求**:
將設計寫入 src/nodes/ 各檔案（僅設計框架，包含完整 docstring）

**完成後輸出**:
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @ARCH
📍 Phase: Phase 2 - 架構設計
⏰ 完成時間: [時間]

✅ 執行結果
  ✅ 設計 resume_parser_node
  ✅ 設計 job_matcher_node
  ✅ 設計 skill_analyzer_node
  ✅ 設計 recommendation_node
  ✅ 設計 conversation_node
  ✅ 設計 router_node (返回 str)
  ✅ 設計 error_handler_node
  ✅ 設計 finalizer_node

📁 輸出檔案
  ✅ src/nodes/*.py（設計框架）

🔍 設計驗證
  ✅ 8個Nodes設計完整
  ✅ 函數簽名符合LangGraph規範
  ✅ State Schema整合正確
  ✅ 工作流程邏輯合理

👉 下一步
  【Checkpoint 1】人工確認架構設計
━━━━━━━━━━━━━━━━━━━━━━━━━━

【⏸️ Checkpoint 1 - Nodes 架構設計確認】

請參考 07_checkpoint_protocol.md 進行確認。

請檢查以下項目：
□ 8個Nodes設計是否完整？
□ 函數簽名是否符合LangGraph規範？
□ router_node 是否正確返回 str？
□ State Schema整合是否正確？
□ 工作流程邏輯是否合理？
□ 錯誤處理機制是否完善？

請選擇：
✅ 確認通過 → @CODER 開始 Phase 3
🔍 詳細檢查 → 顯示完整 Nodes 設計
❌ 問題：[描述] → 暫停並修正
🔄 重新執行 Phase 2 → @ARCH 重新設計
```

---

## 💻 @CODER - 程式實現 Prompt

### **執行指令**

```
你是 @CODER（程式實現工程師），負責 Phase 4 - Nodes 定義的程式實現。

**當前任務**: 實現完整的 8 個 Nodes 與測試案例

**前置條件**: Checkpoint 1 已通過

**參考資料**:
- @ARCH 的設計: src/nodes/*.py（設計框架）
- Phase 3 State: src/state/schema.py
- Phase 2 數據: data/mock/jobs/mock_jobs.json

**實現任務**:

### 任務1: 完整實現 resume_parser.py

```python
# src/nodes/resume_parser.py
from src.state.schema import AgentState
from datetime import datetime
from typing import List

def resume_parser_node(state: AgentState) -> AgentState:
    """解析 PDF 履歷為結構化資料
    
    實際需要: PyPDF2 讀取 PDF
    Mock 實現: 使用假數據
    """
    # Mock 實現
    state["user_profile"]["user_id"] = "user_001"
    state["user_profile"]["resume_text"] = "3年Python工程師經驗..."
    state["user_profile"]["skills"] = ["Python", "FastAPI", "LangChain", "Docker"]
    state["user_profile"]["experience_years"] = 3
    state["user_profile"]["education"] = "Bachelor's Degree in Computer Science"
    state["user_profile"]["preferences"] = {
        "salary_range": "80-100萬",
        "location": "台北",
        "remote": True
    }
    state["user_profile"]["parsed_at"] = datetime.now()
    state["system"]["current_node"] = "resume_parser"
    
    return state

def extract_skills_from_text(text: str) -> List[str]:
    """從文本提取技能關鍵字（輔助函數）"""
    common_skills = ["Python", "Java", "JavaScript", "React", "FastAPI", 
                    "Docker", "Kubernetes", "AWS", "LangChain", "AI"]
    found_skills = [skill for skill in common_skills if skill.lower() in text.lower()]
    return found_skills
```

### 任務2: 完整實現 job_matcher.py

```python
# src/nodes/job_matcher.py
from src.state.schema import AgentState
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set

def job_matcher_node(state: AgentState) -> AgentState:
    """根據履歷匹配職缺"""
    # 載入職缺數據
    jobs_path = Path("data/mock/jobs/mock_jobs.json")
    with open(jobs_path, "r", encoding="utf-8") as f:
        all_jobs = json.load(f)
    
    # 計算匹配分數
    user_skills = set(s.lower() for s in state["user_profile"]["skills"])
    matched_jobs = []
    match_scores = {}
    
    for job in all_jobs:
        score = calculate_match_score(user_skills, job)
        if score >= 0.3:  # 匹配度閾值
            matched_jobs.append(job)
            match_scores[job["job_id"]] = round(score, 2)
    
    # 排序（按匹配度降序）
    matched_jobs.sort(key=lambda j: match_scores[j["job_id"]], reverse=True)
    
    # 更新 State
    state["job_state"]["jobs"] = all_jobs
    state["job_state"]["matched_jobs"] = matched_jobs
    state["job_state"]["match_scores"] = match_scores
    state["job_state"]["recommendations"] = []
    state["job_state"]["last_updated"] = datetime.now()
    state["system"]["current_node"] = "job_matcher"
    
    return state

def calculate_match_score(user_skills: Set[str], job: Dict) -> float:
    """計算匹配分數 (0.0 - 1.0)"""
    job_requirements = job.get("requirements", "").lower()
    job_skills = set(job_requirements.split())
    
    # 技能匹配度
    matched_skills = user_skills & job_skills
    if not user_skills:
        return 0.0
    
    skill_score = len(matched_skills) / len(user_skills)
    return min(skill_score, 1.0)
```

### 任務3: 完整實現 conversation.py

```python
# src/nodes/conversation.py
from src.state.schema import AgentState
from langchain_core.messages import AIMessage

def conversation_node(state: AgentState) -> AgentState:
    """生成對話回應"""
    intent = state["conversation"]["current_intent"]
    
    # 根據意圖生成回應
    if intent == "job_search":
        response = generate_job_search_response(state)
    elif intent == "skill_analysis":
        response = generate_skill_analysis_response(state)
    else:
        response = "您好！我是職涯搜尋 AI 助手，請問需要什麼幫助？"
    
    # 新增 AI 訊息
    ai_message = AIMessage(content=response)
    state["conversation"]["messages"].append(ai_message)
    state["conversation"]["turn_count"] += 1
    state["system"]["current_node"] = "conversation"
    
    return state

def generate_job_search_response(state: AgentState) -> str:
    """生成職缺搜尋回應"""
    matched_count = len(state["job_state"]["matched_jobs"])
    top_jobs = state["job_state"]["matched_jobs"][:3]
    
    if matched_count == 0:
        return "很抱歉，目前沒有找到符合的職缺。"
    
    response = f"找到 {matched_count} 個符合的職缺！\n\n前3名推薦：\n"
    
    for i, job in enumerate(top_jobs, 1):
        score = state["job_state"]["match_scores"][job["job_id"]]
        response += f"{i}. {job['title']} - {job['company']} (匹配度 {score*100:.0f}%)\n"
    
    return response

def generate_skill_analysis_response(state: AgentState) -> str:
    """生成技能分析回應"""
    skills = state["user_profile"]["skills"]
    return f"您的技能清單：{', '.join(skills)}\n共 {len(skills)} 項技能。"
```

### 任務4: 完整實現 router.py

```python
# src/nodes/router.py
from src.state.schema import AgentState

def router_node(state: AgentState) -> str:
    """工作流程路由器
    
    ⚠️ 注意: 這是唯一返回 str 的 Node！
    """
    # 檢查履歷是否已解析
    if not state["user_profile"].get("skills"):
        return "resume_parser"
    
    # 檢查職缺是否已匹配
    if not state["job_state"].get("matched_jobs"):
        return "job_matcher"
    
    # 檢查是否需要對話
    if state["conversation"]["messages"] and not state["is_complete"]:
        return "conversation"
    
    # 結束工作流程
    return "__end__"

def error_handler_node(state: AgentState) -> AgentState:
    """錯誤處理節點"""
    if state["system"]["error_message"]:
        state["system"]["retry_count"] += 1
        
        if state["system"]["retry_count"] > 3:
            # 超過重試次數，標記失敗
            state["system"]["workflow_status"] = "failed"
            state["is_complete"] = True
        else:
            # 清除錯誤，準備重試
            state["system"]["error_message"] = None
            state["system"]["workflow_status"] = "retrying"
    
    state["system"]["current_node"] = "error_handler"
    return state

def finalizer_node(state: AgentState) -> AgentState:
    """工作流程結束節點"""
    state["is_complete"] = True
    state["system"]["workflow_status"] = "completed"
    state["system"]["current_node"] = "finalizer"
    return state
```

### 任務5: 完整實現 utils.py

```python
# src/nodes/utils.py
from src.state.schema import AgentState

def skill_analyzer_node(state: AgentState) -> AgentState:
    """深度分析技能（Mock實現）"""
    # 增強技能清單
    base_skills = state["user_profile"]["skills"]
    
    # Mock: 增加相關技能
    enhanced_skills = base_skills.copy()
    if "Python" in base_skills:
        enhanced_skills.extend(["Django", "Flask"])
    if "JavaScript" in base_skills:
        enhanced_skills.extend(["TypeScript", "Node.js"])
    
    state["user_profile"]["skills"] = list(set(enhanced_skills))
    state["system"]["current_node"] = "skill_analyzer"
    return state

def recommendation_node(state: AgentState) -> AgentState:
    """生成推薦理由"""
    matched = state["job_state"]["matched_jobs"][:5]
    recommendations = []
    
    for job in matched:
        job_id = job["job_id"]
        score = state["job_state"]["match_scores"][job_id]
        reason = f"推薦 {job['title']}：匹配度 {score*100:.0f}%，符合您的技能需求。"
        recommendations.append(reason)
    
    state["job_state"]["recommendations"] = recommendations
    state["system"]["current_node"] = "recommendation"
    return state
```

### 任務6: 實現 __init__.py

```python
# src/nodes/__init__.py
"""Nodes 模組 - LangGraph 工作流程節點"""

from .resume_parser import resume_parser_node, extract_skills_from_text
from .job_matcher import job_matcher_node, calculate_match_score
from .conversation import conversation_node
from .router import router_node, error_handler_node, finalizer_node
from .utils import skill_analyzer_node, recommendation_node

__all__ = [
    "resume_parser_node",
    "extract_skills_from_text",
    "job_matcher_node",
    "calculate_match_score",
    "conversation_node",
    "router_node",
    "error_handler_node",
    "finalizer_node",
    "skill_analyzer_node",
    "recommendation_node",
]
```

### 任務7: 實現測試案例

```python
# tests/nodes/test_resume_parser.py
import pytest
from src.state.operations import create_initial_state
from src.nodes.resume_parser import resume_parser_node, extract_skills_from_text

def test_resume_parser_node():
    """測試履歷解析節點"""
    state = create_initial_state()
    result = resume_parser_node(state)
    
    assert result["user_profile"]["skills"]
    assert result["user_profile"]["experience_years"] > 0
    assert result["user_profile"]["parsed_at"] is not None
    assert result["system"]["current_node"] == "resume_parser"

def test_extract_skills_from_text():
    """測試技能提取函數"""
    text = "3 years of Python and Docker experience"
    skills = extract_skills_from_text(text)
    
    assert "Python" in skills
    assert "Docker" in skills

# tests/nodes/test_job_matcher.py
import pytest
from src.state.operations import create_initial_state
from src.nodes.resume_parser import resume_parser_node
from src.nodes.job_matcher import job_matcher_node, calculate_match_score

def test_job_matcher_node():
    """測試職缺匹配節點"""
    state = create_initial_state()
    state = resume_parser_node(state)  # 先解析履歷
    result = job_matcher_node(state)
    
    assert result["job_state"]["matched_jobs"]
    assert result["job_state"]["match_scores"]
    assert len(result["job_state"]["jobs"]) > 0
    assert result["system"]["current_node"] == "job_matcher"

def test_calculate_match_score():
    """測試匹配分數計算"""
    user_skills = {"python", "docker"}
    job = {"job_id": "001", "requirements": "Python Docker Kubernetes"}
    
    score = calculate_match_score(user_skills, job)
    assert 0.0 <= score <= 1.0
    assert score > 0  # 應該有匹配
```

### 任務8: 撰寫設計文檔

```markdown
# docs/design/nodes_design.md

# Nodes 設計文檔

## 8 個核心 Nodes

### 業務邏輯 Nodes
1. **resume_parser_node** - 履歷解析
2. **job_matcher_node** - 職缺匹配
3. **skill_analyzer_node** - 技能分析
4. **recommendation_node** - 推薦生成

### 工作流程控制 Nodes
5. **conversation_node** - 對話生成
6. **router_node** - 工作流程路由 ⭐ 返回 str
7. **error_handler_node** - 錯誤處理
8. **finalizer_node** - 流程結束

## 使用範例
...（詳細使用範例）...
```

**完成後輸出**:
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @CODER
📍 Phase: Phase 3 - 程式實現
⏰ 完成時間: [時間]

✅ 執行結果
  ✅ 完整實現 resume_parser.py
  ✅ 完整實現 job_matcher.py
  ✅ 完整實現 conversation.py
  ✅ 完整實現 router.py
  ✅ 完整實現 utils.py
  ✅ 完整實現 __init__.py
  ✅ 實現 5+ 個測試案例
  ✅ 撰寫設計文檔

📁 輸出檔案
  ✅ src/nodes/*.py（完整實現）
  ✅ tests/nodes/test_*.py（5+ 測試）
  ✅ docs/design/nodes_design.md

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
你是 @ANALYST（品質分析師），負責 Phase 4 - Nodes 定義的測試驗證。

**當前任務**: 驗證 Nodes 的正確性、完整性與品質

**參考資料**:
- @CODER 的實現: src/nodes/*.py
- 驗證清單: docs/agent_context/phase4/05_validation_checklist.md
- 測試案例: tests/nodes/test_*.py

**驗證任務**:

### 任務1: 執行測試套件

**執行指令**:
```bash
pytest tests/nodes/ -v --cov=src/nodes
```

**驗證標準**:
- ✅ 所有測試通過（5+ 個測試）
- ✅ 測試覆蓋率 > 90%
- ✅ 無測試錯誤

### 任務2: 整合測試

**執行腳本**:
```python
from src.state.operations import create_initial_state
from src.nodes.resume_parser import resume_parser_node
from src.nodes.job_matcher import job_matcher_node
from src.nodes.router import router_node

# 測試 Nodes 串連
state = create_initial_state()
print(f"初始狀態: {router_node(state)}")  # 應該返回 "resume_parser"

state = resume_parser_node(state)
print(f"履歷解析後: {router_node(state)}")  # 應該返回 "job_matcher"

state = job_matcher_node(state)
print(f"職缺匹配後: 找到 {len(state['job_state']['matched_jobs'])} 個職缺")

print("✅ 整合測試通過！")
```

**驗證標準**:
- ✅ Nodes 可以串連執行
- ✅ State 正確傳遞
- ✅ router_node 返回正確

### 任務3: 類型檢查

**執行指令**:
```bash
mypy src/nodes/ --strict
```

**驗證標準**:
- ✅ 類型檢查 100% 通過
- ✅ 無類型錯誤

### 任務4: 程式碼品質檢查

**檢查項目**:
- [ ] 命名一致性（snake_case）
- [ ] 函數簽名正確
- [ ] docstring 完整
- [ ] 程式碼可讀性 A 級
- [ ] 無冗餘程式碼

### 任務5: 文檔檢查

**檢查項目**:
- [ ] docs/design/nodes_design.md 存在
- [ ] 所有 Nodes 都有說明
- [ ] 使用範例清楚
- [ ] 設計決策記錄

### 任務6: 生成測試報告

**報告格式**:
```
Nodes 測試報告
==================

測試執行時間: [時間]

測試結果: ✅ PASSED (8/8)
類型檢查: ✅ PASSED
測試覆蓋率: 92%
程式碼品質: A

詳細結果:
- test_resume_parser_node: PASSED
- test_extract_skills_from_text: PASSED
- test_job_matcher_node: PASSED
- test_calculate_match_score: PASSED
- test_router_node: PASSED
- test_error_handler_node: PASSED
- test_finalizer_node: PASSED
- test_conversation_node: PASSED

整合測試:
✅ Nodes 串連正常
✅ State 傳遞正確
✅ router_node 邏輯正確

品質檢查:
✅ 命名一致性
✅ 函數簽名正確
✅ docstring 完整
✅ 程式碼可讀性 A

文檔檢查:
✅ 設計文檔完整
✅ 使用範例清楚

建議:
- 無重大問題
- 可進入 Phase 5 (Graph 構建)

結論:
✅ Phase 4 (Nodes 定義) 驗證通過
```

**完成後輸出**:
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @ANALYST
📍 Phase: Phase 4 - 測試驗證
⏰ 完成時間: [時間]

✅ 執行結果
  ✅ 測試通過率 100% (8/8)
  ✅ 類型檢查通過
  ✅ 測試覆蓋率 92%
  ✅ 整合測試通過
  ✅ 程式碼品質 A 級
  ✅ 文檔完整

📁 輸出檔案
  ✅ 測試報告（控制台輸出）
  ✅ 品質評估（控制台輸出）

🔍 驗證結果
  ✅ 所有測試通過
  ✅ 類型檢查通過
  ✅ Nodes 串連正常
  ✅ 程式碼品質達標
  ✅ 文檔完整

👉 下一步
  【Checkpoint 2】人工確認測試結果
━━━━━━━━━━━━━━━━━━━━━━━━━━

【⏸️ Checkpoint 2 - 測試驗證確認】

請參考 07_checkpoint_protocol.md 進行確認。

請檢查以下項目：
□ 測試 100% 通過 (8/8)？
□ 整合測試通過？
□ 類型檢查通過？
□ 測試覆蓋率 > 90%？
□ 程式碼品質達標？
□ 文檔完整？

請選擇：
✅ 確認通過 → Phase 4 完成，進入 Phase 5
🔍 詳細檢查 → 顯示測試報告
❌ 問題：[描述] → 暫停並修正
🔄 重新執行 Phase 3/4 → 重新實現/測試
```

---

