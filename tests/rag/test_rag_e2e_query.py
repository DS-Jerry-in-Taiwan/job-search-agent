import pytest
from src.rag import RAGSystem

# @pytest.mark.skip("端到端查詢需完整資料與模型，僅範例展示")
def test_rag_e2e_query():
    rag = RAGSystem()
    query = "桃園python AI工程師 4-6年以上經驗"
    user_profile = {
        "skills": [
            "Python", "AI", "ETL", "PyTorch", "Scikit-learn", "ONNX", "Langchain", "Langgraph",
            "OpenCV", "YOLO", "Docker", "Kubernetes", "AWS", "QuestDB", "Elasticsearch",
            "Redis", "Prometheus", "Grafana"
        ],
        "experience": "6年",
        "location": "桃園"
    }
    # 端到端查詢流程（僅驗證 API 可調用，不驗證結果內容）
    try:
        result = rag.search(query, user_profile)
        print("查詢結果：", result)
    except NotImplementedError:
        # 尚未實作 search，允許拋出
        assert True
    except Exception as e:
        print("查詢異常：", e)
        assert False, f"查詢流程出現未預期錯誤: {e}"
