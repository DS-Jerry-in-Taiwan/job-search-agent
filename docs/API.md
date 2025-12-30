# StateGraph 可視化 API 文件

## 端點說明

### GET /api/v1/graph/visualize

- 功能：回傳 StateGraph 的流程圖（mermaid/dot 格式）、節點與邊結構
- 回傳格式：
  ```json
  {
    "graph_svg": "mermaid 格式字串或 dot 格式字串",
    "nodes": ["node1", "node2", ...],
    "edges": ["edge1", "edge2", ...]
  }
  ```

- 範例請求：
  ```
  GET /api/v1/graph/visualize
  ```

- 範例回應：
  ```json
  {
    "graph_svg": "graph TD; A-->B; B-->C;",
    "nodes": ["A", "B", "C"],
    "edges": ["A-->B", "B-->C"]
  }
  ```

## 多 workflow 支援

- 可於 API 增加參數 workflow_id，根據 workflow_id 回傳不同 StateGraph。
- 範例：
  ```
  GET /api/v1/graph/visualize?workflow_id=demo
  ```

## 前端渲染建議

- 使用 mermaid.js 或 graphviz.js 於前端渲染流程圖。
- 參考 ui/graph_demo.html + ui/graph_demo.js 實作。

## 驗收測試

- API 回傳格式正確
- 前端可正確渲染流程圖
- 多 workflow 切換無誤
