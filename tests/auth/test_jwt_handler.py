import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.auth.jwt_handler import create_access_token, verify_token

def test_create_access_token():
    token = create_access_token(1)
    assert isinstance(token, str)
    assert len(token) > 0

def test_verify_token():
    token = create_access_token(1)
    user_id = verify_token(token)
    assert user_id == 1

def test_expired_token():
    # 測試過期 Token（略，需 mock datetime 或設短效期）
    pass
