from typing import Dict, Optional

DEFAULT_ROUTING_RULES = {
    "search_job": "JobSearchAgent",
    "analyze_salary": "SalaryAnalyzerAgent",
    "interview_prep": "InterviewCoachAgent",
    "optimize_resume": "ResumeOptimizerAgent",
}

class AgentRouter:
    def __init__(self, routing_rules: Dict[str, str] = None):
        self.routing_rules = routing_rules or DEFAULT_ROUTING_RULES

    def route_rule_based(self, intent: str) -> Optional[str]:
        return self.routing_rules.get(intent)

    def route_llm_based(self, intent: str) -> str:
        # LLM 路由邏輯（預留）
        return self.routing_rules.get(intent, "JobSearchAgent")

    def route(self, intent: str) -> str:
        # 混合路由：先規則，失敗用 LLM
        agent = self.route_rule_based(intent)
        if agent:
            return agent
        return self.route_llm_based(intent)
