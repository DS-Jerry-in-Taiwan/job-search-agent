# JobSearch Agent API 說明

## 主要端點

### POST /api/chat
- 說明：多智能體對話入口，調用 SupervisorAgent
- 輸入：
  ```json
  {
    "message": "找台北 Python 工作",
    "user_profile": {
      "skills": ["Python"],
      "experience_years": 3,
      "location": "台北"
    }
  }
  ```
- 輸出：
  ```json
  {
    "response": "推薦職缺...",
    "status": "success"
  }
  ```

### GET /api/search
- 說明：職缺搜尋，調用 JobSearchAgent
- 輸入參數：`query` (string)
- 輸出：
  ```json
  {
    "jobs": [],
    "query": "Python"
  }
  ```

### POST /api/analyze
- 說明：薪資分析，調用 SalaryAnalyzerAgent
- 輸入參數：`job_title` (string), `experience` (int)
- 輸出：
  ```json
  {
    "salary_range": {},
    "advice": "",
    "job_title": "Python 後端",
    "experience": 3
  }
  ```

### GET /health
- 說明：健康檢查
- 輸出：
  ```json
  {
    "status": "ok",
    "version": "1.0.0"
  }
  ```

### GET /docs
- 說明：Swagger/OpenAPI 文件

---

## 錯誤格式

- HTTP 500:
  ```json
  {
    "detail": "錯誤訊息"
  }
  ```

---

## CORS 支援

- 允許所有來源，支援跨域請求

---

## 版本

- v1.0.0
