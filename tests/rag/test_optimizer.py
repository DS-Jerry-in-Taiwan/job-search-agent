import pytest
from src.rag.optimizer import RAGOptimizer

def test_lru_cache_basic():
    opt = RAGOptimizer(cache_size=3)
    opt.cache_embedding("a", [1])
    opt.cache_embedding("b", [2])
    opt.cache_embedding("c", [3])
    assert opt.get_cached_embedding("a") == [1]
    opt.cache_embedding("d", [4])
    # "b" 應被淘汰
    assert opt.get_cached_embedding("b") is None
    assert opt.get_cached_embedding("c") == [3]
    assert opt.get_cached_embedding("d") == [4]

def test_cache_hit_rate():
    opt = RAGOptimizer(cache_size=2)
    opt.cache_embedding("x", 1)
    opt.cache_embedding("y", 2)
    _ = opt.get_cached_embedding("x")
    _ = opt.get_cached_embedding("y")
    _ = opt.get_cached_embedding("z")
    rate = opt.cache_hit_rate()
    assert 0.6 < rate < 1.0  # 2 hit, 1 miss

def test_batch_queue():
    opt = RAGOptimizer()
    opt.add_to_batch("q1", {"meta": 1})
    opt.add_to_batch("q2", {"meta": 2})
    batch = opt.get_batch(batch_size=1)
    assert len(batch) == 1
    assert batch[0][0] == "q1"
    assert batch[0][1]["meta"] == 1
    batch2 = opt.get_batch(batch_size=2)
    assert len(batch2) == 1
    assert batch2[0][0] == "q2"
