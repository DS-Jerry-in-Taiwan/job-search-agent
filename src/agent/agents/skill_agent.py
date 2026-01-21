from typing import Set

class SkillAgent:
    """
    技能分析 Agent，根據技能集合分析短板，推薦提升方向
    """
    def analyze(self, skills: Set[str]) -> str:
        if "AI" not in skills:
            return "推薦學習 AI/深度學習技能"
        elif "Docker" not in skills:
            return "推薦補強 Docker/DevOps 技能"
        elif "Python" not in skills:
            return "推薦學習 Python"
        else:
            return "技能組合完整，可進階專案管理"
