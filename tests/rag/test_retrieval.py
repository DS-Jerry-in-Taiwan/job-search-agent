import pytest
from src.rag.retrieval.bm25_store import BM25Store
from src.rag.retrieval.hybrid_retriever import HybridRetriever
from src.rag.retrieval.reranker import CrossEncoderReranker
from src.rag.retrieval.pipeline import RetrievalPipeline

class DummyVectorStore:
    def __init__(self):
        self.docs = []
    def add(self, vecs, metas):
        for i, meta in enumerate(metas):
            self.docs.append({"id": meta["id"], "content": meta["content"], "metadata": meta})
    def search(self, query_vec, top_k=10):
        # Return all docs with dummy score
        return [{"id": d["id"], "score": 1.0, "content": d["content"], "metadata": d["metadata"]} for d in self.docs][:top_k]

class DummyEmbedder:
    def embed_text(self, text):
        return [0.0] * 8

@pytest.fixture(scope="module")
def bm25_store(tmp_path_factory):
    idx_path = tmp_path_factory.mktemp("bm25_idx")
    store = BM25Store(str(idx_path))
    docs = [
        {"id": "1", "content": "Python backend developer in Taipei", "metadata": {"lang": "en"}},
        {"id": "2", "content": "台北 Python 後端工程師", "metadata": {"lang": "zh"}},
        {"id": "3", "content": "Data scientist, NLP, ML", "metadata": {"lang": "en"}},
    ]
    store.add_documents(docs)
    return store

def test_bm25_search(bm25_store):
    results = bm25_store.search("Python", top_k=2)
    assert len(results) == 2
    assert any("Python" in r["content"] for r in results)

def test_bm25_filter(bm25_store):
    results = bm25_store.search("Python", top_k=2, filters={"lang": "zh"})
    assert len(results) == 1
    assert results[0]["metadata"]["lang"] == "zh"

def test_rrf_fusion_math():
    dummy_vec = [{"id": "1"}, {"id": "2"}, {"id": "3"}]
    dummy_bm25 = [{"id": "2"}, {"id": "3"}, {"id": "4"}]
    retriever = HybridRetriever(None, None, None)
    fused = retriever._rrf_fuse(dummy_vec, dummy_bm25)
    ids = [d["id"] for d in fused]
    assert ids[0] == "2"  # Appears in both, should have highest score

def test_hybrid_retrieval_end2end(bm25_store):
    vector_store = DummyVectorStore()
    embedder = DummyEmbedder()
    # Add docs to vector store
    for doc in bm25_store.search("Python", top_k=3):
        vector_store.docs.append(doc)
    retriever = HybridRetriever(vector_store, bm25_store, embedder)
    results = retriever.retrieve("Python", top_k=2)
    assert len(results) == 2

def test_cross_encoder_rerank(monkeypatch):
    class DummyCE:
        def predict(self, pairs):
            return [float(i) for i in range(len(pairs))]
    reranker = CrossEncoderReranker()
    reranker.model = DummyCE()
    docs = [{"id": str(i), "content": f"doc{i}"} for i in range(5)]
    reranked = reranker.rerank("query", docs, top_k=3)
    assert len(reranked) == 3
    assert reranked[0]["ce_score"] > reranked[1]["ce_score"]

def test_retrieval_pipeline(monkeypatch, bm25_store):
    class DummyCE:
        def predict(self, pairs):
            return [float(i) for i in range(len(pairs))]
    vector_store = DummyVectorStore()
    embedder = DummyEmbedder()
    for doc in bm25_store.search("Python", top_k=3):
        vector_store.docs.append(doc)
    retriever = HybridRetriever(vector_store, bm25_store, embedder)
    reranker = CrossEncoderReranker()
    reranker.model = DummyCE()
    pipeline = RetrievalPipeline(retriever, reranker)
    results = pipeline.retrieve("Python", top_k=2)
    assert len(results) == 2
    assert "ce_score" in results[0]

def test_empty_query_handling(bm25_store):
    results = bm25_store.search("", top_k=2)
    assert isinstance(results, list)

def test_large_scale_retrieval(tmp_path_factory):
    idx_path = tmp_path_factory.mktemp("bm25_large")
    store = BM25Store(str(idx_path))
    docs = [{"id": str(i), "content": f"doc{i}", "metadata": {}} for i in range(100)]
    store.add_documents(docs)
    results = store.search("doc", top_k=10)
    assert len(results) == 10

def test_score_consistency(monkeypatch):
    class DummyCE:
        def predict(self, pairs):
            return [1.0 for _ in pairs]
    reranker = CrossEncoderReranker()
    reranker.model = DummyCE()
    docs = [{"id": str(i), "content": f"doc{i}"} for i in range(5)]
    reranked = reranker.rerank("query", docs, top_k=5)
    scores = [d["ce_score"] for d in reranked]
    assert all(s == 1.0 for s in scores)
