from .base_provider import BaseProvider
import json
import random

class MockProvider(BaseProvider):
    def fetch_jobs(self, count=50, high=20, mid=20, low=10):
        """生成 Mock 職缺數據，匹配度分布：高20/中20/低10"""
        jobs = []
        candidate_skills = [
            "Python", "SQL", "PyTorch", "TensorFlow", "Docker", "Kubernetes"
        ]
        llm_skills = [
            "LangChain", "LlamaIndex", "RAG", "OpenAI API", "Prompt Engineering", "Vector DB", "ElasticSearch"
        ]
        # 高匹配度
        for i in range(1, high+1):
            max_overlap = min(6, len(candidate_skills), 10, 10)
            min_overlap = max(1, 10 - len(llm_skills))
            if min_overlap > max_overlap:
                overlap = min(len(candidate_skills), 10)
            else:
                overlap = random.randint(min_overlap, max_overlap)
            overlap = max(0, min(overlap, len(candidate_skills)))
            required = random.sample(candidate_skills, overlap) if overlap > 0 else []
            llm_count = max(0, min(len(llm_skills), 10 - overlap))
            if llm_count > 0:
                required += random.sample(llm_skills, llm_count)
            jobs.append({
                "id": f"job_{i:03d}",
                "title": f"Senior AI Engineer {i}",
                "company": f"TechCorp {i}",
                "description": "負責開發 AI 相關產品與技術",
                "requirements": required,
                "location": "台北市/新竹/遠端",
                "salary_range": "120-200萬/年",
                "employment_type": "全職",
                "match_score": round(overlap / 10, 2),
                "match_reasons": ["技能高度重疊"]
            })
        # 中匹配度
        for i in range(high+1, high+mid+1):
            max_overlap = min(4, len(candidate_skills), 10, 10)
            min_overlap = max(1, 10 - len(llm_skills))
            if min_overlap > max_overlap:
                overlap = min(len(candidate_skills), 10)
            else:
                overlap = random.randint(min_overlap, max_overlap)
            overlap = max(0, min(overlap, len(candidate_skills)))
            required = random.sample(candidate_skills, overlap) if overlap > 0 else []
            llm_count = max(0, min(len(llm_skills), 10 - overlap))
            if llm_count > 0:
                required += random.sample(llm_skills, llm_count)
            jobs.append({
                "id": f"job_{i:03d}",
                "title": f"AI Engineer {i}",
                "company": f"StartupCo {i}",
                "description": "參與 AI 專案開發",
                "requirements": required,
                "location": "台北市/台中/遠端",
                "salary_range": "90-150萬/年",
                "employment_type": "全職",
                "match_score": round(overlap / 10, 2),
                "match_reasons": ["部分技能重疊"]
            })
        # 低匹配度
        for i in range(high+mid+1, count+1):
            max_overlap = min(2, len(candidate_skills), 10, 10)
            min_overlap = max(1, 10 - len(llm_skills))
            if min_overlap > max_overlap:
                overlap = min(len(candidate_skills), 10)
            else:
                overlap = random.randint(min_overlap, max_overlap)
            overlap = max(0, min(overlap, len(candidate_skills)))
            required = random.sample(candidate_skills, overlap) if overlap > 0 else []
            llm_count = max(0, min(len(llm_skills), 10 - overlap))
            if llm_count > 0:
                required += random.sample(llm_skills, llm_count)
            jobs.append({
                "id": f"job_{i:03d}",
                "title": f"Junior AI Developer {i}",
                "company": f"Company {i}",
                "description": "協助開發 AI 功能",
                "requirements": required,
                "location": "台北市/遠端",
                "salary_range": "60-100萬/年",
                "employment_type": "全職",
                "match_score": round(overlap / 10, 2),
                "match_reasons": ["技能重疊較低"]
            })
        with open("data/mock/jobs/mock_jobs.json", "w", encoding="utf-8") as f:
            json.dump(jobs, f, ensure_ascii=False, indent=2)
        return jobs

# 預留未來擴展
# class CrawlerProvider(BaseProvider):
#     def fetch_jobs(self, **kwargs):
#         raise NotImplementedError("Phase 5 實現")
