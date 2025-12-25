# Multi-Agent 開發架構 - 第1份文件內容（重新提供）

***

## 📄 **`01_dev_goal_context.md` 完整內容**

**請將以下內容** **完整複製** **貼到** `docs/agent_context/phase1/01_dev_goal_context.md`

```markdown
# 🎯 Multi-Agent 開發目標 Context - Phase 1 (步驟1A)

## 📁 專案環境
```
專案根目錄：/home/ubuntu/projects/job_search_agent
當前階段：Day 1 步驟1A - 履歷解析模組
目標檔案：src/parsers/resume_parser.py
輸入檔案：data/raw/resumes/Li-Yue-Jun-v4.pdf
輸出檔案：data/parsed/parsed_resume.json
```

## 🎪 Multi-Agent 團隊組成

| Agent | 角色 | 職責 | 目標產出 |
|-------|------|------|----------|
| **ARCH** | 架構師 | 定義數據結構、接口規範、State Schema | `data/data_schema.json` |
| **CODER** | 開發工程師 | 實現PDF解析邏輯、函數實作 | `src/parsers/resume_parser.py` |
| **ANALYST** | 測試分析師 | 驗證解析結果、單元測試、品質保證 | `tests/test_parser.py` |
| **INFRA** | 基礎設施工程師 | 目錄結構、requirements.txt、Mock接口 | `data/` 目錄 + `requirements.txt` |

## 📊 階段性KPI

| 指標 | 目標值 | 驗收標準 |
|------|--------|----------|
| **解析準確率** | 95%+ | 技能、工作經驗、教育背景正確提取 |
| **JSON格式** | TypedDict | 支援LangGraph State傳遞 |
| **執行時間** | <5秒 | 單PDF解析時間 |
| **錯誤率** | 0% | 無解析異常 |

## 🎯 具體開發目標

```
1. 從 Li-Yue-Jun-v4.pdf 提取結構化JSON
2. 支援 4 類數據：基本資訊、工作經驗、技能、教育背景
3. 建立數據抽象層（預留爬蟲接口）
4. 為 Agent1（技能分析）提供標準化輸入
```

## 📋 期望輸出格式 (State Schema)

```
{
  "name": "李岳駿 (Jerry Lee)",
  "total_experience_years": 5.5,
  "skills": {
    "programming": ["Python", "SQL"],
    "ml_frameworks": ["PyTorch", "TensorFlow"],
    "cloud_devops": ["Docker", "Kubernetes"]
  },
  "work_history": [
    {
      "company": "昇銳智慧科技",
      "role": "AI工程師",
      "duration": "2024/10-至今",
      "key_tech": ["YOLO", "OpenCV"]
    }
  ]
}
```

## 🚨 關鍵約束
- 使用 PyPDF2 解析PDF（已確認在requirements.txt）
- 處理中文編碼問題（utf-8）
- 錯誤處理：檔案不存在、解析失敗
- 日誌記錄：記錄解析過程與結果

---
**Phase 1 完成標準：**
✅ src/parsers/resume_parser.py 可運行
✅ data/parsed/parsed_resume.json 產生
✅ tests/test_parser.py 通過所有測試
✅ 解析準確率 ≥ 95%
```

***

## 🚀 **立即執行**

```bash
# 貼入內容（如果檔案已存在則覆蓋）
cat > docs/agent_context/phase1/01_dev_goal_context.md << 'EOF'
[將上方完整內容貼入這裡]
EOF

# 驗證
wc -l docs/agent_context/phase1/01_dev_goal_context.md
# 預期：約 60 行
```