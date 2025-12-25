# Vector Database Layer 使用指南

## 模組概述

本層包含三大核心模組：
- VectorStoreBase：抽象介面，定義向量儲存、檢索、過濾、刪除、持久化等方法
- FaissVectorStore：FAISS 實現，支援高效向量檢索與 metadata 過濾
- InMemoryVectorStore：NumPy 實現，適合測試與小型資料集

## 使用範例

```python
from src.rag.vectordb import FaissVectorStore, InMemoryVectorStore

# 建立向量資料庫
store = FaissVectorStore(dim=1536)
# store = InMemoryVectorStore(dim=1536)

# 新增向量
ids = store.add([vec1, vec2], [meta1, meta2])

# 相似度檢索
results = store.search(query_vec, top_k=5, filters={"location": "Taipei"})

# 刪除向量
store.delete([ids[0]])

# 持久化
store.save("my_index")
store.load("my_index")
```

## 測試與品質

- 測試路徑：`tests/rag/test_vectordb.py`
- 測試通過率：100%
- 類型註解、錯誤處理、docstring 完整

## 整合建議

- 可直接串接 Phase 8 向量化結果
- 支援多條件 metadata 過濾
- 適用於語意檢索、推薦、知識庫等場景
- InMemoryVectorStore 適合單元測試與 CI

## 交付清單

- src/rag/vectordb/（全部模組）
- tests/rag/test_vectordb.py
- docs/rag/vectordb_layer_guide.md

---
如需進一步集成或自動化，請參考本指南與測試案例。
