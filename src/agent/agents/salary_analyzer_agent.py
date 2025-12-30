from typing import Dict
from src.agent import AgentBase, Tool, Memory

class SalaryAnalyzerAgent(AgentBase):
    def __init__(self):
        tools = [
            Tool("analyze_range", self._analyze_range, "Analyze salary range", {}),
            Tool("predict_salary", self._predict_salary, "Predict user salary", {}),
            Tool("suggest_negotiation", self._suggest_negotiation, "Negotiation advice", {})
        ]
        super().__init__("SalaryAnalyzerAgent", tools, Memory())

    def _analyze_range(self, job_title: str = "", location: str = "") -> Dict:
        # Dummy salary range analysis
        return {"min": 80, "p25": 120, "median": 150, "p75": 180, "max": 250}

    def _predict_salary(self, job_title: str = "", experience: int = 0) -> int:
        base = 100
        return int(base * (1 + experience * 0.1))

    def _suggest_negotiation(self, predicted: int = 0, market_range: Dict = None) -> str:
        # Dummy negotiation advice
        return "建議：根據市場行情，爭取 median ~ p75 薪資。"

    def run(self, task: str, context: Dict) -> str:
        range_info = self.call_tool("analyze_range", job_title=context.get("job_title", ""), location=context.get("location", ""))
        predicted = self.call_tool("predict_salary", job_title=context.get("job_title", ""), experience=context.get("experience", 0))
        advice = self.call_tool("suggest_negotiation", predicted=predicted, market_range=range_info)
        self.remember(f"user: {task}")
        self.remember(f"assistant: {advice}")
        return advice
