import pytest
from src.rag.retrieval.hybrid_retriever import HybridRetriever

class DummyVectorStore:
    def search(self, query_vec, top_k=10):
        # 回傳固定假資料
        return [{"id": f"vec_{i}", "score": 1.0/(i+1)} for i in range(top_k)]

class DummyBM25Store:
    def search(self, query, top_k=10):
        return [{"id": f"bm25_{i}", "score": 1.0/(i+1)} for i in range(top_k)]

class DummyEmbedder:
    def embed_text(self, query):
        return [0.1, 0.2, 0.3]

def test_hybrid_retrieve_rrf_fuse():
    retriever = HybridRetriever(
        vector_store=DummyVectorStore(),
        bm25_store=DummyBM25Store(),
        embedder=DummyEmbedder(),
        rrf_k=60
    )
    results = retriever.retrieve("test query", top_k=5)
    assert isinstance(results, list)
    assert len(results) == 5
    for doc in results:
        assert "id" in doc
        assert "rrf_score" in doc
        assert isinstance(doc["rrf_score"], float)
