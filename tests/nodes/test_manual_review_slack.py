import os
from dotenv import load_dotenv
from src.nodes.manual_review import manual_review_node


def test_manual_review_real_slack():
    """
    真實發送人工審核 payload 到 Slack webhook，需先設定 SLACK_WEBHOOK_URL
    """
    load_dotenv(dotenv_path="./.env")
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    assert webhook_url, "SLACK_WEBHOOK_URL 環境變數未設定"

    state = {
        "system": {
            "current_node": "router",
            "manual_review_reason": "【真實測試】請協助人工審核",
            "extra_info": {"user_id": "U123", "test_case": "test_manual_review_real_slack"},
            "history": [{"node": "conversation", "action": "manual_review"}]
        },
        "conversation": {
            "context": {"user_message": "這是人工審核真實測試"},
            "messages": []
        }
    }

    result = manual_review_node(state)
    # 驗證狀態
    assert result["system"]["current_node"] == "manual_review"
    assert result["system"]["manual_review_status"] == "pending"