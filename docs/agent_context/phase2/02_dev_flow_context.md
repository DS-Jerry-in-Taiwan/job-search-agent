# Phase 2 第2份文件內容 - 開發流程Context

***

## 📄 **`02_dev_flow_context.md` 完整內容**

**請將以下內容** **完整複製** **貼到** `docs/agent_context/phase2/02_dev_flow_context.md`

```markdown
# 🔄 Multi-Agent 開發流程 Context - Phase 2 (步驟1B)

## 📁 專案根目錄
```
/home/ubuntu/projects/job_search_agent
```

## 🎪 開發流程順序（4階段接力）

```
Phase 1: INFRA 環境準備 (30分鐘)
↓
Phase 2: ARCH 結構定義 (20分鐘) 
↓
Phase 3: CODER 程式實現 (60分鐘)
↓
Phase 4: ANALYST 測試驗證 (20分鐘)
```

## 🚀 **Phase 1: INFRA Agent 啟動指令**

```
# 1. 建立完整目錄結構
mkdir -p data/mock data/providers/{base,mock,crawler} tests/

# 2. 建立必要檔案
touch data/providers/base.py
touch data/providers/mock.py
touch data/providers/crawler.py
touch data/providers/__init__.py

# 3. 準備輸入數據
# 確認 data/parsed/parsed_resume.json 存在

# 4. 驗證結構
tree data/mock data/providers
```

**INFRA Agent 完成檢查清單：**
```
□ data/mock/ 存在
□ data/providers/ 結構完整
□ data/parsed/parsed_resume.json 可讀取
□ tree 輸出符合預期
```

## 🏗️ **Phase 2: ARCH Agent 任務**

```
輸入：INFRA完成的目錄結構
任務：
1. 定義 Mock 數據結構 Schema
2. 定義職缺匹配度計算規範
3. 定義數據接口抽象層規範
4. 讀取 parsed_resume.json，分析技能缺口

輸出：
data/mock_data_schema.json
docs/architecture/mock_data_spec.md
```

**ARCH 關鍵設計：**
```
{
  "候選人現有技能": ["Python", "PyTorch", "Docker", "Kubernetes"],
  "目標職位技能": ["LangChain", "LangGraph", "RAG", "OpenAI API"],
  "技能缺口": ["LangChain", "LangGraph", "RAG"],
  "匹配度公式": "現有技能重疊數 / 職位必備技能總數"
}
```

## 💻 **Phase 3: CODER Agent 任務**

```
輸入：ARCH定義的 Schema + parsed_resume.json
任務：
1. 實現數據接口抽象層
   - data/providers/base.py (抽象基類)
   - data/providers/mock.py (Mock實現)
   - data/providers/crawler.py (預留接口)

2. 生成 Mock 職缺數據
   - 讀取候選人技能清單
   - 生成50個職缺（高20/中20/低10）
   - 計算 match_score 與 skill_gap

3. 生成輔助數據
   - transfer_matrix.json
   - market_stats.json

輸出：
data/mock/jobs.json (50個職缺)
data/mock/transfer_matrix.json
data/mock/market_stats.json
data/providers/*.py (接口層程式碼)
```

**CODER 職缺生成邏輯：**
```
# 高匹配職缺（70-90%）：20個
# required_skills: 候選人已有技能（5個）
# preferred_skills: 包含少量LLM技能（2-3個）
# match_score: 0.70 - 0.90

# 中匹配職缺（50-70%）：20個
# required_skills: 50%候選人已有 + 50%新技能
# preferred_skills: LLM技能為主（3-4個）
# match_score: 0.50 - 0.70

# 低匹配職缺（30-50%）：10個
# required_skills: 主要是LLM新技能
# preferred_skills: 進階LLM技能
# match_score: 0.30 - 0.50
```

## 🧪 **Phase 4: ANALYST Agent 任務**

```
輸入：CODER完成的 Mock 數據
任務：
1. 撰寫 tests/test_mock_data.py
2. 驗證職缺數量（應為50個）
3. 驗證匹配度分佈（高20/中20/低10）
4. 驗證 JSON 格式正確性
5. 驗證技能覆蓋率（100%）
6. 生成數據分析報告

輸出：
tests/test_mock_data.py (100% pass)
reports/mock_data_analysis.md
```

**ANALYST 驗證項目：**
```
# 1. 職缺數量
assert len(jobs) == 50

# 2. 匹配度分佈
high_match = [j for j in jobs if j['match_score'] >= 0.7]
assert len(high_match) == 20

# 3. 必要欄位完整
required_fields = ['id', 'title', 'required_skills', 'match_score']
assert all(field in job for field in required_fields for job in jobs)

# 4. 技能覆蓋
all_skills = set()
for job in jobs:
    all_skills.update(job['required_skills'] + job['preferred_skills'])
assert '候選人現有技能' in all_skills
assert 'LLM新技能' in all_skills
```

## 📋 **檔案交接規範**

| Phase | Agent | 輸入檔案 | 輸出檔案 | 驗收條件 |
|-------|-------|----------|----------|----------|
| 1 | INFRA | 專案根目錄 | data/mock/ + providers/ | tree 輸出正確 |
| 2 | ARCH | data/parsed/parsed_resume.json | mock_data_schema.json | Schema 完整定義 |
| 3 | CODER | mock_data_schema.json | jobs.json (50個) | JSON 格式正確 |
| 4 | ANALYST | jobs.json | test report | pytest 100% pass |

## 🚨 關鍵時間節點
```
14:25 - INFRA 完成環境準備
14:45 - ARCH 完成結構定義
15:45 - CODER 完成數據生成
16:05 - ANALYST 完成測試驗證
16:15 - Phase 2 全部完成 ✅
```

---
**Phase 2 啟動指令：**
`@INFRA 執行 Phase 1 環境準備，建立 Mock 數據目錄結構！`
```

***

## 🚀 **立即執行**

```bash
# 貼入內容
nano docs/agent_context/phase2/02_dev_flow_context.md

# 驗證
wc -l docs/agent_context/phase2/02_dev_flow_context.md
# 預期：約 130 行
```
