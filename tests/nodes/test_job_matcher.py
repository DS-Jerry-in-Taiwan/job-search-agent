import pytest
from src.nodes.job_matcher import job_matcher_node
import json
from pathlib import Path

def setup_jobs(tmp_path):
    jobs = [
        {"id": "job_1", "requirements": ["python", "ai"]},
        {"id": "job_2", "requirements": ["javascript", "react"]},
        {"id": "job_3", "requirements": ["docker", "kubernetes"]},
        {"id": "job_4", "requirements": ["python", "docker", "ai"]}
    ]
    jobs_path = tmp_path / "jobs.json"
    with open(jobs_path, "w", encoding="utf-8") as f:
        json.dump(jobs, f)
    return jobs_path

def test_job_matcher(tmp_path, monkeypatch):
    jobs_path = setup_jobs(tmp_path)
    monkeypatch.setattr("pathlib.Path.exists", lambda self: True)
    monkeypatch.setattr("pathlib.Path.open", lambda self, mode="r", encoding=None: open(jobs_path, mode, encoding=encoding))

    state = {
        "user_profile": {"skills": ["python", "ai", "docker"]},
        "job_state": {},
        "system": {}
    }
    out = job_matcher_node(state, jobs_path=str(jobs_path))
    # job_4 完全匹配，job_1 部分匹配
    assert any(j["id"] == "job_4" for j in out["job_state"]["matched_jobs"])
    assert any(j["id"] == "job_1" for j in out["job_state"]["matched_jobs"])
    assert out["system"]["current_node"] == "job_matcher"
    assert out["job_state"]["match_scores"]["job_4"] == 1.0
    assert out["job_state"]["match_scores"]["job_1"] == 1.0
