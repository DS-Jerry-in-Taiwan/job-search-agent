# Phase 9 Agent 角色

## @INFRA (環境工程師)

職責: 環境準備、依賴安裝、目錄建立

任務:
1. 建立 src/rag/vectordb 目錄
2. 建立 4 個核心檔案
3. 安裝 faiss-cpu, numpy
4. 驗證 FAISS 可正常導入

輸出: 環境準備報告

## @ARCH (架構師)

職責: 抽象介面設計、類別架構規劃

任務:
1. 設計 VectorStoreBase 抽象介面
   - 定義所有必要方法
   - 完整 type hints

2. 設計 FaissVectorStore 實現
   - FAISS 索引初始化策略
   - metadata 儲存結構
   - 過濾機制設計

3. 設計 InMemoryVectorStore (optional)
   - NumPy 實現方案

輸出: 完整類別介面定義

## @CODER (程式開發者)

職責: 程式實現、FAISS 整合

任務:
1. 實現 VectorStoreBase
   - ABC 抽象類
   - 完整 Docstring

2. 實現 FaissVectorStore
   - FAISS index 初始化
   - add/search/save/load 方法
   - metadata 管理
   - 錯誤處理

3. 實現 InMemoryVectorStore (optional)
   - NumPy 相似度計算
   - 簡單排序與過濾

技術重點:
- FAISS API 正確使用
- NumPy array 轉換
- UUID 生成管理
- 錯誤處理與驗證

輸出: 完整可執行程式碼

## @ANALYST (測試分析師)

職責: 測試設計、效能驗證

任務:
1. 實現 10+ 測試案例
   - 功能測試 (新增/檢索/過濾)
   - 邊界測試 (空索引/維度錯誤)
   - 效能測試 (大規模/延遲)

2. 執行驗證
   - pytest -v
   - coverage >90%
   - mypy --strict

3. 效能測試
   - pytest-benchmark
   - 檢索延遲測試
   - 批次新增測試

輸出: 測試報告與效能分析
