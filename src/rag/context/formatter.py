from typing import List, Dict, Any

class ContextFormatter:
    """
    將組裝後的資料格式化為 LLM 友好 Markdown Prompt。
    """

    def format_context(self, query: str, jobs: List[Dict[str, Any]], analysis: Dict[str, Any]) -> str:
        """
        產生 LLM 輸入格式的 Markdown prompt。
        """
        user_skills = analysis.get("user_skills", [])
        match_scores = analysis.get("match_scores", [])
        best_job = analysis.get("best_job", "")
        lines = []
        lines.append(f"用戶需求: {query}")
        lines.append(f"用戶技能: {', '.join(user_skills)}\n")
        lines.append(f"🔍 精選職缺 (Top-{len(jobs)}):\n")
        for idx, job in enumerate(jobs, 1):
            title = job.get("title", "未知職缺")
            company = job.get("company", "")
            salary = job.get("salary", "")
            location = job.get("location", "")
            skills = job.get("skills", [])
            match = job.get("match_score", 0)
            lines.append(f"{idx}. **{company} {title}**")
            if salary or location:
                lines.append(f"   💰 {salary} | 📍 {location}")
            lines.append(f"   技能匹配: {match}% ({' '.join([s+'✅' if s in user_skills else s+'❌' for s in skills])})")
            desc = job.get("description", "")
            if desc:
                lines.append(f"   職務: {desc}")
            lines.append("")
        lines.append("💡 推薦分析:")
        lines.append(f"最佳選擇: {best_job}")
        if match_scores:
            lines.append(f"技能匹配度: {max(match_scores)}%")
        return "\n".join(lines)
