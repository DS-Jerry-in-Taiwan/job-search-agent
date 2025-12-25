# Phase 7 - Query Enhancement 開發目標上下文

**階段**: Day 2 - Phase 7  
**時間**: 2025-12-25 10:45 AM  
**預估時間**: 28 分鐘  
**優先級**: P0 (關鍵)

---

## 🎯 核心目標

建立查詢增強層 (Query Enhancement Layer)，提升 RAG 檢索系統的查詢品質與準確度。

### 主要目標

1. **Query Rewriter**: 將自然語言查詢轉換為最佳檢索查詢
2. **HyDE Generator**: 生成假設性文檔提升檢索準確度
3. **Query Decomposer**: 複雜查詢拆解為多個子查詢

### 成功標準

```
✅ 3 個核心模組完整實現
✅ 8 個單元測試全部通過
✅ 類型註解覆蓋率 100%
✅ 查詢改寫成功率 > 95%
✅ HyDE 品質評分 > 0.85
✅ 查詢分解準確率 > 90%
✅ 處理延遲 < 200ms
✅ 文檔完整度 100%
```

---

## 📦 交付物清單

### 程式碼模組 (3個)

```
src/rag/query/
├── __init__.py           ✅ 導出所有查詢增強功能
├── rewriter.py           ✅ QueryRewriter 類別
├── hyde.py               ✅ HyDEGenerator 類別
└── decomposer.py         ✅ QueryDecomposer 類別
```

### 測試模組 (1個，8測試)

```
tests/rag/
└── test_query_enhancement.py
    ├── test_query_rewriter_basic()
    ├── test_query_rewriter_multilingual()
    ├── test_query_multi_rewrite()
    ├── test_hyde_generation()
    ├── test_hyde_quality()
    ├── test_query_decomposition()
    ├── test_query_merge_results()
    └── test_enhancement_pipeline()
```

### 文檔 (1個)

```
docs/rag/
└── query_enhancement_guide.md
    ├── 查詢增強概述
    ├── Query Rewriter 使用指南
    ├── HyDE 原理與實踐
    ├── Query Decomposer 策略
    └── 完整使用範例
```

---

## 🎯 品質指標

### 功能指標

| 指標 | 目標值 | 測量方法 |
|------|--------|---------|
| 查詢改寫成功率 | >95% | 自動評估 + 人工審核 |
| HyDE 品質評分 | >0.85 | 語意相似度評分 |
| 查詢分解準確率 | >90% | 邏輯正確性驗證 |
| 多語言支援 | 中文/英文 | 測試案例覆蓋 |

### 效能指標

| 指標 | 目標值 | 測量方法 |
|------|--------|---------|
| Query Rewriter 延遲 | <100ms | 平均執行時間 |
| HyDE 生成延遲 | <200ms | 平均執行時間 |
| Query Decomposer 延遲 | <150ms | 平均執行時間 |
| 整體處理延遲 | <300ms | 端到端計時 |

### 程式碼品質

```
✅ 類型註解 100%
✅ Docstring 100%
✅ Mypy 嚴格模式通過
✅ 測試覆蓋率 > 95%
✅ 程式碼可讀性 A+
```

---

## 🔗 依賴關係

### 前置依賴 (Day 1)

```
✅ LangChain 框架
✅ OpenAI API 配置
✅ State Schema 定義
✅ 基礎測試框架
```

### 技術依賴

```python
# 核心依賴
langchain>=0.1.0
openai>=1.0.0
tiktoken>=0.5.0

# 測試依賴
pytest>=7.4.0
pytest-asyncio>=0.21.0
```

### 後續依賴 (Phase 8-12)

```
Phase 8: Embedding 將使用 Query Enhancement 結果
Phase 10: Retrieval 將使用增強後的查詢
Phase 12: Integration 將整合完整查詢增強流程
```

---

## 💡 技術要點

### Query Rewriter 設計

**核心概念**:
- 將口語化查詢轉換為精確的檢索關鍵字
- 移除冗余詞彙，保留核心語意
- 支援中英文查詢轉換

**實現策略**:
```python
# Prompt Engineering
system_prompt = '''
你是查詢優化專家。將用戶的自然語言查詢轉換為最佳的搜尋關鍵字。

規則:
1. 保留核心關鍵字
2. 移除冗余詞彙 (我想、請幫我等)
3. 轉換為專業術語
4. 支援中英文混合

範例:
輸入: "我想找台北的Python後端工程師工作"
輸出: "Python backend engineer job Taipei Taiwan"
'''
```

### HyDE 原理

