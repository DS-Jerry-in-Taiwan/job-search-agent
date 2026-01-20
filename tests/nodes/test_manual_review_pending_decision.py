import os
import json
from dotenv import load_dotenv
import pytest

from src.nodes.manual_review import manual_review_node

# 假設 decision_node 在 src/nodes/decision.py
from src.nodes.decision import decision_node

def test_manual_review_to_decision_pending(capsys):
    """
    測試 workflow 進入 manual_review，然後 decision_node 偵測到 pending 並正確處理
    """
    # 載入 .env，確保 webhook 可用
    load_dotenv(dotenv_path="./.env")
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    assert webhook_url, "SLACK_WEBHOOK_URL 環境變數未設定"

    # Step 1: 先進入 manual_review_node
    state = {
        "system": {
            "current_node": "router",
            "manual_review_reason": "【測試】請協助人工審核AAA",
            "extra_info": {"user_id": "U456", "test_case": "test_manual_review_to_decision_pending"},
            "history": [{"node": "conversation", "action": "manual_review"}]
        },
        "conversation": {
            "context": {"user_message": "這是人工審核測試AAA"},
            "messages": []
        }
    }
    state = manual_review_node(state)
    assert state["system"]["current_node"] == "manual_review"
    assert state["system"]["manual_review_status"] == "pending"

    # Step 2: 回到 decision_node，驗證 pending 狀態下的行為
    result = decision_node(state)
    # 驗證 decision_node 有正確回應
    assert result["conversation"]["messages"][-1]["content"] == "請稍候，人工審核中，審核完成後會自動通知您。"
    # 你也可以驗證 state 沒有被不當修改
    assert result["system"]["manual_review_status"] == "pending"