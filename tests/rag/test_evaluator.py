import pytest
from src.rag.evaluator import RAGEvaluator

def test_evaluate_retrieval():
    evaluator = RAGEvaluator()
    results = [
        {"id": "a"}, {"id": "b"}, {"id": "c"}
    ]
    ground_truth = [
        {"id": "b"}, {"id": "d"}
    ]
    metrics = evaluator.evaluate_retrieval(results, ground_truth)
    assert 0.0 <= metrics["top_k_accuracy"] <= 1.0
    assert 0.0 <= metrics["mrr"] <= 1.0
    assert 0.0 <= metrics["ndcg"] <= 1.0
    # b 在第2個，MRR=1/2
    assert abs(metrics["mrr"] - 0.5) < 1e-6

def test_empty_results():
    evaluator = RAGEvaluator()
    metrics = evaluator.evaluate_retrieval([], [])
    assert metrics["top_k_accuracy"] == 0.0
    assert metrics["mrr"] == 0.0
    assert metrics["ndcg"] == 0.0

def test_calculate_metrics():
    evaluator = RAGEvaluator()
    evaluator.metrics = {"top_k_accuracy": 0.8, "mrr": 0.7, "ndcg": 0.6}
    m = evaluator.calculate_metrics()
    assert m["top_k_accuracy"] == 0.8
    assert m["mrr"] == 0.7
    assert m["ndcg"] == 0.6
