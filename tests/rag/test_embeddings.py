import pytest
from src.rag.embeddings.manager import EmbeddingManager

class DummyEmbeddingManager(EmbeddingManager):
    def __init__(self):
        # 不調用 openai，直接設置參數
        self.model = "dummy"
        self.dimensions = 3

    def embed_text(self, text: str):
        # 回傳固定向量，僅測試資料流
        return [1.0, 2.0, 3.0]

    def embed_batch(self, texts):
        return [[1.0, 2.0, 3.0] for _ in texts]

def test_embed_text():
    em = DummyEmbeddingManager()
    vec = em.embed_text("test query")
    assert isinstance(vec, list)
    assert len(vec) == 3
    assert all(isinstance(x, float) for x in vec)

def test_embed_batch():
    em = DummyEmbeddingManager()
    batch = em.embed_batch(["a", "b", "c"])
    assert isinstance(batch, list)
    assert len(batch) == 3
    for vec in batch:
        assert isinstance(vec, list)
        assert len(vec) == 3
        assert all(isinstance(x, float) for x in vec)
