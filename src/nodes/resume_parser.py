from src.state.schema import AgentState
from datetime import datetime
from typing import List

def resume_parser_node(state: AgentState) -> AgentState:
    """
    解析 PDF 履歷 → UserProfileState

    輸入: state["user_profile"]["resume_text"]
    輸出: 更新完整的 UserProfileState

    處理流程:
    1. 讀取 PDF 檔案 (PyPDF2)
    2. 提取技能關鍵字
    3. 提取工作年資
    4. 提取學歷
    5. 更新 parsed_at
    """
    # Mock 實作
    state["user_profile"]["user_id"] = "user_001"
    state["user_profile"]["resume_text"] = "3年Python工程師經驗..."
    state["user_profile"]["skills"] = extract_skills_from_text(state["user_profile"]["resume_text"])
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
    """
    從文本提取技能關鍵字（輔助函數）

    :param text: 履歷文本
    :return: 技能清單
    """
    common_skills = ["Python", "Java", "JavaScript", "React", "FastAPI", 
                     "Docker", "Kubernetes", "AWS", "LangChain", "AI"]
    found_skills = [skill for skill in common_skills if skill.lower() in text.lower()]
    return found_skills
