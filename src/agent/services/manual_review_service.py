import requests
import os
import json
from datetime import datetime
from typing import Dict, Any

def process_manual_review(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    處理人工審核邏輯，發送 Slack 通知，更新狀態
    """
    SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
 
    workflow_history = state.get("system", {}).get("history", [])
    current_node = state.get("system", {}).get("current_node", "")
    issue = (
        state.get("system", {}).get("manual_review_reason") or
        state.get("system", {}).get("error_message") or
        state.get("conversation", {}).get("context", {}).get("user_message", "需要人工審核")
    )
    requirement = state.get("system", {}).get("manual_review_reason", "請協助處理此用戶需求")
    extra_info = state.get("system", {}).get("extra_info", {})
    
    slack_message = {
        "text": "[人工審核通知]",
        "blocks": [
            {"type": "section", "text": {"type": "mrkdwn", "text": "*[人工審核通知]*"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": f"*目前節點：* `{current_node}`"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": f"*流程歷程：*\n```{json.dumps(workflow_history, ensure_ascii=False, indent=2)}```"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": f"*問題描述：*\n{issue}"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": f"*需求說明：*\n{requirement}"}},
            {"type": "section", "text": {"type": "mrkdwn", "text": f"*擴充資訊：*\n```{json.dumps(extra_info, ensure_ascii=False, indent=2)}```"}},
            {"type": "context", "elements": [{"type": "plain_text", "text": f"時間：{datetime.now().isoformat()}"}]}
        ]
    }
    
    if SLACK_WEBHOOK_URL:
        try:
            resp = requests.post(SLACK_WEBHOOK_URL, json=slack_message)
            resp.raise_for_status()
            state["system"]["manual_review_status"] = "pending"
        except Exception as e:
            state["system"]["manual_review_status"] = "failed"
            state["system"]["manual_review_slack_error"] = str(e)
    else:
        state["system"]["manual_review_status"] = "failed"
        state["system"]["manual_review_slack_error"] = "SLACK_WEBHOOK_URL not set"
        
    state["system"]["current_node"] = "manual_review"
    return state
