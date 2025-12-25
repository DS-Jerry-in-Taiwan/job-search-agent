# Phase 8 開發流程

執行時間: 12:49 - 13:14 (25分鐘)
模式: Multi-Agent 自動化

## 流程

Stage 1: @INFRA 環境準備 (3-5min)
  → Stage 2: @ARCH 架構設計 (5-7min)
    → Stage 3: @CODER 程式實現 (10-12min)
      → Stage 4: @ANALYST 測試驗證 (5-7min)

## Stage 1: @INFRA

建立目錄:
- src/rag/embeddings
- tests/rag
- docs/rag

建立檔案:
- __init__.py
- manager.py
- chunker.py
- cache.py
- test_embeddings.py

驗證依賴:
- openai, tiktoken, numpy

## Stage 2: @ARCH

設計 EmbeddingManager:
- __init__(model, dimensions)
- embed_text(text) -> List[float]
- embed_batch(texts) -> List[List[float]]

設計 TextChunker:
- __init__(chunk_size, overlap)
- chunk_text(text) -> List[str]
- chunk_documents(docs) -> List[Dict]

設計 EmbeddingCache:
- get(text) -> Optional[List[float]]
- set(text, embedding)
- clear()

## Stage 3: @CODER

實現 EmbeddingManager:
- OpenAI client 初始化
- embed_text 使用 openai.embeddings.create
- embed_batch 批次處理
- 錯誤處理與重試

實現 TextChunker:
- tiktoken 計算 tokens
- 固定大小分塊
- 重疊處理
- 句子邊界保留

實現 EmbeddingCache:
- 使用 dict 作為快取
- hash(text) 作為鍵
- LRU 邏輯
- 大小限制

## Stage 4: @ANALYST

實現 8 個測試:
- 基本向量化
- 批次處理
- 文本分塊
- 快取命中
- 邊界案例

執行驗證:
- pytest -v
- coverage >90%
- mypy --strict

## 完成標準

- 所有 Stage 完成
- 8 個測試通過
- 覆蓋率 >90%
- 類型檢查通過
- 總時間 <25分鐘
