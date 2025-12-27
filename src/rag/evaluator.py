from typing import List, Dict, Any
import math

class RAGEvaluator:
    def __init__(self):
        self.metrics: Dict[str, float] = {}

    def evaluate(self, llm_context, jobs):
        # 目前僅回傳預設分數，未來可擴充評分邏輯
        return 1.0

    def evaluate_retrieval(self, results: List[Dict[str, Any]], ground_truth: List[Dict[str, Any]]) -> Dict[str, float]:
        # Top-K accuracy
        gt_ids = set([item.get("id") for item in ground_truth])
        retrieved_ids = [item.get("id") for item in results]
        top_k = len(results)
        hit = sum(1 for rid in retrieved_ids if rid in gt_ids)
        top_k_acc = hit / top_k if top_k else 0.0

        # MRR
        mrr = 0.0
        for i, rid in enumerate(retrieved_ids):
            if rid in gt_ids:
                mrr = 1.0 / (i + 1)
                break

        # NDCG
        dcg = 0.0
        idcg = 0.0
        for i, rid in enumerate(retrieved_ids):
            rel = 1 if rid in gt_ids else 0
            dcg += (2 ** rel - 1) / math.log2(i + 2)
        for i in range(min(len(gt_ids), top_k)):
            idcg += 1 / math.log2(i + 2)
        ndcg = dcg / idcg if idcg > 0 else 0.0

        self.metrics = {
            "top_k_accuracy": top_k_acc,
            "mrr": mrr,
            "ndcg": ndcg
        }
        return self.metrics

    def calculate_metrics(self) -> Dict[str, float]:
        return dict(self.metrics)
