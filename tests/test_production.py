import pytest
import requests
from fastapi.testclient import TestClient
from api.server import app

client = TestClient(app)

class TestAPI:
    def test_health_endpoint(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"

    def test_chat_endpoint(self):
        response = client.post("/api/chat", json={
            "message": "找台北 Python 工作",
            "user_profile": {"skills": ["Python"], "experience_years": 3}
        })
        assert response.status_code == 200
        assert "response" in response.json()

    def test_search_endpoint(self):
        response = client.get("/api/search?query=Python")
        assert response.status_code == 200

    def test_analyze_endpoint(self):
        response = client.post("/api/analyze", json={
            "job_title": "Python 後端",
            "experience": 3
        })
        assert response.status_code == 200

class TestDeployment:
    def test_docker_build(self):
        # 測試 Docker build
        pass

    def test_docker_deployment(self):
        # 測試 Docker 部署
        pass

    def test_health_check(self):
        response = requests.get("http://localhost:8000/health")
        assert response.status_code == 200
