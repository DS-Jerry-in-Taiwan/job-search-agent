import pytest
from src.nodes.resume_parser import resume_parser_node

def test_resume_parser_pdf():
    state = {
        "user_profile": {
            "user_id": "test_user",
            "resume_path": "data/raw/resumes/Li-Yue-Jun-v4.pdf",
            "resume_text": "",
            "skills": [],
            "experience_years": 0,
            "education": "",
            "preferences": {},
            "parsed_at": None
        },
        "job_state": {
            "jobs": [],
            "matched_jobs": [],
            "match_scores": {},
            "recommendations": [],
            "last_updated": None
        },
        "conversation": {
            "messages": [],
            "current_intent": "",
            "context": {},
            "history_summary": "",
            "turn_count": 0
        },
        "system": {
            "current_node": "",
            "workflow_status": "",
            "error_message": None,
            "retry_count": 0,
            "metadata": {}
        },
        "next_action": "",
        "is_complete": False
    }
    out = resume_parser_node(state)
    assert isinstance(out["user_profile"]["skills"], list)
    assert out["user_profile"]["experience_years"] == 3.5
    assert isinstance(out["user_profile"]["skill_score"], int)
    assert isinstance(out["user_profile"]["exp_score"], int)
    assert isinstance(out["user_profile"]["pref_score"], int)
    assert out["system"]["current_node"] == "resume_parser"
