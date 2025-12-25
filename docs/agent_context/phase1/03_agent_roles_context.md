# Multi-Agent 開發架構 - 第3份文件內容

***

## 📄 **`03_agent_roles_context.md` 完整內容**

**請將以下內容** **完整複製** **貼到** `docs/agent_context/phase1/03_agent_roles_context.md`

```markdown
# 👥 Multi-Agent 角色職責 Context - Phase 1 (步驟1A)

## 🎪 **Agent 團隊角色定義**

### **INFRA Agent (基礎設施工程師)**
```
🚀 Phase 1 第一執行者
職責：
├── 建立完整目錄結構：data/, src/, tests/
├── 準備 requirements.txt (PyPDF2 等依賴)
├── 驗證履歷檔案位置：data/raw/resumes/Li-Yue-Jun-v4.pdf
├── 建立空白程式檔案：src/parsers/resume_parser.py
└── 環境檢查：pip install -r requirements.txt

啟動指令："@INFRA 執行 Phase 1 環境準備"
輸出檢查：tree data src ✓
```

### **ARCH Agent (架構師)**
```
📐 Phase 2 結構定義者
職責：
├── 定義數據結構 Schema：data/data_schema.json
├── 定義解析器接口規範：src/parsers/interfaces.py
├── 定義錯誤處理規範：docs/architecture/error_handling.md
└── 驗證 Schema 與目標 JSON 格式一致性

輸入：INFRA完成的目錄結構
啟動指令："@ARCH 定義履歷解析數據結構"
輸出檢查：data/data_schema.json ✓
```

### **CODER Agent (開發工程師)**
```
💻 Phase 3 程式實現者
職責：
├── 實現核心解析邏輯：src/parsers/resume_parser.py
├── PDF → JSON 轉換函數：parse_resume_pdf()
├── 錯誤處理與日誌記錄
├── 測試用範例數據生成：data/parsed/parsed_resume.json
└── 程式碼註解與類型提示

輸入：ARCH定義的 data_schema.json
啟動指令："@CODER 實現 resume_parser.py"
輸出檢查：python src/parsers/resume_parser.py ✓
```

### **ANALYST Agent (測試分析師)**
```
🧪 Phase 4 品質保證者
職責：
├── 撰寫單元測試：tests/test_parser.py
├── 驗證解析準確率：95%+
├── 執行端到端測試：PDF → JSON
├── 生成測試報告：reports/parser_test_report.md
└── 效能測試：<5秒解析時間

輸入：CODER完成的 resume_parser.py
啟動指令："@ANALYST 執行完整測試流程"
輸出檢查：pytest tests/ -v ✓ 100% pass
```

## 📋 **角色間協作協議**

| Agent | 接收者 | 交接檔案 | 驗收條件 |
|-------|--------|----------|----------|
| INFRA | ARCH | `tree data src` | 目錄結構完整 |
| ARCH | CODER | `data/data_schema.json` | JSON Schema 有效 |
| CODER | ANALYST | `src/parsers/resume_parser.py` | 程式可執行無錯 |
| ANALYST | 全體 | `reports/parser_test_report.md` | 測試100%通過 |

## 🎯 **每個Agent的成功標準**

```
INFRA 成功 = 環境準備就緒（tree 輸出正確）
ARCH 成功 = 結構規範清晰（Schema 可驗證）
CODER 成功 = 程式碼可運行（python xxx.py 無錯）
ANALYST 成功 = 測試全通過（pytest 100% pass）
```

## 🚨 **角色切換規則**
```
1. 使用 @角色名 明確指定
2. 每個Agent只處理自己的Phase
3. 完成後明確說「Phase X 完成，交給 @下一角色」
4. 嚴格依流程順序，不跳步驟
```

---
**Phase 1 Agent 團隊就位！**
**啟動順序：INFRA → ARCH → CODER → ANALYST**
```

***

## 🚀 **立即執行**

```bash
# 貼入內容
nano docs/agent_context/phase1/03_agent_roles_context.md

# 驗證
wc -l docs/agent_context/phase1/03_agent_roles_context.md
# 預期：約 70 行
```
