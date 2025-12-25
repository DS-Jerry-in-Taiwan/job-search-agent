# Phase 9 開發流程

執行時間: 15:01 - 15:31 (30分鐘)
模式: Multi-Agent 自動化

## 流程

Stage 1: @INFRA 環境準備 (3-5min)
  → Stage 2: @ARCH 架構設計 (5-7min)
    → Stage 3: @CODER 程式實現 (12-15min)
      → Stage 4: @ANALYST 測試驗證 (5-7min)

## Stage 1: @INFRA

建立目錄:
- src/rag/vectordb
- tests/rag
- docs/rag

建立檔案:
- __init__.py
- base.py
- faiss_store.py
- memory_store.py (optional)
- test_vectordb.py

安裝依賴:
pip install faiss-cpu numpy

驗證:
python -c "import faiss, numpy; print('OK')"

## Stage 2: @ARCH

設計 VectorStoreBase:
- add(vectors: List[List[float]], metadatas: List[Dict]) -> List[str]
- search(query_vector: List[float], top_k: int, filters: Dict) -> List[Dict]
- delete(ids: List[str]) -> bool
- save(path: str) -> None
- load(path: str) -> None

設計 FaissVectorStore:
- __init__(dim: int, metric: str = "l2")
- 使用 faiss.IndexFlatL2 或 IndexFlatIP
- 內部維護 ids 與 metadatas 列表
- 實現所有抽象方法

設計 InMemoryVectorStore (optional):
- 純 NumPy 實現
- 用於測試與小型資料

## Stage 3: @CODER

實現 VectorStoreBase (base.py):
- ABC 抽象類
- 完整 type hints
- Docstring

實現 FaissVectorStore (faiss_store.py):
- __init__: 初始化 FAISS index
- add: 轉換為 numpy array, 呼叫 index.add()
- search: index.search(), 組合 metadata
- 過濾: 後處理 Python filter
- save/load: faiss.write_index / read_index
- 錯誤處理: 維度檢查, 空索引處理

實現 InMemoryVectorStore (optional):
- NumPy 計算 L2 距離
- argsort 排序
- metadata 字典儲存

模組導出 (__init__.py):
- from .base import VectorStoreBase
- from .faiss_store import FaissVectorStore

## Stage 4: @ANALYST

實現 10+ 測試:
1. test_vector_store_init - 初始化
2. test_add_single_vector - 單個向量新增
3. test_add_batch_vectors - 批次新增
4. test_search_similarity - 相似度檢索
5. test_search_top_k - Top-K 正確性
6. test_search_with_filters - 元數據過濾
7. test_save_load_index - 持久化
8. test_empty_search - 空索引搜尋
9. test_dimension_mismatch - 維度錯誤
10. test_large_scale - 1000+ 向量效能

執行驗證:
- pytest tests/rag/test_vectordb.py -v
- pytest --cov=src/rag/vectordb
- mypy src/rag/vectordb/ --strict

效能測試:
- 使用 pytest-benchmark
- 檢索延遲 <10ms
- 批次新增效能

## 完成標準

- 所有 Stage 完成
- 10+ 測試通過
- 覆蓋率 >90%
- 類型檢查通過
- 效能達標
- 總時間 <30分鐘
