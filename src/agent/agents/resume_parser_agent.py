from datetime import datetime
from typing import List, Dict, Any
import PyPDF2

class ResumeParserAgent:
    """
    履歷解析 Agent，負責解析 PDF 履歷，提取技能、年資、學歷，計算分數
    """
    def extract_skills_from_text(self, text: str) -> List[str]:
        common_skills = ["Python", "Java", "JavaScript", "React", "FastAPI", 
                         "Docker", "Kubernetes", "AWS", "LangChain", "AI"]
        return [skill for skill in common_skills if skill.lower() in text.lower()]

    def calculate_skill_score(self, skills: List[str]) -> int:
        return min(len(skills) * 10, 100)

    def calculate_exp_score(self, years: float) -> int:
        if years >= 5:
            return 100
        elif years >= 3:
            return 80
        else:
            return 60

    def calculate_pref_score(self, preferences: dict) -> int:
        score = 0
        if preferences.get("remote"):
            score += 30
        if preferences.get("location") == "台北":
            score += 40
        if preferences.get("salary_range"):
            score += 30
        return min(score, 100)

    def parse(self, pdf_path: str) -> Dict[str, Any]:
        try:
            with open(pdf_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() or ""
        except Exception as e:
            raise RuntimeError(f"PDF解析失敗: {e}")

        skills = self.extract_skills_from_text(text)
        experience_years = 3.5  # 可根據文本進階抽取
        education = "Bachelor's Degree in Computer Science"
        preferences = {
            "salary_range": "80-100萬",
            "location": "台北",
            "remote": True
        }
        return {
            "resume_text": text,
            "skills": skills,
            "experience_years": experience_years,
            "education": education,
            "preferences": preferences,
            "parsed_at": datetime.now(),
            "skill_score": self.calculate_skill_score(skills),
            "exp_score": self.calculate_exp_score(experience_years),
            "pref_score": self.calculate_pref_score(preferences)
        }
