import os
import json
import pytest

from src.parsers.resume_parser import parse_resume_pdf

def test_parse_resume_pdf_success():
    pdf_path = "data/raw/resumes/Li-Yue-Jun-v4.pdf"
    result = parse_resume_pdf(pdf_path)
    assert isinstance(result, dict)
    assert "name" in result
    assert "skills" in result
    assert "work_history" in result

def test_parse_resume_pdf_file_not_found():
    with pytest.raises(FileNotFoundError):
        parse_resume_pdf("data/raw/resumes/not_exist.pdf")

def test_output_json_format():
    output_path = "data/parsed/parsed_resume.json"
    assert os.path.exists(output_path)
    with open(output_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, dict)
    assert "name" in data
    assert "skills" in data
    assert "work_history" in data
