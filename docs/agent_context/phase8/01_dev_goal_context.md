# Phase 8 - Embedding & Vectorization 開發目標

**階段**: Day 2 - Phase 8  
**時間**: 2025-12-25 12:49 PM  
**預估時間**: 20-25 分鐘  
**優先級**: P0 (關鍵)

## 核心目標

建立向量化層，將文本轉換為高維度向量，支援語意檢索。

### 主要目標

1. EmbeddingManager - 統一向量化管理
2. TextChunker - 智能文本分塊
3. EmbeddingCache - 向量快取機制

### 成功標準

- 3 個核心模組完整實現
- 8+ 個單元測試通過
- 類型註解 100%
- 向量化準確率 >99%
- 處理延遲 <100ms (有快取)
- 快取命中率 >80%

## 交付物

### 程式碼模組 (4個)

src/rag/embeddings/
- __init__.py
- manager.py (EmbeddingManager)
- chunker.py (TextChunker)
- cache.py (EmbeddingCache)

### 測試 (8+)

- test_embedding_manager_init
- test_embed_text
- test_embed_batch
- test_text_chunker
- test_chunk_overlap
- test_embedding_cache
- test_cache_hit
- test_multi_model_support

## 品質指標

功能: 向量化準確率 >99%
效能: 單次延遲 <50ms, 批次 <200ms
快取: 命中率 >80%, 查詢 <1ms

## 技術要點

### EmbeddingManager
- OpenAI text-embedding-3-small
- 支援批次處理
- 自動錯誤重試

### TextChunker
- 智能分塊 (512 tokens)
- 重疊保留上下文 (50 tokens)
- 句子完整性

### EmbeddingCache
- LRU 快取策略
- 文本 hash 為鍵
- 最大 1000 個向量

## 依賴

- openai>=1.0.0
- tiktoken>=0.5.0
- numpy>=1.24.0
- pytest>=7.4.0

## 注意事項

OpenAI API 限制:
- 最大 8191 tokens
- 速率 3000 req/min
- 文本過長自動分塊

記憶體:
- 1個向量 ~6KB
- 1000個向量 ~6MB
- LRU 自動淘汰
