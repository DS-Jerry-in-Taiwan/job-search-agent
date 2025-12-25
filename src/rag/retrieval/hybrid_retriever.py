from typing import List, Dict, Any, Optional
import numpy as np

class HybridRetriever:
    """
    混合檢索器：向量檢索 + BM25 關鍵字檢索 + RRF 融合。
    """

    def __init__(self, vector_store, bm25_store, embedder, rrf_k: int = 60) -> None:
        self.vector_store = vector_store
        self.bm25_store = bm25_store
        self.embedder = embedder
        self.rrf_k = rrf_k

    def retrieve(self, query: str, top_k: int = 10, vector_top_k: int = 50, bm25_top_k: int = 50) -> List[Dict[str, Any]]:
        # 向量檢索
        query_vec = self.embedder.embed_text(query)
        vector_results = self.vector_store.search(query_vec, top_k=vector_top_k)
        # BM25 檢索
        bm25_results = self.bm25_store.search(query, top_k=bm25_top_k)
        # RRF 融合
        fused = self._rrf_fuse(vector_results, bm25_results)
        return fused[:top_k]

    def _rrf_fuse(self, vector_results: List[Dict[str, Any]], bm25_results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        # RRF 融合公式: score = Σ(1/(k+rank)), k=60
        doc_scores = {}
        doc_map = {}
        for rank, doc in enumerate(vector_results):
            doc_id = doc["id"]
            doc_scores.setdefault(doc_id, 0)
            doc_scores[doc_id] += 1.0 / (self.rrf_k + rank + 1)
            doc_map[doc_id] = doc
        for rank, doc in enumerate(bm25_results):
            doc_id = doc["id"]
            doc_scores.setdefault(doc_id, 0)
            doc_scores[doc_id] += 1.0 / (self.rrf_k + rank + 1)
            # 若向量結果無 metadata，補上
            if doc_id not in doc_map:
                doc_map[doc_id] = doc
        # 排序
        sorted_docs = sorted(doc_scores.items(), key=lambda x: -x[1])
        results = []
        for doc_id, score in sorted_docs:
            doc = dict(doc_map[doc_id])
            doc["rrf_score"] = score
            results.append(doc)
        return results
