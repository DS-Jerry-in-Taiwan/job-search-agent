# Phase 9 - Vector Database 開發目標

**階段**: Day 2 - Phase 9  
**時間**: 2025-12-25 15:01 PM  
**預估時間**: 25-30 分鐘  
**優先級**: P0 (關鍵)

## 核心目標

建立向量資料庫層，提供高效的向量儲存、檢索與過濾能力。

### 主要目標

1. VectorStoreBase - 抽象介面定義
2. FaissVectorStore - FAISS 實現
3. MetadataIndex - 元數據索引與過濾
4. Index Management - 索引持久化

### 成功標準

- 3 個核心模組完整實現
- 10+ 個單元測試通過
- 類型註解 100%
- 向量檢索準確率 100%
- 檢索延遲 <10ms (10k向量)
- 支援 metadata 過濾
- 支援索引持久化

## 交付物

### 程式碼模組 (4個)

src/rag/vectordb/
- __init__.py
- base.py (VectorStoreBase 抽象類)
- faiss_store.py (FaissVectorStore)
- memory_store.py (InMemoryVectorStore, optional)

### 測試 (10+)

- test_vector_store_init
- test_add_vectors
- test_add_batch
- test_search_similarity
- test_search_with_filters
- test_metadata_filtering
- test_save_load_index
- test_empty_search
- test_dimension_mismatch
- test_large_scale (1000+ vectors)

## 品質指標

功能: 
- 向量新增準確率 100%
- 檢索準確率 100% (相似度排序正確)
- Metadata 過濾正確性 100%

效能: 
- 單次檢索 <10ms (10k向量)
- 批次新增 1000向量 <1s
- 索引載入 <100ms

可靠性:
- 索引持久化正確
- 錯誤處理完善

## 技術要點

### FAISS 選擇

使用 FAISS (Facebook AI Similarity Search):
- 開源、高效能、成熟
- 支援 CPU/GPU
- 多種索引類型
- Python 綁定完整

初期使用 IndexFlatL2:
- 精確搜尋 (100% recall)
- 實現簡單
- 適合中小規模 (<100k)

### VectorStoreBase 設計

抽象介面定義:
- add(vectors, metadatas) -> ids
- search(query_vector, top_k, filters) -> results
- delete(ids) -> bool
- update(id, vector, metadata) -> bool
- save(path) -> None
- load(path) -> None

### Metadata 索引

使用 Python dict 儲存:
- key: vector_id (uuid)
- value: metadata (job_id, title, location, etc.)

過濾策略:
- 先向量檢索 (FAISS)
- 後 metadata 過濾 (Python)
- 支援多條件 AND 邏輯

## 依賴

核心:
- faiss-cpu>=1.7.4 (或 faiss-gpu)
- numpy>=1.24.0

測試:
- pytest>=7.4.0
- pytest-benchmark (效能測試)

## 與 Phase 8 整合

from src.rag.embeddings import EmbeddingManager
from src.rag.vectordb import FaissVectorStore

# Phase 8: 向量化
embedder = EmbeddingManager()
vectors = embedder.embed_batch(texts)

# Phase 9: 儲存
store = FaissVectorStore(dim=1536)
ids = store.add(vectors, metadatas)

# Phase 9: 檢索
query_vec = embedder.embed_text(query)
results = store.search(query_vec, top_k=10)

## 注意事項

FAISS 限制:
- IndexFlatL2 需將所有向量載入記憶體
- 維度必須一致
- 不支援動態刪除 (需重建索引)

記憶體估算:
- 1個向量 (1536維) = 6KB
- 10k向量 = 60MB
- 100k向量 = 600MB

擴展策略:
- 初期: IndexFlatL2 (<100k)
- 中期: IndexIVFFlat (100k-1M)
- 長期: IndexHNSW (>1M, 需近似)

錯誤處理:
- 維度不匹配 -> 拒絕新增
- 空查詢 -> 回傳空列表
- 索引檔案損壞 -> 重建提示
- ID 不存在 -> 錯誤訊息
