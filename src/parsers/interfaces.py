from typing import TypedDict, List, Dict, Any

class WorkHistoryItem(TypedDict):
    company: str
    role: str
    duration: str
    key_tech: List[str]

class Skills(TypedDict):
    programming: List[str]
    ml_frameworks: List[str]
    cloud_devops: List[str]

class ResumeSchema(TypedDict):
    name: str
    total_experience_years: float
    skills: Skills
    work_history: List[WorkHistoryItem]

def parse_resume_pdf(pdf_path: str) -> ResumeSchema:
    """
    解析履歷PDF並回傳結構化資料。
    :param pdf_path: PDF檔案路徑
    :return: ResumeSchema 格式的 dict
    """
    ...
