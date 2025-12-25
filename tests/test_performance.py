"""效能測試套件"""

import pytest
from src.graph import create_workflow
from src.state.operations import create_initial_state
import time
import psutil
import os

def test_workflow_execution_time():
    """測試執行時間 < 5秒"""
    app = create_workflow()
    state = create_initial_state()
    start_time = time.time()
    result = app.invoke(state)
    execution_time = time.time() - start_time
    assert execution_time < 5.0
    print(f"Execution time: {execution_time:.2f}s")

def test_memory_usage():
    """測試記憶體使用 < 100MB"""
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss / 1024 / 1024  # MB
    app = create_workflow()
    state = create_initial_state()
    result = app.invoke(state)
    final_memory = process.memory_info().rss / 1024 / 1024
    memory_used = final_memory - initial_memory
    assert memory_used < 100
    print(f"Memory used: {memory_used:.2f}MB")

def test_throughput():
    """測試吞吐量 > 10 req/sec"""
    app = create_workflow()
    start_time = time.time()
    count = 0
    while time.time() - start_time < 1.0:
        state = create_initial_state()
        app.invoke(state)
        count += 1
    throughput = count
    assert throughput >= 10
    print(f"Throughput: {throughput} req/sec")

def test_latency():
    """測試延遲 < 500ms"""
    app = create_workflow()
    state = create_initial_state()
    start = time.time()
    app.invoke(state)
    latency = (time.time() - start) * 1000
    assert latency < 500
    print(f"Latency: {latency:.2f}ms")

def test_scalability():
    """可擴展性測試（負載增加時效能退化 < 20%）"""
    app = create_workflow()
    # baseline
    state = create_initial_state()
    start = time.time()
    app.invoke(state)
    base_time = time.time() - start

    # 增加負載
    states = [create_initial_state() for _ in range(20)]
    start = time.time()
    for s in states:
        app.invoke(s)
    multi_time = (time.time() - start) / 20

    degradation = (multi_time - base_time) / base_time if base_time > 0 else 0
    assert degradation < 0.2
    print(f"Scalability degradation: {degradation:.2%}")
