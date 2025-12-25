import os
import sys
import json
import logging
from typing import Any
from PyPDF2 import PdfReader

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.parsers.interfaces import ResumeSchema

logging.basicConfig(
    filename='resume_parser.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

def parse_resume_pdf(pdf_path: str) -> ResumeSchema:
    """
    解析履歷PDF並回傳結構化資料。
    :param pdf_path: PDF檔案路徑
    :return: ResumeSchema 格式的 dict
    """
    if not os.path.exists(pdf_path):
        logging.error(f"檔案不存在: {pdf_path}")
        raise FileNotFoundError(f"檔案不存在: {pdf_path}")

    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        # TODO: 真正的解析邏輯，這裡僅為範例
        result: ResumeSchema = {
            "name": "李岳駿 (Jerry Lee)",
            "total_experience_years": 5.5,
            "skills": {
                "programming": ["Python", "SQL"],
                "ml_frameworks": ["PyTorch", "TensorFlow"],
                "cloud_devops": ["Docker", "Kubernetes"]
            },
            "work_history": [
                {
                    "company": "昇銳智慧科技",
                    "role": "AI工程師",
                    "duration": "2024/10-至今",
                    "key_tech": ["YOLO", "OpenCV"]
                }
            ]
        }
        logging.info("解析成功")
        return result
    except Exception as e:
        logging.error(f"解析失敗: {e}")
        raise

if __name__ == "__main__":
    pdf_path = "data/raw/resumes/Li-Yue-Jun-v4.pdf"
    output_path = "data/parsed/parsed_resume.json"
    try:
        result = parse_resume_pdf(pdf_path)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"解析完成，輸出：{output_path}")
    except Exception as e:
        print(f"解析失敗: {e}")
