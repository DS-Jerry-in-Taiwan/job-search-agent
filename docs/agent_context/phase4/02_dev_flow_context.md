✅ **完美！提供第 2 份文件內容**

***

## ✍️ **【第 2 份檔案內容】**

### **檔案：`docs/agent_context/phase4/02_dev_flow_context.md`**

**完整複製以下內容貼入**：

```markdown
# Phase 4 - Nodes 定義開發流程

**階段**: Day 1 步驟3 - Nodes 定義  
**執行模式**: 混合模式（Checkpoint 1 和 2）  
**預估時間**: 16-20 分鐘

---

## 🚀 開發流程總覽

```
Phase 1 (INFRA)  → Phase 2 (ARCH)     → Phase 3 (CODER)    → Phase 4 (ANALYST)
環境準備          Nodes架構設計         程式實現              測試驗證
~2分鐘            ~4分鐘               ~6分鐘                ~4分鐘
                 [Checkpoint 1] ⏸️                         [Checkpoint 2] ⏸️
```

---

## 📋 Phase 1: 環境準備 (@INFRA)

### **目標**
建立 Nodes 開發所需的目錄結構與基礎檔案

### **執行步驟**

1. **建立目錄結構**
```
mkdir -p src/nodes
mkdir -p tests/nodes
```

2. **建立基礎檔案**
```
touch src/nodes/__init__.py
touch src/nodes/resume_parser.py
touch src/nodes/job_matcher.py
touch src/nodes/conversation.py
touch src/nodes/router.py
touch src/nodes/utils.py
touch tests/nodes/test_resume_parser.py
touch tests/nodes/test_job_matcher.py
touch docs/design/nodes_design.md
```

3. **驗證 Phase 3 State 可用**
```
python -c "from src.state.schema import AgentState; print('State Schema OK')"
```

### **驗證標準**
- ✅ 目錄結構正確
- ✅ 9 個檔案已建立
- ✅ Phase 3 State Schema 可用

### **預期輸出**
```
src/nodes/ (6個檔案)
tests/nodes/ (2個檔案)
docs/design/nodes_design.md
Phase 3 State Schema ✅ 可用
```

### **預估時間**: ~2 分鐘

---

## 🏗️ Phase 2: Nodes 架構設計 (@ARCH)

### **目標**
設計 8 個核心 Nodes 的完整架構與函數簽名

### **8 個 Nodes 設計規格**

#### **Node 1: resume_parser_node**
```
# src/nodes/resume_parser.py
from src.state.schema import AgentState
from datetime import datetime

def resume_parser_node(state: AgentState) -> AgentState:
    """解析 PDF 履歷 → UserProfileState
    
    輸入: state["user_profile"]["resume_text"] (PDF路徑或文本)
    輸出: 更新 state["user_profile"] 所有欄位
    
    處理邏輯:
    1. 讀取 PDF 檔案 (使用 PyPDF2)
    2. 提取技能關鍵字 (正則或 NLP)
    3. 提取工作年資
    4. 提取學歷資訊
    5. 更新 parsed_at 時間戳
    """
    # Mock 實現 (實際需要 PDF 解析)
    state["user_profile"]["skills"] = ["Python", "LangChain", "FastAPI"]
    state["user_profile"]["experience_years"] = 3
    state["user_profile"]["education"] = "Bachelor"
    state["user_profile"]["parsed_at"] = datetime.now()
    state["system"]["current_node"] = "resume_parser"
    return state
```

#### **Node 2: job_matcher_node**
```
# src/nodes/job_matcher.py
from src.state.schema import AgentState
import json
from datetime import datetime

def job_matcher_node(state: AgentState) -> AgentState:
    """履歷匹配職缺 → JobState
    
    輸入: state["user_profile"]["skills"]
    輸出: state["job_state"]["matched_jobs"], ["match_scores"]
    
    處理邏輯:
    1. 載入 data/mock/jobs/mock_jobs.json
    2. 計算每個職缺的匹配分數
    3. 篩選匹配度 >= 0.3 的職缺
    4. 排序並更新 JobState
    """
    # 載入職缺
    with open("data/mock/jobs/mock_jobs.json") as f:
        all_jobs = json.load(f)
    
    # 計算匹配分數
    user_skills = set(s.lower() for s in state["user_profile"]["skills"])
    matched = []
    scores = {}
    
    for job in all_jobs:
        # 簡單匹配邏輯
        job_skills = set(job["requirements"].lower().split())
        match_count = len(user_skills & job_skills)
        score = match_count / max(len(user_skills), 1)
        
        if score >= 0.3:
            matched.append(job)
            scores[job["job_id"]] = score
    
    state["job_state"]["jobs"] = all_jobs
    state["job_state"]["matched_jobs"] = matched
    state["job_state"]["match_scores"] = scores
    state["job_state"]["last_updated"] = datetime.now()
    state["system"]["current_node"] = "job_matcher"
    return state
