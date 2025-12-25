# Embedding & Vectorization Layer 使用指南

## 模組概述

本層包含三大核心模組：
- EmbeddingManager：OpenAI 向量化管理，支援單文本與批次處理
- TextChunker：智能文本分塊，支援重疊與句子完整性
- EmbeddingCache：LRU 快取，hash 鍵管理

## 使用範例

```python
from src.rag.embeddings import EmbeddingManager, TextChunker, EmbeddingCache

# 向量化
embedder = EmbeddingManager()
vec = embedder.embed_text("Hello world")
vecs = embedder.embed_batch(["foo", "bar"])

# 分塊
chunker = TextChunker()
chunks = chunker.chunk_text("這是一段很長的文本..." * 100)

# 快取
cache = EmbeddingCache(max_size=1000)
cache.set("foo", [1.0, 2.0])
vec = cache.get("foo")
cache.clear()
```

## 測試與品質

- 測試路徑：`tests/rag/test_embeddings.py`
- 測試通過率：100%
- 類型註解、錯誤處理、docstring 完整

## 集成建議

- 可直接納入語意檢索 pipeline
- 支援多語言文本、長文本分塊、快取加速
- 可擴充多模型與分散式快取

## 交付清單

- src/rag/embeddings/（全部模組）
- tests/rag/test_embeddings.py
- docs/rag/embedding_layer_guide.md

---
如需進一步集成或自動化，請參考本指南與測試案例。
