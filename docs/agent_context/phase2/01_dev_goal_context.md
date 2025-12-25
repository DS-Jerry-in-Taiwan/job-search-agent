# Phase 2 第1份文件內容 - 開發目標Context（繁體中文版）

***

## 📄 **`01_dev_goal_context.md` 完整內容**

**請將以下內容** **完整複製** **貼到** `docs/agent_context/phase2/01_dev_goal_context.md`

```markdown
# 🎯 Multi-Agent 開發目標 Context - Phase 2 (步驟1B)

## 📁 專案環境
```
專案根目錄：/home/ubuntu/projects/job_search_agent
當前階段：Day 1 步驟1B - Mock職缺生成
目標檔案：data/mock/jobs.json + data/providers/
輸入檔案：data/parsed/parsed_resume.json (Phase 1產出)
輸出檔案：data/mock/ 下所有Mock數據
```

## 🎪 Multi-Agent 團隊組成

| Agent | 角色 | 職責 | 目標產出 |
|-------|------|------|----------|
| **ARCH** | 架構師 | 定義Mock數據結構、接口規範 | `data/mock_data_schema.json` |
| **CODER** | 開發工程師 | 生成Mock數據、實現數據接口層 | `data/mock/*.json` + `data/providers/` |
| **ANALYST** | 測試分析師 | 驗證數據完整性、匹配度計算 | `tests/test_mock_data.py` |
| **INFRA** | 基礎設施工程師 | 目錄結構、數據接口抽象層 | `data/mock/` + `data/providers/` |

## 📊 階段性KPI

| 指標 | 目標值 | 驗收標準 |
|------|--------|----------|
| **職缺數量** | 50個 | jobs.json 包含50個職缺 |
| **匹配度分佈** | 高20/中20/低10 | match_score 合理分佈 |
| **技能覆蓋率** | 100% | 涵蓋履歷所有技能 |
| **數據格式** | JSON標準 | 可直接被Agent1讀取 |
| **接口可擴展性** | 預留爬蟲接口 | providers/ 抽象層完整 |

## 🎯 具體開發目標

```
1. 分析 parsed_resume.json，提取候選人技能缺口
2. 生成50個職缺，匹配度分佈：
   - 高匹配(70-90%)：20個
   - 中匹配(50-70%)：20個
   - 低匹配(30-50%)：10個
3. 建立數據接口抽象層（Mock + 預留爬蟲）
4. 準備轉移矩陣與市場統計數據
5. 為 Agent 2（市場分析）提供標準化輸入
```

## 📋 期望輸出格式

### **jobs.json (50個職缺)**
```
[
  {
    "id": "job_001",
    "title": "LLM應用工程師",
    "company": "某科技公司",
    "location": "台北市",
    "required_skills": ["Python", "Docker", "Kubernetes"],
    "preferred_skills": ["LangChain", "RAG", "OpenAI API"],
    "experience_years": 5,
    "salary_range": ,
    "match_score": 0.75,
    "skill_gap": ["LangChain", "RAG"],
    "description": "開發LLM應用系統",
    "posted_date": "2025-12",
    "category": "LLM應用工程師"
  }
]
```

### **transfer_matrix.json**
```
{
  "AI工程師": {
    "LLM應用工程師": {"rate": 0.85, "time_months": 3},
    "MLOps工程師": {"rate": 0.90, "time_months": 2}
  }
}
```

### **market_stats.json**
```
{
  "llm_engineer": {
    "demand": "high",
    "avg_salary": 70000,
    "growth_rate": 0.35
  }
}
```

## 🚨 關鍵約束

- 職缺必須基於真實台灣市場（台北/新北/新竹/桃園）
- match_score 計算基於技能重疊度
- skill_gap 必須列出候選人缺少的關鍵技能
- salary_range 需考慮候選人期望（100-125萬/年）
- 數據接口層必須可擴展（預留爬蟲替換）
- 所有JSON格式必須符合 data_schema

---
**Phase 2 完成標準：**
✅ data/mock/jobs.json 產生（50個職缺）
✅ data/mock/transfer_matrix.json 產生
✅ data/mock/market_stats.json 產生
✅ data/providers/ 接口層建立
✅ tests/test_mock_data.py 通過所有測試
✅ 職缺匹配度分佈合理
```

***

## 🚀 **立即執行**

```bash
# 貼入內容
nano docs/agent_context/phase2/01_dev_goal_context.md

# 驗證
wc -l docs/agent_context/phase2/01_dev_goal_context.md
# 預期：約 100 行
```
