# Phase 7 開發流程上下文

**執行時間**: 10:45 - 11:13 (28分鐘)
**模式**: Multi-Agent 自動化協作

## 開發流程

```
Stage 1: @INFRA 環境準備 (3-5min)
  → Stage 2: @ARCH 架構設計 (5-7min)
    → Stage 3: @CODER 程式實現 (12-15min)
      → Stage 4: @ANALYST 測試驗證 (5-7min)
        → ✅ Phase 7 完成
```

## Stage 1: @INFRA (環境準備)

建立目錄與檔案結構，驗證依賴。

交付: 5個檔案 + 目錄結構

## Stage 2: @ARCH (架構設計)

設計 3 個核心類別的介面：
- QueryRewriter
- HyDEGenerator  
- QueryDecomposer

交付: 完整類別介面定義

## Stage 3: @CODER (程式實現)

實現所有類別與方法，包含 Prompt Engineering。

交付: 3個完整模組 + 導出檔案

## Stage 4: @ANALYST (測試驗證)

實現 8 個單元測試，執行驗證。

交付: 測試套件 + 驗證報告

## 完成標準

```
✅ 所有 Stage 完成
✅ 8 個測試通過
✅ 覆蓋率 >90%
✅ 類型檢查通過
✅ 總時間 <30分鐘
```
