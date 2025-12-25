from typing import Any, Dict, List

class RetrievalPipeline:
    """
    檢索管線，整合 HybridRetriever、CrossEncoderReranker，端到端檢索流程。
    """

    def __init__(self, hybrid_retriever, reranker) -> None:
        self.hybrid_retriever = hybrid_retriever
        self.reranker = reranker

    def retrieve(self, query: str, top_k: int = 10) -> List[Dict[str, Any]]:
        # 先混合檢索
        hybrid_results = self.hybrid_retriever.retrieve(query, top_k=top_k*5)
        # 再 CrossEncoder 重排序
        reranked = self.reranker.rerank(query, hybrid_results, top_k=top_k)
        return reranked
