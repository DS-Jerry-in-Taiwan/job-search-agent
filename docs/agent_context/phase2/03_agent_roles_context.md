# Phase 2 第3份文件內容 - Agent角色職責Context

***

## 📄 **`03_agent_roles_context.md` 完整內容**

**請將以下內容** **完整複製** **貼到** `docs/agent_context/phase2/03_agent_roles_context.md`

```markdown
# 👥 Multi-Agent 角色職責 Context - Phase 2 (步驟1B)

## 🎪 **Agent 團隊角色定義**

### **INFRA Agent (基礎設施工程師)**
```
🚀 Phase 1 第一執行者
職責：
├── 建立 Mock 數據目錄結構：data/mock/
├── 建立數據接口抽象層：data/providers/
├── 確認輸入檔案：data/parsed/parsed_resume.json
└── 環境檢查：目錄權限、檔案存在性

啟動指令："@INFRA 執行 Phase 1 環境準備，建立 Mock 數據結構"
輸出檢查：tree data/mock data/providers ✓
```

### **ARCH Agent (架構師)**
```
📐 Phase 2 結構定義者
職責：
├── 定義 Mock 數據 Schema：data/mock_data_schema.json
├── 分析候選人技能缺口（讀取 parsed_resume.json）
├── 定義職缺匹配度計算公式
├── 定義數據接口抽象層規範
└── 規劃50個職缺的匹配度分佈策略

輸入：data/parsed/parsed_resume.json
啟動指令："@ARCH 分析候選人技能，定義 Mock 職缺數據結構"
輸出檢查：data/mock_data_schema.json ✓
```

### **CODER Agent (開發工程師)**
```
💻 Phase 3 程式實現者
職責：
├── 實現數據接口抽象層
│   ├── data/providers/base.py (抽象基類)
│   ├── data/providers/mock.py (Mock實現)
│   └── data/providers/crawler.py (預留接口)
├── 生成50個 Mock 職缺數據
│   ├── 高匹配度職缺（70-90%）：20個
│   ├── 中匹配度職缺（50-70%）：20個
│   └── 低匹配度職缺（30-50%）：10個
├── 計算 match_score 與 skill_gap
├── 生成轉移矩陣：transfer_matrix.json
└── 生成市場統計：market_stats.json

輸入：data/mock_data_schema.json + parsed_resume.json
啟動指令："@CODER 生成50個 Mock 職缺數據與接口層"
輸出檢查：
- data/mock/jobs.json (50個職缺) ✓
- data/providers/*.py ✓
```

### **ANALYST Agent (測試分析師)**
```
🧪 Phase 4 品質保證者
職責：
├── 撰寫數據驗證測試：tests/test_mock_data.py
├── 驗證職缺數量（應為50個）
├── 驗證匹配度分佈（高20/中20/低10）
├── 驗證必要欄位完整性
├── 驗證技能覆蓋率（100%）
├── 生成數據分析報告
└── 計算數據品質指標

輸入：data/mock/jobs.json
啟動指令："@ANALYST 執行 Mock 數據完整驗證"
輸出檢查：
- pytest tests/test_mock_data.py -v ✓ 100% pass
- reports/mock_data_analysis.md ✓
```

## 📋 **角色間協作協議**

| Agent | 接收者 | 交接檔案 | 驗收條件 |
|-------|--------|----------|----------|
| INFRA | ARCH | `tree data/mock data/providers` | 目錄結構完整 |
| ARCH | CODER | `data/mock_data_schema.json` | Schema 定義完整 |
| CODER | ANALYST | `data/mock/jobs.json` (50個) | JSON 格式正確 |
| ANALYST | 全體 | `reports/mock_data_analysis.md` | 測試100%通過 |

## 🎯 **每個Agent的成功標準**

```
INFRA 成功 = 目錄結構建立完成（tree 輸出正確）
ARCH 成功 = Schema 定義清晰（包含匹配度計算公式）
CODER 成功 = 50個職缺生成（匹配度分佈合理）
ANALYST 成功 = 測試全通過（數據品質達標）
```

## 🔍 **關鍵驗證點**

### **ARCH 驗證點**
```
{
  "候選人技能": ["Python", "PyTorch", "Docker"],
  "目標LLM技能": ["LangChain", "RAG", "OpenAI API"],
  "技能缺口": ["LangChain", "RAG"],
  "匹配度公式": "重疊技能數 / 必備技能總數"
}
```

### **CODER 驗證點**
```
# 職缺匹配度分佈檢查
jobs = load_jobs()
high = [j for j in jobs if 0.7 <= j['match_score'] < 0.9]
mid = [j for j in jobs if 0.5 <= j['match_score'] < 0.7]
low = [j for j in jobs if 0.3 <= j['match_score'] < 0.5]

assert len(high) == 20  # 高匹配
assert len(mid) == 20   # 中匹配
assert len(low) == 10   # 低匹配
```

### **ANALYST 驗證點**
```
# 必要欄位檢查
required_fields = [
    'id', 'title', 'company', 'location',
    'required_skills', 'preferred_skills',
    'match_score', 'skill_gap', 'salary_range'
]

# 技能覆蓋率檢查
候選人現有技能 ⊆ 所有職缺required_skills聯集
目標LLM技能 ⊆ 所有職缺preferred_skills聯集
```

## 🚨 **角色切換規則**
```
1. 使用 @角色名 明確指定
2. 每個Agent只處理自己的Phase
3. 完成後明確說「Phase X 完成，交給 @下一角色」
4. 嚴格依流程順序，不跳步驟
5. 遇到問題時說明並請求人類協助
```

---
**Phase 2 Agent 團隊就位！**
**啟動順序：INFRA → ARCH → CODER → ANALYST**
```

***

## 🚀 **立即執行**

```bash
# 貼入內容
nano docs/agent_context/phase2/03_agent_roles_context.md

# 驗證
wc -l docs/agent_context/phase2/03_agent_roles_context.md
# 預期：約 130 行
```
