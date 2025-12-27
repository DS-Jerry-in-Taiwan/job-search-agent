import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.auth.auth_service import register_user, authenticate_user, get_user_by_email
from src.auth.password_handler import hash_password, verify_password
from src.models.database import Base, engine, SessionLocal

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    # 測試前確保資料庫表存在
    Base.metadata.create_all(bind=engine)
    yield
    # 測試後清理資料表
    Base.metadata.drop_all(bind=engine)

def test_register_user():
    # 密碼長度不超過 bcrypt 限制
    user = register_user("test@example.com", "pw123456", "Test User")
    assert user.email == "test@example.com"
    assert user.full_name == "Test User"

def test_register_user_too_long_password():
    # 密碼超過72 bytes應該 raise ValueError
    long_pw = "a" * 73
    with pytest.raises(ValueError):
        register_user("longpw@example.com", long_pw, "Long PW User")

def test_register_user_too_long_password():
    # 密碼超過72 bytes應該 raise ValueError
    long_pw = "a" * 73
    try:
        register_user("longpw@example.com", long_pw, "Long PW User")
        assert False, "Should raise ValueError for password > 72 bytes"
    except ValueError:
        assert True

def test_login_user():
    user = authenticate_user("test@example.com", "pw123456")
    assert user is not None
    assert user.email == "test@example.com"

def test_login_user_too_long_password():
    long_pw = "b" * 73
    user = authenticate_user("test@example.com", long_pw)
    assert user is None

def test_verify_password():
    hashed = hash_password("mypassword")
    assert verify_password("mypassword", hashed)
    assert not verify_password("wrongpassword", hashed)
    # 密碼超過72 bytes驗證應直接回傳False
    long_pw = "b" * 73
    hashed2 = hash_password("shortpw")
    assert not verify_password(long_pw, hashed2)
    with pytest.raises(ValueError):
        hash_password(long_pw)

def test_get_user_by_email():
    user = get_user_by_email("test@example.com")
    assert user is not None
