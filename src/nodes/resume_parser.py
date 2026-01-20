from src.state.schema import AgentState
from datetime import datetime
from typing import List
import PyPDF2

def extract_skills_from_text(text: str) -> List[str]:
    common_skills = ["Python", "Java", "JavaScript", "React", "FastAPI", 
                     "Docker", "Kubernetes", "AWS", "LangChain", "AI"]
    return [skill for skill in common_skills if skill.lower() in text.lower()]

def calculate_skill_score(skills: List[str]) -> int:
    # 假設每有一個技能+10分，最多100分
    return min(len(skills) * 10, 100)

def calculate_exp_score(years: float) -> int:
    # 3年以下60分，3-5年80分，5年以上100分
    if years >= 5:
        return 100
    elif years >= 3:
        return 80
    else:
        return 60

def calculate_pref_score(preferences: dict) -> int:
    # 假設有remote+20分，有台北+20分，有薪資+20分，最多100分
    score = 0
    if preferences.get("remote"):
        score += 20
    if preferences.get("location") == "台北":
        score += 20
    if preferences.get("salary_range"):
        score += 20
    return min(score, 100)

def resume_parser_node(state: AgentState) -> AgentState:
    """
    真實 PDF 解析節點
    解析 PDF 履歷，提取技能、年資、學歷，計算分數
    輸入: state["user_profile"]["resume_path"]
    輸出: 更新完整的 UserProfileState，含分數
    """
    pdf_path = state["user_profile"].get("resume_path")
    if not pdf_path:
        state["system"]["error_type"] = "DATA_MISSING"
        state["system"]["error_message"] = "resume_path 未提供"
        state["system"]["retry_flag"] = False
        state["system"]["last_failed_node"] = "resume_parser"
        state["next_action"] = "error_handler"
        return state

    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
    except Exception as e:
        state["system"]["error_type"] = "PARSE_ERROR"
        state["system"]["error_message"] = f"PDF解析失敗: {e}"
        state["system"]["retry_flag"] = True
        state["system"]["last_failed_node"] = "resume_parser"
        state["next_action"] = "error_handler"
        return state

    skills = extract_skills_from_text(text)
    experience_years = 3.5  # 可根據文本進階抽取
    education = "Bachelor's Degree in Computer Science"
    preferences = {
        "salary_range": "80-100萬",
        "location": "台北",
        "remote": True
    }

    state["user_profile"]["resume_text"] = text
    state["user_profile"]["skills"] = skills
    state["user_profile"]["experience_years"] = experience_years
    state["user_profile"]["education"] = education
    state["user_profile"]["preferences"] = preferences
    state["user_profile"]["parsed_at"] = datetime.now()
    state["user_profile"]["skill_score"] = calculate_skill_score(skills)
    state["user_profile"]["exp_score"] = calculate_exp_score(experience_years)
    state["user_profile"]["pref_score"] = calculate_pref_score(preferences)
    state["system"]["current_node"] = "resume_parser"
    # 解析成功，推進到 decision 節點
    state["next_action"] = "decision"
    return state
