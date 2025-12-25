# Multi-Agent 開發架構 - 第二份文件內容

***

## 📄 **dev_flow_context.md 完整內容**

**請將以下內容** **完整複製** **貼到** `docs/agent_context/phase1/dev_flow_context.md`

```markdown
# 🔄 Multi-Agent 開發流程 Context - Phase 1 (步驟1A)

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
Phase 3: CODER 程式實現 (40分鐘)
↓
Phase 4: ANALYST 測試驗證 (20分鐘)
```

## 🚀 **Phase 1: INFRA Agent 啟動指令**

```
# 1. 建立完整目錄結構
mkdir -p data/{raw/resumes,parsed,mock} src/{parsers,agents} tests/

# 2. 建立必要檔案
touch src/parsers/resume_parser.py
touch requirements.txt
touch data/parsed/parsed_resume.json

# 3. 準備履歷檔案（請確認路徑）
# cp /path/to/Li-Yue-Jun-v4.pdf data/raw/resumes/

# 4. requirements.txt 內容
cat > requirements.txt << 'EOF'
PyPDF2==3.0.1
python-dotenv==1.0.1
langchain-core==0.1.0
EOF

# 5. 驗證結構
tree -d data src
```

**INFRA Agent 完成檢查清單：**
```
□ data/raw/resumes/ 存在
□ src/parsers/resume_parser.py 存在  
□ requirements.txt 有 PyPDF2
□ tree 輸出符合預期
```

## 🏗️ **Phase 2: ARCH Agent 任務**

```
輸入：INFRA完成的目錄結構
任務：
1. 定義 data_schema.json (TypedDict結構)
2. 定義解析器接口規範
3. 定義錯誤處理規範

輸出：
data/data_schema.json
docs/architecture/resume_schema.md
```

## 💻 **Phase 3: CODER Agent 任務**

```
輸入：ARCH定義的 Schema
任務：
1. 實現 src/parsers/resume_parser.py
2. 支援 PDF 解析 → JSON
3. 錯誤處理 + 日誌記錄

輸出：
src/parsers/resume_parser.py (可執行)
data/parsed/parsed_resume.json (範例數據)
```

## 🧪 **Phase 4: ANALYST Agent 任務**

```
輸入：CODER完成的程式碼
任務：
1. 寫 tests/test_parser.py
2. 執行解析測試
3. 驗證 JSON 格式與內容準確性

輸出：
tests/test_parser.py (100% pass)
reports/parser_test_report.md
```

## 📋 **檔案交接規範**

| Phase | Agent | 輸入檔案 | 輸出檔案 | 驗收條件 |
|-------|-------|----------|----------|----------|
| 1 | INFRA | 專案根目錄 | data/ 結構 + requirements.txt | tree 輸出正確 |
| 2 | ARCH | data/ 結構 | data/data_schema.json | JSON Schema 有效 |
| 3 | CODER | data_schema.json | resume_parser.py | python src/parsers/resume_parser.py 無錯 |
| 4 | ANALYST | resume_parser.py | test report | pytest tests/ 100% pass |

## 🚨 關鍵時間節點
```
12:00 - INFRA 完成環境準備
12:20 - ARCH 完成結構定義
13:00 - CODER 完成程式實現
13:20 - ANALYST 完成測試驗證
13:30 - Phase 1 全部完成 ✅
```

---
**Phase 1 啟動指令：**
`@INFRA 執行 Phase 1 環境準備，所有指令已準備好！`
```

***

## 🚀 **立即執行**

```bash
# 貼入內容
nano docs/agent_context/phase1/dev_flow_context.md

# 驗證
wc -l docs/agent_context/phase1/dev_flow_context.md
# 預期：約 80 行
```
