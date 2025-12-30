# LangGraph StateGraph API

## 專案簡介
本專案提供基於 FastAPI 的 StateGraph 多智能體協作 API，支援對話、健康檢查、流程圖可視化與 Session 歷史查詢。

## 快速啟動

```bash
pip install -r requirements.txt
uvicorn src.api.main:app --reload --port 8000
```

## API 端點說明

- `POST /api/v1/chat`  
  發送對話訊息，取得 AI 回應。

- `GET /api/v1/health`  
  健康檢查，回傳服務狀態。

- `GET /api/v1/graph/visualize`  
  取得 StateGraph 流程圖（SVG/JSON）。

- `GET /api/v1/session/{id}/history`  
  查詢指定 session 的對話歷史。

## Swagger 文件
啟動後瀏覽 [http://localhost:8000/docs](http://localhost:8000/docs) 可互動測試所有 API。

## 自動化測試

```bash
pytest tests/test_api_endpoints.py -v
```

## 目錄結構
- src/api/         FastAPI 主程式與路由
- src/langgraph/   StateGraph 編排核心
- tests/           測試腳本
- docs/            文件與設計說明

## 聯絡方式
如有問題請聯絡專案維護者。
