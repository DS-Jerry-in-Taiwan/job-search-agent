from typing import List, Dict, Any
from sentence_transformers import CrossEncoder

class CrossEncoderReranker:
    """
    CrossEncoder 重排序器，基於 sentence-transformers cross-encoder。
    """

    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2") -> None:
        self.model = CrossEncoder(model_name)

    def rerank(self, query: str, docs: List[Dict[str, Any]], top_k: int = 10) -> List[Dict[str, Any]]:
        # 準備查詢-文件對
        pairs = [(query, doc["content"]) for doc in docs]
        scores = self.model.predict(pairs)
        for doc, score in zip(docs, scores):
            doc["ce_score"] = float(score)
        # 依分數排序
        sorted_docs = sorted(docs, key=lambda d: -d["ce_score"])
        return sorted_docs[:top_k]
