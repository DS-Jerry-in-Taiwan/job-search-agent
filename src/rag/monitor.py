from typing import Dict, Any
import time
import threading

class RAGMonitor:
    def __init__(self):
        self.metrics: Dict[str, float] = {}
        self.cache_hit = 0
        self.cache_total = 0
        self.quality_scores = []
        self.lock = threading.Lock()

    def track_latency(self, stage: str, duration: float):
        with self.lock:
            self.metrics[stage] = self.metrics.get(stage, 0.0) + duration

    def track_cache(self, hit: bool):
        with self.lock:
            self.cache_total += 1
            if hit:
                self.cache_hit += 1

    def track_quality(self, score: float):
        with self.lock:
            self.quality_scores.append(score)

    def export_metrics(self) -> Dict[str, Any]:
        with self.lock:
            avg_quality = sum(self.quality_scores) / len(self.quality_scores) if self.quality_scores else 0.0
            cache_hit_rate = self.cache_hit / self.cache_total if self.cache_total else 0.0
            return {
                "latency": dict(self.metrics),
                "cache_hit_rate": cache_hit_rate,
                "quality_score": avg_quality,
            }

    def log_query(self, query: str, user_profile: Dict[str, Any], retrieved_docs: Any):
        # 目前僅簡單記錄查詢，可擴充為詳細日誌或監控
        print(f"[RAGMonitor] Query: {query} | User: {user_profile} | Retrieved: {len(retrieved_docs) if hasattr(retrieved_docs, '__len__') else 'N/A'}")

    def reset(self):
        with self.lock:
            self.metrics.clear()
            self.cache_hit = 0
            self.cache_total = 0
            self.quality_scores.clear()
