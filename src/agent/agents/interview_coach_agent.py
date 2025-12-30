from typing import Dict, List
from src.agent import AgentBase, Tool, Memory

class InterviewCoachAgent(AgentBase):
    def __init__(self):
        tools = [
            Tool("generate_questions", self._generate_questions, "Generate interview questions", {}),
            Tool("evaluate_skills", self._evaluate_skills, "Evaluate skill readiness", {}),
            Tool("suggest_prep", self._suggest_prep, "Preparation suggestions", {})
        ]
        super().__init__("InterviewCoachAgent", tools, Memory())

    def _generate_questions(self, job_title: str = "", tech_stack: List[str] = None) -> List[str]:
        tech_stack = tech_stack or []
        return [f"請解釋 {tech} 的核心概念" for tech in tech_stack][:10]

    def _evaluate_skills(self, user_skills: List[str] = None, required_skills: List[str] = None) -> Dict:
        user_skills = set(user_skills or [])
        required_skills = set(required_skills or [])
        gaps = list(required_skills - user_skills)
        return {"gaps": gaps, "score": len(user_skills & required_skills) / max(len(required_skills), 1)}

    def _suggest_prep(self, gaps: List[str] = None) -> str:
        gaps = gaps or []
        if not gaps:
            return "技能準備充分，可直接面試。"
        return f"建議加強以下技能：{', '.join(gaps)}"

    def run(self, task: str, context: Dict) -> str:
        questions = self.call_tool("generate_questions", job_title=context.get("job_title", ""), tech_stack=context.get("tech_stack", []))
        eval_result = self.call_tool("evaluate_skills", user_skills=context.get("user_skills", []), required_skills=context.get("required_skills", []))
        prep_suggestion = self.call_tool("suggest_prep", gaps=eval_result.get("gaps", []))
        self.remember(f"user: {task}")
        self.remember(f"assistant: {prep_suggestion}")
        return prep_suggestion
