# Phase 8 Agent 角色

## @INFRA (環境工程師)

職責: 環境準備、目錄建立、依賴驗證

任務:
1. 建立 src/rag/embeddings 目錄
2. 建立 4 個核心檔案
3. 驗證 openai, tiktoken, numpy
4. 檢查 OPENAI_API_KEY

輸出: 環境準備報告

## @ARCH (架構師)

職責: 類別介面設計、API 定義

任務:
1. 設計 EmbeddingManager 介面
2. 設計 TextChunker 介面
3. 設計 EmbeddingCache 介面
4. 定義模組導出

輸出: 完整類別介面定義

## @CODER (程式開發者)

職責: 程式實現、錯誤處理

任務:
1. 實現 EmbeddingManager
   - OpenAI API 整合
   - 批次處理邏輯
2. 實現 TextChunker
   - Token 計算
   - 智能分塊
3. 實現 EmbeddingCache
   - LRU 快取
   - Hash 鍵管理

輸出: 完整可執行程式碼

## @ANALYST (測試分析師)

職責: 測試設計、品質驗證

任務:
1. 實現 8+ 測試案例
2. 執行測試驗證
3. 檢查測試覆蓋率
4. 執行類型檢查
5. 效能測試

輸出: 測試報告與驗證結果
