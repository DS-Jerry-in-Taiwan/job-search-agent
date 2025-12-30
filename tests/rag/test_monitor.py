import pytest
from src.rag.monitor import RAGMonitor

def test_latency_and_cache():
    monitor = RAGMonitor()
    monitor.track_latency("embedding", 0.5)
    monitor.track_latency("embedding", 0.7)
    monitor.track_cache(True)
    monitor.track_cache(False)
    monitor.track_cache(True)
    metrics = monitor.export_metrics()
    assert metrics["latency"]["embedding"] == 1.2
    assert 0.6 < metrics["cache_hit_rate"] < 1.0  # 2 hit, 1 miss

def test_quality_and_reset():
    monitor = RAGMonitor()
    monitor.track_quality(0.8)
    monitor.track_quality(0.6)
    metrics = monitor.export_metrics()
    assert abs(metrics["quality_score"] - 0.7) < 1e-6
    monitor.reset()
    metrics2 = monitor.export_metrics()
    assert metrics2["latency"] == {}
    assert metrics2["cache_hit_rate"] == 0.0
    assert metrics2["quality_score"] == 0.0
