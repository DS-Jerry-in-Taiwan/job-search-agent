# RAG 系統開發與使用指南

## 模組架構

- `RAGPipeline`：端到端查詢主流程，整合查詢增強、embedding、retriever、assembler、optimizer、monitor、evaluator。
- `RAGOptimizer`：快取、批次處理、預熱機制。
- `RAGMonitor`：查詢延遲、快取命中率、品質指標監控。
- `RAGEvaluator`：查詢品質評分與指標計算。

## RAGEvaluator

RAGEvaluator 負責查詢品質評分與指標計算，支援 Top-K 準確率、MRR、NDCG、A/B 測試等。

> **註：evaluate 方法目前為 stub（僅回傳預設分數 1.0），主流程打通後可依需求擴充精細評分邏輯。**

## 開發與擴充建議

- 第一版僅需保證主流程與測試通過，進階排序、去重、精細評分可於後續優化階段擴充。
- 文檔應註明 stub 實作，方便團隊後續維護與升級。

## 參考

- 詳細 API 與測試案例請參閱各模組原始碼與 tests/rag/ 目錄。
