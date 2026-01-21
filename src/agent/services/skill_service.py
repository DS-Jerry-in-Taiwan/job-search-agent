from typing import Set

def analyze_skills(skills: Set[str]) -> str:
    """
    根據技能集合分析短板，推薦提升方向
    """
    if "AI" not in skills:
        return "推薦學習 AI/深度學習技能"
    elif "Docker" not in skills:
        return "推薦補強 Docker/DevOps 技能"
    elif "Python" not in skills:
        return "推薦學習 Python"
    else:
        return "技能組合完整，可進階專案管理"