**核心概念**:
- Hypothetical Document Embeddings
- 生成「理想答案」，用答案向量檢索
- 比直接用問題檢索更精準 (+20-30%)

**實現策略**:
```python
# Prompt Engineering
system_prompt = '''
你是職缺描述撰寫專家。根據用戶查詢，生成一個理想的職缺描述。

要求:
1. 描述應該包含用戶期望的所有要素
2. 使用專業的職缺描述語言
3. 長度約 150-200 字
4. 包含技能要求、工作內容、公司文化

範例:
查詢: "Python backend job in Taipei"
生成: "We are seeking a talented Python Backend Engineer...
[完整的理想職缺描述]"
'''
```

### Query Decomposer 邏輯

**核心概念**:
- 識別複雜查詢中的 AND/OR 邏輯
- 拆解為獨立子查詢
- 平行執行，智能合併

**實現策略**:
```python
# 邏輯分析
# 輸入: "台北或新竹的Python或Java後端工作"
# 分解:
sub_queries = [
    "Python backend Taipei",
    "Java backend Taipei",
    "Python backend Hsinchu",
    "Java backend Hsinchu"
]
# 合併: 使用 RRF 或加權平均
```

---

## 🚀 開發優先級

### P0 (必須實現)

```
1. QueryRewriter 基本功能
   - rewrite() 方法
   - 中英文支援
   - 基本 Prompt

2. HyDEGenerator 基本功能
   - generate_hypothetical_doc() 方法
   - 基本 Prompt
   - 單文檔生成

3. QueryDecomposer 基本功能
   - decompose() 方法
   - AND/OR 邏輯識別
   - 基本合併邏輯
```

### P1 (應該實現)

```
1. QueryRewriter 進階功能
   - multi_rewrite() 生成多個版本
   - 查詢品質評分

2. HyDEGenerator 進階功能
   - generate_multiple() 生成多個文檔
   - 品質評估

3. QueryDecomposer 進階功能
   - 複雜邏輯處理
   - 智能權重分配
```

### P2 (可選實現)

```
1. 查詢意圖分類
2. 查詢建議功能
3. A/B 測試框架
```

---

## ⚠️ 注意事項

### API 調用限制

```python
# OpenAI API 限制
- text-davinci-003: 3,000 requests/min
- gpt-4: 500 requests/min
- gpt-3.5-turbo: 3,500 requests/min

# 緩解策略
1. 實現指數退避重試
2. 使用 gpt-3.5-turbo (更快更便宜)
3. 批次處理請求
4. 實現本地快取
```

### 錯誤處理

```python
# 必須處理的錯誤
1. API 調用失敗 → 回退到原始查詢
2. 網路超時 → 重試機制
3. 回應格式錯誤 → 驗證與修正
4. 空查詢輸入 → 預設處理
```

### 效能優化

```python
# 優化策略
1. 非同步 API 調用
2. 結果快取 (基於查詢 hash)
3. Prompt 長度控制
4. 批次請求合併
```

---

## 📊 驗收標準

### 自動化驗收

```bash
# 執行所有測試
pytest tests/rag/test_query_enhancement.py -v

# 檢查覆蓋率
pytest tests/rag/test_query_enhancement.py --cov=src/rag/query

# 類型檢查
mypy src/rag/query/ --strict

# 程式碼品質
pylint src/rag/query/
```

### 人工驗收

```
□ 查詢改寫結果合理
□ HyDE 生成品質高
□ 查詢分解邏輯正確
□ 文檔清晰易懂
□ 程式碼可讀性好
```

### 效能驗收

```python
# 效能測試
def test_performance():
    rewriter = QueryRewriter()

    # 測試 100 次
    times = []
    for _ in range(100):
        start = time.time()
        rewriter.rewrite("test query")
        times.append(time.time() - start)

    avg_time = sum(times) / len(times)
    assert avg_time < 0.1  # <100ms
```

---

## 🎓 學習資源

### HyDE 論文與實現

- [HyDE Paper](https://arxiv.org/abs/2212.10496)
- [LangChain HyDE](https://python.langchain.com/docs/use_cases/query_analysis/techniques/hyde)
- [Cohere Blog on HyDE](https://cohere.com/blog/hyde)

### Query Rewriting 最佳實踐

- [Query Understanding in RAG](https://www.pinecone.io/learn/query-understanding/)
- [Advanced RAG Techniques](https://www.llamaindex.ai/blog/advanced-rag-techniques)

---

**Phase 7 開發目標定義完成！準備進入開發流程！** 🚀
