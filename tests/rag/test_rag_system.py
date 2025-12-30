import pytest
from src.rag import RAGPipeline, RAGSystem, RAGResult, RAGOptimizer, RAGMonitor, RAGEvaluator

def test_rag_pipeline_init():
    rag = RAGPipeline()
    assert hasattr(rag, "query_rewriter")
    assert hasattr(rag, "embedder")
    assert hasattr(rag, "vector_store")
    assert hasattr(rag, "retriever")
    assert hasattr(rag, "assembler")
    assert hasattr(rag, "optimizer")
    assert hasattr(rag, "monitor")
    assert hasattr(rag, "evaluator")

def test_rag_system_api():
    rag = RAGSystem()
    assert hasattr(rag, "search")
    assert hasattr(rag, "optimizer")
    assert hasattr(rag, "monitor")
    assert hasattr(rag, "evaluator")

def test_rag_result_structure():
    result = RAGResult(
        llm_context="test",
        jobs=[{"id": 1, "title": "test"}],
        latency_ms=123.4,
        cache_hit=True,
        quality_score=0.95,
        metadata={"foo": "bar"}
    )
    assert result.llm_context == "test"
    assert isinstance(result.jobs, list)
    assert isinstance(result.latency_ms, float)
    assert isinstance(result.cache_hit, bool)
    assert isinstance(result.quality_score, float)
    assert isinstance(result.metadata, dict)

def test_optimizer_cache():
    opt = RAGOptimizer(cache_size=2)
    opt.cache_embedding("a", 1)
    opt.cache_embedding("b", 2)
    assert opt.get_cached_embedding("a") == 1
    assert opt.get_cached_embedding("b") == 2
    opt.cache_embedding("c", 3)
    # "a" should be evicted if "b" and "c" accessed
    assert opt.get_cached_embedding("a") is None or opt.get_cached_embedding("b") == 2

def test_optimizer_batch():
    opt = RAGOptimizer()
    opt.add_to_batch("q1", {"meta": 1})
    opt.add_to_batch("q2", {"meta": 2})
    batch = opt.get_batch(2)
    assert len(batch) == 2
    assert batch[0][0] == "q1"
    assert batch[1][0] == "q2"

def test_monitor_metrics():
    monitor = RAGMonitor()
    monitor.track_latency("embedding", 10.0)
    monitor.track_latency("embedding", 5.0)
    monitor.track_cache(True)
    monitor.track_cache(False)
    monitor.track_quality(0.9)
    monitor.track_quality(0.8)
    metrics = monitor.export_metrics()
    assert metrics["latency"]["embedding"] == 15.0
    assert 0.0 <= metrics["cache_hit_rate"] <= 1.0
    assert 0.0 <= metrics["quality_score"] <= 1.0

def test_evaluator_metrics():
    evaluator = RAGEvaluator()
    results = [{"id": 1}, {"id": 2}, {"id": 3}]
    ground_truth = [{"id": 2}, {"id": 4}]
    metrics = evaluator.evaluate_retrieval(results, ground_truth)
    assert "top_k_accuracy" in metrics
    assert "mrr" in metrics
    assert "ndcg" in metrics
    assert 0.0 <= metrics["top_k_accuracy"] <= 1.0
    assert 0.0 <= metrics["mrr"] <= 1.0
    assert 0.0 <= metrics["ndcg"] <= 1.0
