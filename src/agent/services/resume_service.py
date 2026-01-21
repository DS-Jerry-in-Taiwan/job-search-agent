from typing import Dict, Any
import PyPDF2
import json

def parse_resume(pdf_path: str) -> Dict[str, Any]:
    """
    解析 PDF 履歷，返回結構化資料
    """
    try:
        with open(pdf_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
        # TODO: 根據實際需求解析 text，這裡僅回傳原始文本
        return {"raw_text": text}
    except Exception as e:
        return {"error": str(e)}
