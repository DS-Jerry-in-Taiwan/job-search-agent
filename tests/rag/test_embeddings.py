import pytest
from src.rag.embeddings import EmbeddingManager, TextChunker, EmbeddingCache

@pytest.fixture
def embedder():
    return EmbeddingManager()

@pytest.fixture
def chunker():
    return TextChunker()

@pytest.fixture
def cache():
    return EmbeddingCache(max_size=3)

def test_embedding_manager_init(embedder):
    assert embedder.model == "text-embedding-3-small"
    assert embedder.dimensions == 1536

def test_embed_text(embedder):
    vec = embedder.embed_text("Hello world")
    assert isinstance(vec, list)
    assert len(vec) == 1536

def test_embed_batch(embedder):
    texts = ["Hello", "world"]
    vecs = embedder.embed_batch(texts)
    assert isinstance(vecs, list)
    assert len(vecs) == 2
    assert all(len(v) == 1536 for v in vecs)

def test_text_chunker(chunker):
    text = "這是一段很長的文本。" * 100
    chunks = chunker.chunk_text(text)
    assert isinstance(chunks, list)
    assert len(chunks) > 1

def test_chunk_overlap(chunker):
    text = "這是一段很長的文本。" * 100
    chunks = chunker.chunk_text(text)
    assert len(chunks) > 1
    # 檢查重疊
    assert any(chunks[i][-10:] in chunks[i+1] for i in range(len(chunks)-1))

def test_embedding_cache_set_get(cache):
    cache.set("foo", [1.0, 2.0])
    assert cache.get("foo") == [1.0, 2.0]

def test_embedding_cache_lru(cache):
    cache.set("a", [1])
    cache.set("b", [2])
    cache.set("c", [3])
    cache.set("d", [4])  # 觸發淘汰
    assert cache.get("a") is None
    assert cache.get("b") == [2]
    assert cache.get("d") == [4]

def test_embedding_cache_clear(cache):
    cache.set("foo", [1.0, 2.0])
    cache.clear()
    assert cache.get("foo") is None
