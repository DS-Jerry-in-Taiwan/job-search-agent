# Multi-Agent 第5份文件內容 - 驗證清單

***

## 📄 **`05_validation_checklist.md` 完整內容**

**請將以下內容** **完整複製** **貼到** `docs/agent_context/phase1/05_validation_checklist.md`

```markdown
# ✅ Phase 1 驗證清單 - 履歷解析模組

## 📊 驗證總覽
```
專案階段：Phase 1 (Day 1 步驟1A)
驗證目標：確保履歷解析模組完整可用
驗證時機：Step 8 (Agent執行完成後)
```

---

## 🔍 Phase 1: INFRA 驗證

| 驗證項 | 驗證指令 | 通過標準 |
|--------|----------|----------|
| 目錄結構 | `tree data src tests/` | 所有目錄存在 |
| 履歷檔案 | `ls data/raw/resumes/Li-Yue-Jun-v4.pdf` | 檔案存在 |
| 依賴安裝 | `pip list \| grep PyPDF2` | PyPDF2 已安裝 |
| 解析器檔案 | `ls src/parsers/resume_parser.py` | 檔案存在且非空 |

**執行驗證：**
```
# INFRA 驗證腳本
echo "🔍 驗證 Phase 1 - INFRA"
tree -d data src tests/ && \
ls data/raw/resumes/Li-Yue-Jun-v4.pdf && \
pip list | grep -q PyPDF2 && \
[ -s src/parsers/resume_parser.py ] && \
echo "✅ INFRA 驗證通過"
```

---

## 🏗️ Phase 2: ARCH 驗證

| 驗證項 | 驗證指令 | 通過標準 |
|--------|----------|----------|
| Schema定義 | `cat data/data_schema.json` | JSON檔案存在 |
| JSON格式 | `python -m json.tool data/data_schema.json` | 無語法錯誤 |
| 必要欄位 | 檢查 name, skills, work_history | 欄位完整 |

**執行驗證：**
```
# ARCH 驗證腳本
echo "🔍 驗證 Phase 2 - ARCH"
[ -f data/data_schema.json ] && \
python -m json.tool data/data_schema.json > /dev/null && \
echo "✅ ARCH 驗證通過"
```

---

## 💻 Phase 3: CODER 驗證

| 驗證項 | 驗證指令 | 通過標準 |
|--------|----------|----------|
| 程式執行 | `python src/parsers/resume_parser.py` | 無錯誤執行 |
| 輸出產生 | `ls data/parsed/parsed_resume.json` | JSON檔案產生 |
| 輸出格式 | `python -m json.tool data/parsed/parsed_resume.json` | JSON格式正確 |
| 編碼處理 | 檢查中文字符顯示 | UTF-8正確 |

**執行驗證：**
```
# CODER 驗證腳本
echo "🔍 驗證 Phase 3 - CODER"
python src/parsers/resume_parser.py && \
[ -f data/parsed/parsed_resume.json ] && \
python -m json.tool data/parsed/parsed_resume.json > /dev/null && \
echo "✅ CODER 驗證通過"
```

---

## 🧪 Phase 4: ANALYST 驗證

| 驗證項 | 驗證指令 | 通過標準 |
|--------|----------|----------|
| 測試檔案 | `ls tests/test_parser.py` | 測試檔案存在 |
| 單元測試 | `pytest tests/test_parser.py -v` | 100% pass |
| 測試覆蓋 | `pytest --cov=src/parsers tests/` | ≥80% |
| 測試報告 | `cat reports/parser_test_report.md` | 報告完整 |

**執行驗證：**
```
# ANALYST 驗證腳本
echo "🔍 驗證 Phase 4 - ANALYST"
[ -f tests/test_parser.py ] && \
pytest tests/test_parser.py -v && \
echo "✅ ANALYST 驗證通過"
```

---

## 📈 整體品質指標驗證

| 指標 | 目標值 | 驗證方法 |
|------|--------|----------|
| 解析準確率 | ≥95% | 人工檢查 parsed_resume.json |
| 執行時間 | <5秒 | `time python src/parsers/resume_parser.py` |
| 錯誤率 | 0% | 無 Exception 拋出 |
| 檔案大小 | <5MB | `ls -lh data/parsed/parsed_resume.json` |

---

## 🚀 一鍵完整驗證腳本

```
#!/bin/bash
# validate_phase1.sh

echo "=========================================="
echo "Phase 1 完整驗證開始"
echo "=========================================="

# Phase 1: INFRA
tree -d data src tests/ && ls data/raw/resumes/Li-Yue-Jun-v4.pdf && \
pip list | grep -q PyPDF2 && [ -s src/parsers/resume_parser.py ] && \
echo "✅ Phase 1 - INFRA 通過" || echo "❌ Phase 1 - INFRA 失敗"

# Phase 2: ARCH
[ -f data/data_schema.json ] && python -m json.tool data/data_schema.json > /dev/null && \
echo "✅ Phase 2 - ARCH 通過" || echo "❌ Phase 2 - ARCH 失敗"

# Phase 3: CODER
python src/parsers/resume_parser.py && [ -f data/parsed/parsed_resume.json ] && \
python -m json.tool data/parsed/parsed_resume.json > /dev/null && \
echo "✅ Phase 3 - CODER 通過" || echo "❌ Phase 3 - CODER 失敗"

# Phase 4: ANALYST
[ -f tests/test_parser.py ] && pytest tests/test_parser.py -v && \
echo "✅ Phase 4 - ANALYST 通過" || echo "❌ Phase 4 - ANALYST 失敗"

echo "=========================================="
echo "✅ Phase 1 完整驗證完成"
echo "=========================================="
```

---

## ✅ 驗證完成標準

**Phase 1 完整通過條件：**
```
□ INFRA 4項驗證全部通過
□ ARCH 3項驗證全部通過
□ CODER 4項驗證全部通過
□ ANALYST 4項驗證全部通過
□ 品質指標達標
□ 一鍵腳本執行無錯誤
```

**驗證通過後：**
進入 Step 9，填寫 `06_delivery_record.md`
```

***

## 🚀 **立即執行**

```bash
# 貼入內容
nano docs/agent_context/phase1/05_validation_checklist.md

# 驗證
wc -l docs/agent_context/phase1/05_validation_checklist.md
# 預期：約 120 行
```
