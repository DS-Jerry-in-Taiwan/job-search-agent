import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_health():
    resp = client.get("/api/v1/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok", "version": "0.1.0"}

def test_chat():
    resp = client.post(
        "/api/v1/chat",
        json={"session_id": "test", "message": "你好"}
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "reply" in data and "你好" in data["reply"]

def test_graph_visualize():
    resp = client.get("/api/v1/graph/visualize")
    assert resp.status_code == 200
    data = resp.json()
    assert "graph_svg" in data and "nodes" in data and "edges" in data

def test_session_history():
    resp = client.get("/api/v1/session/test/history")
    assert resp.status_code == 200
    data = resp.json()
    assert data["session_id"] == "test"
    assert isinstance(data["history"], list)
