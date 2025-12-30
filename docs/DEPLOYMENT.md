# JobSearch Agent 部署指南

## 需求

- Docker, docker-compose
- Python 3.11+ (如需本地啟動)
- requirements.txt 依賴已安裝

## 一鍵部署（推薦）

```bash
chmod +x deploy.sh
./deploy.sh
```

- 服務啟動後：
  - 前端 UI: http://localhost:8501
  - API 文檔: http://localhost:8000/docs
  - 健康檢查: http://localhost:8000/health

## 手動部署

### 1. 啟動 FastAPI 後端

```bash
docker build -t jobsearch-backend .
docker run -d -p 8000:8000 --env OPENAI_API_KEY=xxx jobsearch-backend
```

### 2. 啟動 Streamlit 前端

```bash
cd ui
docker build -t jobsearch-frontend -f Dockerfile .
docker run -d -p 8501:8501 --env API_URL=http://localhost:8000 jobsearch-frontend
```

### 3. 本地開發模式

```bash
pip install -r requirements.txt
uvicorn api.server:app --reload --host 0.0.0.0 --port 8000
# 另開終端
cd ui
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```

## 環境變數

- OPENAI_API_KEY：必填，後端 LLM 調用
- API_URL：前端調用後端 API

## 常見問題

- 端口衝突請檢查 8000/8501 是否被佔用
- Docker 啟動失敗請檢查 logs

## 健康檢查

```bash
curl http://localhost:8000/health
```

## 停止服務

```bash
docker-compose down
```

---
