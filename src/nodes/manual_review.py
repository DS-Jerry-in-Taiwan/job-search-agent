import requests
import os
import json
from datetime import datetime



def manual_review_node(state):
    """
    manual review node: 僅負責流程調度，所有功能調用 manual_review_service
    """
    from src.agent.services.manual_review_service import process_manual_review
    state = process_manual_review(state)
    return state