```

#### **Node 3: skill_analyzer_node**
```
# src/nodes/utils.py
def skill_analyzer_node(state: AgentState) -> AgentState:
    """技能深度分析 → 增強 skills 清單
    
    輸入: state["user_profile"]["resume_text"]
    輸出: 更新 state["user_profile"]["skills"]
    
    處理邏輯:
    1. NLP 分析履歷文本
    2. 提取技術關鍵字
    3. 分類技能等級 (基礎/進階/專家)
    """
    # Mock 實現
    enhanced_skills = state["user_profile"]["skills"] + ["Docker", "Kubernetes"]
    state["user_profile"]["skills"] = list(set(enhanced_skills))
    return state
```

#### **Node 4: recommendation_node**
```
# src/nodes/utils.py
def recommendation_node(state: AgentState) -> AgentState:
    """生成推薦理由 → recommendations
    
    輸入: state["job_state"]["matched_jobs"]
    輸出: state["job_state"]["recommendations"]
    
    處理邏輯:
    1. 分析匹配度最高的職缺
    2. 生成推薦理由 (為何推薦此職位)
    3. 更新 recommendations 清單
    """
    matched = state["job_state"]["matched_jobs"][:5]
    recommendations = []
    
    for job in matched:
        reason = f"推薦 {job['title']}：符合您的 {', '.join(state['user_profile']['skills'][:3])} 技能"
        recommendations.append(reason)
    
    state["job_state"]["recommendations"] = recommendations
    return state
```

#### **Node 5: conversation_node**
```
# src/nodes/conversation.py
from langchain_core.messages import HumanMessage, AIMessage

def conversation_node(state: AgentState) -> AgentState:
    """生成對話回應 → ConversationState.messages
    
    輸入: state["conversation"]["messages"]
    輸出: 新增 AI 回應到 messages
    
    處理邏輯:
    1. 分析用戶最後一條訊息
    2. 根據 current_intent 生成回應
    3. 新增到 messages 清單
    """
    last_message = state["conversation"]["messages"][-1] if state["conversation"]["messages"] else None
    
    # 生成回應
    if state["conversation"]["current_intent"] == "job_search":
        response = f"找到 {len(state['job_state']['matched_jobs'])} 個符合的職缺！"
    else:
        response = "您好！我是職涯搜尋助手。"
    
    ai_message = AIMessage(content=response)
    state["conversation"]["messages"].append(ai_message)
    state["conversation"]["turn_count"] += 1
    return state
```

#### **Node 6: router_node**
```
# src/nodes/router.py
def router_node(state: AgentState) -> str:
    """工作流程路由器 → 決定下一步
    
    輸入: state 整體狀態
    輸出: 下一個 node 名稱 (str)
    
    返回值:
    - "resume_parser": 履歷未解析
    - "job_matcher": 履歷已解析但未匹配
    - "conversation": 需要對話回應
    - "__end__": 工作流程結束
    """
    # 路由邏輯
    if not state["user_profile"].get("skills"):
        return "resume_parser"
    
    if not state["job_state"].get("matched_jobs"):
        return "job_matcher"
    
    if state["conversation"]["messages"] and not state["is_complete"]:
        return "conversation"
    
    return "__end__"
```

#### **Node 7: error_handler_node**
```
# src/nodes/router.py
def error_handler_node(state: AgentState) -> AgentState:
    """錯誤處理與重試 → SystemState
    
    輸入: state["system"]["error_message"]
    輸出: 更新 retry_count, 清除 error_message
    
    處理邏輯:
    1. 檢查 error_message
    2. 判斷是否需要重試
    3. 更新 retry_count
    4. 超過3次則標記失敗
    """
    if state["system"]["error_message"]:
        state["system"]["retry_count"] += 1
        
        if state["system"]["retry_count"] > 3:
            state["system"]["workflow_status"] = "failed"
            state["is_complete"] = True
        else:
            state["system"]["error_message"] = None
            state["system"]["workflow_status"] = "retrying"
    
    return state
