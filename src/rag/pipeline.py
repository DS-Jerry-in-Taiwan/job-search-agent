from typing import Any, Dict, List, Optional
from src.rag.query.rewriter import QueryRewriter
from src.rag.embeddings.manager import EmbeddingManager
from src.rag.vectordb.faiss_store import FaissVectorStore
from src.rag.retrieval.pipeline import RetrievalPipeline
from src.rag.context.assembler import ContextAssembler
from src.rag.optimizer import RAGOptimizer
from src.rag.monitor import RAGMonitor
from src.rag.evaluator import RAGEvaluator

class RAGResult:
    def __init__(
        self,
        llm_context: str,
        jobs: List[Dict[str, Any]],
        latency_ms: float,
        cache_hit: bool,
        quality_score: float,
        metadata: Optional[Dict[str, Any]] = None
    ):
        self.llm_context = llm_context
        self.jobs = jobs
        self.latency_ms = latency_ms
        self.cache_hit = cache_hit
        self.quality_score = quality_score
        self.metadata = metadata or {}

class RAGPipeline:
    def __init__(self):
        self.query_rewriter = QueryRewriter()
        self.embedder = EmbeddingManager()
        # 對齊 embedding 維度
        self.vector_store = FaissVectorStore(dim=1536)
        from src.rag.retrieval.hybrid_retriever import HybridRetriever
        from src.rag.retrieval.reranker import CrossEncoderReranker
        from src.rag.retrieval.bm25_store import BM25Store
        self.retriever = RetrievalPipeline(
            hybrid_retriever=HybridRetriever(
                vector_store=self.vector_store,
                bm25_store=BM25Store(index_path="data/mock/jobs"),
                embedder=self.embedder
            ),
            reranker=CrossEncoderReranker()
        )
        self.assembler = ContextAssembler()
        self.optimizer = RAGOptimizer()
        self.monitor = RAGMonitor()
        self.evaluator = RAGEvaluator()

    def search(self, query: str, user_profile: Dict[str, Any]) -> RAGResult:
        """
        端到端查詢主流程：
        1. 查詢增強（Query Rewriting）
        2. Embedding 快取/計算
        3. 向量查詢與混合檢索（Retriever）
        4. 上下文組裝（Context Assembler）
        5. 優化（Optimizer）、監控（Monitor）、評分（Evaluator）
        6. 回傳標準化 RAGResult 結構
        """
        # 1. 查詢增強
        rewritten_query = self.query_rewriter.rewrite(query)
        # 2. Embedding
        query_embedding = self.embedder.embed_query(rewritten_query)
        # 3. 檢索
        # 傳遞 top_k 參數，避免傳遞 embedding
        retrieved_docs = self.retriever.retrieve(rewritten_query)
        # 4. 上下文組裝
        llm_context = self.assembler.assemble(rewritten_query, retrieved_docs, user_profile)
        # 5. 優化、監控、評分
        optimized_jobs = self.optimizer.optimize(retrieved_docs, user_profile)
        self.monitor.log_query(query, user_profile, retrieved_docs)
        quality_score = self.evaluator.evaluate(llm_context, optimized_jobs)
        # 6. 回傳 RAGResult
        return RAGResult(
            llm_context=llm_context,
            jobs=optimized_jobs,
            latency_ms=0.0,  # TODO: 計算查詢延遲
            cache_hit=False, # TODO: 實作快取判斷
            quality_score=quality_score,
            metadata={"query": rewritten_query}
        )

class RAGSystem(RAGPipeline):
    """對外一鍵調用 API"""
    pass
