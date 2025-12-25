import pytest
from src.rag.query import QueryRewriter, HyDEGenerator
from src.rag.embeddings import EmbeddingManager

@pytest.fixture
def rewriter():
    return QueryRewriter()

@pytest.fixture
def hyde():
    return HyDEGenerator()

@pytest.fixture
def embedder():
    return EmbeddingManager()

def test_query_to_embedding(rewriter, embedder):
    query = "我想找台北的Python工程師工作"
    enhanced = rewriter.rewrite(query)
    vec = embedder.embed_text(enhanced)
    assert isinstance(vec, list)
    assert len(vec) == 1536

def test_hyde_to_embedding(rewriter, hyde, embedder):
    query = "我想找台北的Python工程師工作"
    enhanced = rewriter.rewrite(query)
    hyde_doc = hyde.generate_hypothetical_doc(enhanced)
    vec = embedder.embed_text(hyde_doc)
    assert isinstance(vec, list)
    assert len(vec) == 1536

def test_batch_embedding_integration(rewriter, embedder):
    queries = [
        "我想找台北的Python工程師工作",
        "新竹Java後端工程師工作"
    ]
    enhanced = [rewriter.rewrite(q) for q in queries]
    vecs = embedder.embed_batch(enhanced)
    assert isinstance(vecs, list)
    assert len(vecs) == 2
    assert all(len(v) == 1536 for v in vecs)
