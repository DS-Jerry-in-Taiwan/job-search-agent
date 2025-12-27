from typing import Dict, List
from src.agent import AgentBase, Tool, Memory

# Placeholder for RAGSystem and LLMClient
try:
    from src.rag import RAGSystem
except ImportError:
    RAGSystem = None
try:
    from src.llm import LLMClient
except ImportError:
    LLMClient = None

class JobSearchAgent(AgentBase):
    def __init__(self):
        rag = RAGSystem() if RAGSystem else None
        tools = [
            Tool(
                "search_jobs",
                rag.search if rag else lambda query, user_profile: [],
                "Search job postings",
                {"query": (str, ...), "user_profile": (dict, ...)}
            ),
            Tool("calculate_match", self._calc_match, "Calculate match score", {"job": (dict, ...), "profile": (dict, ...)}),
            Tool("filter_jobs", self._filter, "Filter jobs by criteria", {"jobs": (list, ...), "criteria": (dict, ...)}),
        ]
        super().__init__("JobSearchAgent", tools, Memory())
        self.llm = LLMClient() if LLMClient else None

    def _calc_match(self, job: Dict, profile: Dict) -> float:
        # Dummy match score calculation
        return 1.0

    def _filter(self, jobs: List[Dict], criteria: Dict) -> List[Dict]:
        # Dummy filter logic
        return jobs

    def run(self, task: str, context: Dict) -> str:
        profile = context.get("profile", {})
        jobs_result = self.call_tool("search_jobs", query=task, user_profile=profile)
        # RAGResult 可能不是 list，需轉換
        jobs = []
        if hasattr(jobs_result, "jobs"):
            jobs = jobs_result.jobs
        elif isinstance(jobs_result, list):
            jobs = jobs_result
        matched_jobs = [
            {**job, "match_score": self.call_tool("calculate_match", job=job, profile=profile)}
            for job in jobs
        ]
        top_jobs = sorted(matched_jobs, key=lambda x: x.get("match_score", 0), reverse=True)[:5]
        response = (
            self.llm.chat(f"找到職缺: {top_jobs}, 生成友善回覆") if self.llm else str(top_jobs)
        )
        self.remember(f"user: {task}")
        self.remember(f"assistant: {response}")
        return response