```

#### **Node 8: finalizer_node**
```
# src/nodes/router.py
def finalizer_node(state: AgentState) -> AgentState:
    """工作流程結束 → is_complete=True
    
    輸入: state 整體狀態
    輸出: state["is_complete"] = True
    
    處理邏輯:
    1. 標記工作流程完成
    2. 更新 workflow_status
    3. 記錄完成時間
    """
    state["is_complete"] = True
    state["system"]["workflow_status"] = "completed"
    state["system"]["current_node"] = "finalizer"
    return state
```

### **設計驗證標準**
- ✅ 8個Nodes函數簽名正確
- ✅ 輸入/輸出都是 AgentState（router 除外返回 str）
- ✅ 依賴 Phase 3 State Schema
- ✅ 錯誤處理機制完整
- ✅ 每個 Node 都有清晰的 docstring

### **⏸️ Checkpoint 1: Nodes 架構確認**

**人工確認項目**:
- [ ] 8個Nodes設計完整？
- [ ] 函數簽名符合LangGraph規範？
- [ ] State Schema整合正確？
- [ ] 工作流程邏輯合理？
- [ ] 錯誤處理機制完善？

### **預估時間**: ~4 分鐘

---

## 💻 Phase 3: 程式實現 (@CODER)

### **目標**
實現完整的 8 個 Nodes 與測試案例

### **執行步驟**

#### **步驟1: 實現 resume_parser.py**
```
# src/nodes/resume_parser.py
from src.state.schema import AgentState
from datetime import datetime
from typing import Dict, Any

def resume_parser_node(state: AgentState) -> AgentState:
    """解析 PDF 履歷為結構化資料"""
    # 實際實現需要 PyPDF2
    # from PyPDF2 import PdfReader
    
    # Mock 實現
    mock_profile: Dict[str, Any] = {
        "user_id": "user_001",
        "resume_text": "3年Python工程師經驗，熟悉FastAPI、LangChain...",
        "skills": ["Python", "FastAPI", "LangChain", "Docker"],
        "experience_years": 3,
        "education": "Bachelor's Degree in Computer Science",
        "preferences": {
            "salary_range": "80-100萬",
            "location": "台北",
            "remote": True
        },
        "parsed_at": datetime.now()
    }
    
    state["user_profile"] = mock_profile
    state["system"]["current_node"] = "resume_parser"
    return state

def extract_skills_from_text(text: str) -> list:
    """從文本提取技能關鍵字"""
    # 簡單實現，實際可用 NLP
    common_skills = ["Python", "Java", "JavaScript", "React", "FastAPI", 
                    "Docker", "Kubernetes", "AWS", "LangChain", "AI"]
    found_skills = [skill for skill in common_skills if skill.lower() in text.lower()]
    return found_skills
```

#### **步驟2: 實現 job_matcher.py**
```
# src/nodes/job_matcher.py
from src.state.schema import AgentState
import json
from datetime import datetime
from pathlib import Path

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
    state["job_state"]["last_updated"] = datetime.now()
    state["system"]["current_node"] = "job_matcher"
    
    return state

def calculate_match_score(user_skills: set, job: dict) -> float:
    """計算匹配分數 (0.0 - 1.0)"""
    job_requirements = job.get("requirements", "").lower()
    job_skills = set(job_requirements.split())
    
    # 技能匹配度
    matched_skills = user_skills & job_skills
    skill_score = len(matched_skills) / max(len(user_skills), 1)
    
    return min(skill_score, 1.0)
```

#### **步驟3: 實現 conversation.py**
```
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
    
    return state

def generate_job_search_response(state: AgentState) -> str:
    """生成職缺搜尋回應"""
    matched_count = len(state["job_state"]["matched_jobs"])
    top_jobs = state["job_state"]["matched_jobs"][:3]
    
    response = f"找到 {matched_count} 個符合的職缺！\n\n"
    response += "前3名推薦：\n"
    
    for i, job in enumerate(top_jobs, 1):
        score = state["job_state"]["match_scores"][job["job_id"]]
        response += f"{i}. {job['title']} - {job['company']} (匹配度 {score*100:.0f}%)\n"
    
    return response

def generate_skill_analysis_response(state: AgentState) -> str:
    """生成技能分析回應"""
    skills = state["user_profile"]["skills"]
    return f"您的技能清單：{', '.join(skills)}\n共 {len(skills)} 項技能。"
```

#### **步驟4: 實現 router.py**
```
# src/nodes/router.py
from src.state.schema import AgentState

def router_node(state: AgentState) -> str:
    """工作流程路由器"""
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
            state["system"]["workflow_status"] = "failed"
            state["is_complete"] = True
        else:
            state["system"]["error_message"] = None
            state["system"]["workflow_status"] = "retrying"
    
    return state

