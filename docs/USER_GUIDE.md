# JobSearch Agent 使用者指南

## 產品簡介

JobSearch Agent 是一套 AI 驅動的智能職缺搜尋、薪資分析與面試準備平台，結合多智能體協作、RESTful API 與 Web UI，協助用戶高效探索職涯機會。

## 如何開始

### 1. 啟動服務

- 推薦：執行 `./deploy.sh` 一鍵部署
- 前端 UI: http://localhost:8501
- API 文檔: http://localhost:8000/docs

### 2. 使用 Web UI

- 於瀏覽器開啟 http://localhost:8501
- 左側可設定技能、年資、地點
- 下方輸入框可提問（如：「找台北 Python 工作」）
- 對話歷史自動保存於頁面

### 3. 使用 API

- 參考 docs/API.md
- 主要端點：
  - POST /api/chat：多智能體對話
  - GET /api/search：職缺搜尋
  - POST /api/analyze：薪資分析

### 4. 常見問題

- 問題：API 無回應？
  - 檢查後端服務是否啟動（`curl http://localhost:8000/health`）
- 問題：UI 無法連線？
  - 檢查前端服務與 API_URL 設定
- 問題：如何重設對話？
  - 重新整理頁面即可

### 5. 聯絡與支援

- 請聯絡專案維護者或參考 GitHub Issues

---

## 功能亮點

- 多智能體協作：自動分派職缺搜尋、薪資分析、面試建議
- 即時對話：支援多輪互動
- 個人化推薦：根據技能、年資、地點自動調整
- 一鍵部署：Docker 支援，快速上線

---

## 版本

- v1.0.0
