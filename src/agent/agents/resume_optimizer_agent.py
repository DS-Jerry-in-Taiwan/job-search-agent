from typing import Dict, List
from src.agent import AgentBase, Tool, Memory

class ResumeOptimizerAgent(AgentBase):
    def __init__(self):
        tools = [
            Tool("analyze_resume", self._analyze_resume, "Analyze resume", {}),
            Tool("extract_keywords", self._extract_keywords, "Extract keywords", {}),
            Tool("identify_gaps", self._identify_gaps, "Identify skill gaps", {}),
            Tool("suggest_improvements", self._suggest_improvements, "Suggest improvements", {})
        ]
        super().__init__("ResumeOptimizerAgent", tools, Memory())

    def _analyze_resume(self, resume_text: str = "") -> Dict:
        # Dummy resume analysis
        return {"length": len(resume_text), "sections": ["Education", "Experience", "Skills"]}

    def _extract_keywords(self, resume_text: str = "") -> List[str]:
        # Dummy keyword extraction
        return ["Python", "Machine Learning", "SQL"]

    def _identify_gaps(self, resume_keywords: List[str] = None, job_requirements: List[str] = None) -> List[str]:
        resume_keywords = set(resume_keywords or [])
        job_requirements = set(job_requirements or [])
        return list(job_requirements - resume_keywords)

    def _suggest_improvements(self, gaps: List[str] = None) -> str:
        gaps = gaps or []
        if not gaps:
            return "履歷已符合目標職缺要求。"
        return f"建議補充以下技能或經驗：{', '.join(gaps)}"

    def run(self, task: str, context: Dict) -> str:
        analysis = self.call_tool("analyze_resume", resume_text=context.get("resume_text", ""))
        keywords = self.call_tool("extract_keywords", resume_text=context.get("resume_text", ""))
        gaps = self.call_tool("identify_gaps", resume_keywords=keywords, job_requirements=context.get("job_requirements", []))
        improvement = self.call_tool("suggest_improvements", gaps=gaps)
        self.remember(f"user: {task}")
        self.remember(f"assistant: {improvement}")
        return improvement
