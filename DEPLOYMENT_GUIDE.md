# 部署指南（DEPLOYMENT_GUIDE.md）

## 環境需求
- Python 3.10 以上
- pip
- 建議使用虛擬環境（venv/conda）

## 安裝步驟

1. 下載專案原始碼
2. 安裝依賴套件
   ```bash
   pip install -r requirements.txt
   ```
3. 啟動 FastAPI 服務
   ```bash
   uvicorn src.api.main:app --reload --port 8000
   ```
4. 開啟瀏覽器進入 [http://localhost:8000/docs](http://localhost:8000/docs) 查看 API 文件

## 測試驗證

- 執行自動化測試
  ```bash
  pytest tests/test_api_endpoints.py -v
  ```
- 所有測試通過即代表部署成功

## Docker 部署（可選）

1. 建立映像檔
   ```bash
   docker build -t langgraph-api .
   ```
2. 啟動容器
   ```bash
   docker run -p 8000:8000 langgraph-api
   ```

## 常見問題

- 若遇到套件安裝失敗，請確認 Python 版本與 pip 已更新
- 若端口被佔用，可調整 `--port` 參數

## 聯絡方式
如有部署相關問題，請聯絡專案維護者。