def finalizer_node(state: AgentState) -> AgentState:
    """工作流程結束節點"""
    state["is_complete"] = True
    state["system"]["workflow_status"] = "completed"
    state["system"]["current_node"] = "finalizer"
    return state
```

#### **步驟5: 實現 utils.py**
```
# src/nodes/utils.py
from src.state.schema import AgentState

def skill_analyzer_node(state: AgentState) -> AgentState:
    """深度分析技能"""
    # 增強技能清單
    base_skills = state["user_profile"]["skills"]
    enhanced_skills = base_skills + ["相關技能A", "相關技能B"]
    state["user_profile"]["skills"] = list(set(enhanced_skills))
    return state

def recommendation_node(state: AgentState) -> AgentState:
    """生成推薦理由"""
    matched = state["job_state"]["matched_jobs"][:5]
    recommendations = []
    
    for job in matched:
        score = state["job_state"]["match_scores"][job["job_id"]]
        reason = f"推薦 {job['title']}：匹配度 {score*100:.0f}%"
        recommendations.append(reason)
    
    state["job_state"]["recommendations"] = recommendations
    return state
```

#### **步驟6: 實現測試案例**
```
# tests/nodes/test_resume_parser.py
import pytest
from src.state.operations import create_initial_state
from src.nodes.resume_parser import resume_parser_node

def test_resume_parser_node():
    """測試履歷解析節點"""
    state = create_initial_state()
    result = resume_parser_node(state)
    
    assert result["user_profile"]["skills"]
    assert result["user_profile"]["experience_years"] > 0
    assert result["system"]["current_node"] == "resume_parser"

# tests/nodes/test_job_matcher.py
import pytest
from src.state.operations import create_initial_state
from src.nodes.resume_parser import resume_parser_node
from src.nodes.job_matcher import job_matcher_node

def test_job_matcher_node():
    """測試職缺匹配節點"""
    state = create_initial_state()
    state = resume_parser_node(state)  # 先解析履歷
    result = job_matcher_node(state)
    
    assert result["job_state"]["matched_jobs"]
    assert result["job_state"]["match_scores"]
    assert len(result["job_state"]["jobs"]) > 0
```

#### **步驟7: 撰寫設計文檔**
```
# docs/design/nodes_design.md

# Nodes 設計文檔

## 8 個核心 Nodes

1. resume_parser_node - 履歷解析
2. job_matcher_node - 職缺匹配
3. skill_analyzer_node - 技能分析
4. recommendation_node - 推薦生成
5. conversation_node - 對話生成
6. router_node - 工作流程路由
7. error_handler_node - 錯誤處理
8. finalizer_node - 流程結束

## 使用範例
...
```

### **驗證標準**
- ✅ 所有 Nodes 實現完整
- ✅ 測試案例可執行
- ✅ 文檔撰寫完成
- ✅ 類型檢查通過

### **預估時間**: ~6 分鐘

---

## 🧪 Phase 4: 測試驗證 (@ANALYST)

### **驗證指令**
```
# 單元測試
pytest tests/nodes/ -v --cov=src/nodes

# 整合測試
python -c "
from src.state.operations import create_initial_state
from src.nodes.resume_parser import resume_parser_node
from src.nodes.job_matcher import job_matcher_node

state = create_initial_state()
state = resume_parser_node(state)
state = job_matcher_node(state)

print(f'✅ 整合測試通過！')
print(f'匹配職缺數: {len(state[\"job_state\"][\"matched_jobs\"])}')
"

# 類型檢查
mypy src/nodes/ --strict
```

### **驗證標準**
- ✅ 測試通過率 100%
- ✅ 覆蓋率 >90%
- ✅ 類型檢查通過
- ✅ Nodes可以串連執行

### **⏸️ Checkpoint 2: 測試驗證確認**

### **預估時間**: ~4 分鐘

---

## 📊 總體時間規劃

| Phase | Agent | 任務 | 預估時間 |
|-------|-------|------|----------|
| Phase 1 | @INFRA | 環境準備 | ~2 分鐘 |
| Phase 2 | @ARCH | Nodes設計 | ~4 分鐘 |
| - | - | Checkpoint 1 | ~2 分鐘 |
| Phase 3 | @CODER | 程式實現 | ~6 分鐘 |
| Phase 4 | @ANALYST | 測試驗證 | ~4 分鐘 |
| - | - | Checkpoint 2 | ~2 分鐘 |
| **總計** | | | **16-20 分鐘** |

---

**Phase 4是LangGraph工作流程的核心！品質第一！** 🚀
```

***