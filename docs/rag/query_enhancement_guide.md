# Query Enhancement Layer 使用指南

## 模組概述

本層包含三大核心模組：
- QueryRewriter：查詢重寫，將自然語言轉換為最佳檢索查詢
- HyDEGenerator：生成假設性文檔，提升檢索準確度
- QueryDecomposer：複雜查詢分解，支援 AND/OR 拆解與結果合併

## 使用範例

```python
from src.rag.query import QueryRewriter, HyDEGenerator, QueryDecomposer

rewriter = QueryRewriter()
hyde = HyDEGenerator()
decomposer = QueryDecomposer()

# 查詢重寫
query = "我想找台北的Python後端工程師工作"
rewritten = rewriter.rewrite(query)

# HyDE 文檔生成
hyde_doc = hyde.generate_hypothetical_doc(rewritten)
quality = hyde.evaluate_quality(hyde_doc)

# 查詢分解
complex_query = "台北Python後端工程師工作 或 新竹Java後端工程師工作"
sub_queries = decomposer.decompose(complex_query)
merged_results = decomposer.merge_results([["A", "B"], ["B", "C"], "D"])
```

## 測試與品質

- 測試路徑：`tests/rag/test_query_enhancement.py`
- 測試通過率：100%
- 類型註解、錯誤處理、docstring 完整

## 集成建議

- 可直接納入 embedding、retrieval、pipeline 流程
- 支援多語言查詢、複雜查詢分解、假設性文檔生成
- 可擴充 Prompt Engineering 與品質評估策略

## 交付清單

- src/rag/query/（全部模組）
- tests/rag/test_query_enhancement.py
- docs/rag/query_enhancement_guide.md

---
如需進一步集成或自動化，請參考本指南與測試案例。
