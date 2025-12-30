import pytest
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_graph_visualize_svg_and_structure():
    resp = client.get("/api/v1/graph/visualize")
    assert resp.status_code == 200
    data = resp.json()
    # SVG 應為字串且含 <svg>
    assert "graph_svg" in data and "<svg" in data["graph_svg"]
    # nodes/edges 應為 list
    assert isinstance(data.get("nodes"), list)
    assert isinstance(data.get("edges"), list)
