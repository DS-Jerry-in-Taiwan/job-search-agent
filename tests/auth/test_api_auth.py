import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from fastapi.testclient import TestClient
from api.server import app
from src.models.database import Base, engine

import pytest

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    # 測試前確保資料庫表存在
    Base.metadata.create_all(bind=engine)
    yield
    # 測試後清理資料表
    Base.metadata.drop_all(bind=engine)

client = TestClient(app)

def test_register_endpoint():
    # 密碼長度不超過 bcrypt 限制
    response = client.post("/api/auth/register", json={
        "email": "newuser@example.com",
        "password": "pw123456",
        "full_name": "New User"
    })
    print(response.status_code, response.text)
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_register_endpoint_too_long_password():
    # 密碼超過72 bytes應該回傳 422 或 400
    long_pw = "a" * 73
    response = client.post("/api/auth/register", json={
        "email": "longpw@example.com",
        "password": long_pw,
        "full_name": "Long PW User"
    })
    assert response.status_code in (400, 422)

def test_login_endpoint():
    response = client.post("/api/auth/login", json={
        "email": "newuser@example.com",
        "password": "pw123456"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_endpoint_too_long_password():
    long_pw = "b" * 73
    response = client.post("/api/auth/login", json={
        "email": "newuser@example.com",
        "password": long_pw
    })
    assert response.status_code in (400, 401, 422)

def test_get_current_user():
    login_response = client.post("/api/auth/login", json={
        "email": "newuser@example.com",
        "password": "pw123456"
    })
    token = login_response.json()["access_token"]
    response = client.get("/api/auth/me", params={"token": token})
    assert response.status_code == 200
    assert response.json()["email"] == "newuser@example.com"

def test_unauthorized_access():
    response = client.get("/api/auth/me")
    assert response.status_code == 422 or response.status_code == 401

def test_invalid_token():
    response = client.get("/api/auth/me", params={"token": "invalid_token"})
    assert response.status_code == 401 or response.status_code == 422
