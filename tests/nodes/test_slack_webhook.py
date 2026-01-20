import os
import requests

def test_send_slack_webhook():
    webhook_url = os.getenv("SLACK_WEBHOOK_URL")
    assert webhook_url, "SLACK_WEBHOOK_URL 環境變數未設定"
    payload = {
        "text": "【測試通知】這是來自 job_search_agent 的 Slack webhook 單元測試訊息。"
    }
    response = requests.post(webhook_url, json=payload)
    assert response.status_code == 200
