# Phase 2 第5份文件內容 - Phase 執行檢查清單

***

## 📄 **`05_phase_checklist_context.md` 完整內容**

**請將以下內容** **完整複製** **貼到** `docs/agent_context/phase2/05_phase_checklist_context.md`

```markdown
# ✅ Phase 執行檢查清單 - Phase 2 (步驟1B)

## 🎯 **總覽檢查清單**

```
Phase 1 (INFRA)  → ✅ 環境準備完成
Phase 2 (ARCH)   → ✅ 架構設計完成
Phase 3 (CODER)  → ✅ 程式實現完成
Phase 4 (ANALYST) → ✅ 品質驗證完成
```

---

## 📋 **Phase 1: 環境準備檢查清單 (@INFRA)**

### **執行前檢查**
```
□ 當前位置在專案根目錄
□ data/parsed/parsed_resume.json 存在
□ Python 版本 >= 3.8
□ 具備目錄寫入權限
```

### **執行任務**
```
□ mkdir -p data/mock
□ mkdir -p data/providers
□ mkdir -p tests
□ mkdir -p reports
□ touch data/providers/__init__.py
□ touch tests/__init__.py
```

### **執行後驗證**
```
# 1. 檢查目錄結構
tree data/mock data/providers tests reports -L 1

預期輸出：
data/mock
data/providers
├── __init__.py
tests
├── __init__.py
reports

# 2. 檢查必要檔案
ls -lh data/parsed/parsed_resume.json

預期：檔案存在且大小 > 0

# 3. 檢查寫入權限
touch data/mock/test.txt && rm data/mock/test.txt

預期：成功執行
```

### **完成標準**
```
✅ 所有目錄建立成功
✅ __init__.py 檔案存在
✅ parsed_resume.json 可讀取
✅ 目錄寫入權限正常
```

### **常見問題**
```
Q: parsed_resume.json 不存在？
A: 檢查是否已完成 Phase 1 步驟1A (履歷解析)

Q: 權限不足？
A: 執行 chmod -R u+w data/ tests/ reports/

Q: Python 版本過低？
A: 使用 pyenv 或虛擬環境升級到 Python 3.8+
```

---

## 📋 **Phase 2: 架構設計檢查清單 (@ARCH)**

### **執行前檢查**
```
□ Phase 1 已完成
□ data/parsed/parsed_resume.json 可讀取
□ 已閱讀候選人技能清單
```

### **執行任務**
```
□ 分析候選人現有技能
□ 定義目標 LLM 技能清單
□ 設計 Mock 職缺 Schema
□ 定義匹配度計算公式
□ 設計技能缺口分析邏輯
□ 規劃 50 個職缺分佈策略
□ 建立 data/mock_data_schema.json
□ 建立 data/provider_interface_spec.md
```

### **執行後驗證**
```
# 1. 檢查 Schema 檔案
cat data/mock_data_schema.json

必須包含：
□ job_schema (所有必要欄位)
□ match_score_formula (計算公式)
□ distribution_strategy (分佈策略)

# 2. 驗證 JSON 格式
python -m json.tool data/mock_data_schema.json

預期：無語法錯誤

# 3. 檢查接口規範
cat data/provider_interface_spec.md

必須包含：
□ BaseProvider 定義
□ MockProvider 規範
□ CrawlerProvider 預留接口
```

### **完成標準**
```
✅ mock_data_schema.json 格式正確
✅ 包含所有必要欄位定義
✅ 匹配度計算公式明確
✅ 50個職缺分佈策略清晰 (20/20/10)
✅ 接口規範文件完整
```

### **Schema 驗證腳本**
```
# 快速驗證 Schema
import json

with open('data/mock_data_schema.json', 'r') as f:
    schema = json.load(f)

required_keys = ['job_schema', 'match_score_formula', 'distribution_strategy']
assert all(k in schema for k in required_keys), "缺少必要欄位"

job_fields = ['id', 'title', 'company', 'location', 'required_skills', 
              'preferred_skills', 'salary_range', 'match_score', 'skill_gap']
assert all(f in schema['job_schema'] for f in job_fields), "job_schema 欄位不完整"

print("✅ Schema 驗證通過")
```

### **常見問題**
```
Q: 不知道如何定義匹配度公式？
A: 建議使用：overlap_skills / required_skills

Q: 職缺分佈策略不確定？
A: 高匹配(0.7-0.9):20個, 中匹配(0.5-0.7):20個, 低匹配(0.3-0.5):10個

Q: 技能缺口如何計算？
A: skill_gap = required_skills - candidate_skills (集合運算)
```

---

## 📋 **Phase 3: 程式實現檢查清單 (@CODER)**

### **執行前檢查**
```
□ Phase 2 已完成
□ data/mock_data_schema.json 存在
□ data/provider_interface_spec.md 存在
□ data/parsed/parsed_resume.json 可讀取
```

### **執行任務**
```
□ 建立 data/providers/base.py (抽象基類)
□ 建立 data/providers/mock.py (Mock 實現)
□ 建立 data/providers/crawler.py (預留接口)
□ 建立 scripts/generate_mock_jobs.py (生成腳本)
□ 執行生成腳本
□ 檢查生成的 data/mock/jobs.json
```

### **執行後驗證**
```
# 1. 檢查接口層檔案
ls -lh data/providers/

預期輸出：
base.py      ✓
mock.py      ✓
crawler.py   ✓
__init__.py  ✓

# 2. 驗證 Python 語法
python -m py_compile data/providers/base.py
python -m py_compile data/providers/mock.py

預期：無語法錯誤

# 3. 檢查職缺數據
python -c "
import json
with open('data/mock/jobs.json', 'r') as f:
    jobs = json.load(f)
print(f'職缺數量: {len(jobs)}')
print(f'高匹配: {len([j for j in jobs if 0.7 <= j[\"match_score\"] < 0.9])}')
print(f'中匹配: {len([j for j in jobs if 0.5 <= j[\"match_score\"] < 0.7])}')
print(f'低匹配: {len([j for j in jobs if 0.3 <= j[\"match_score\"] < 0.5])}')
"

預期輸出：
職缺數量: 50
高匹配: 20
中匹配: 20
低匹配: 10

# 4. 驗證 JSON 格式
python -m json.tool data/mock/jobs.json > /dev/null

預期：無錯誤
```

### **完成標準**
```
✅ 所有 Provider 類別實現完成
✅ jobs.json 包含 50 個職缺
✅ 匹配度分佈符合要求 (20/20/10)
✅ 所有職缺包含必要欄位
✅ skill_gap 計算正確
✅ JSON 格式正確無誤
```

### **詳細數據驗證腳本**
```
# 完整驗證腳本
import json

# 載入數據
with open('data/mock/jobs.json', 'r') as f:
    jobs = json.load(f)

with open('data/parsed/parsed_resume.json', 'r') as f:
    resume = json.load(f)

candidate_skills = set(resume['skills'])

# 檢查1: 職缺數量
assert len(jobs) == 50, f"職缺數量錯誤: {len(jobs)}"

# 檢查2: 匹配度分佈
high = [j for j in jobs if 0.7 <= j['match_score'] < 0.9]
mid = [j for j in jobs if 0.5 <= j['match_score'] < 0.7]
low = [j for j in jobs if 0.3 <= j['match_score'] < 0.5]
assert len(high) == 20, f"高匹配數量錯誤: {len(high)}"
assert len(mid) == 20, f"中匹配數量錯誤: {len(mid)}"
assert len(low) == 10, f"低匹配數量錯誤: {len(low)}"

# 檢查3: 必要欄位
required_fields = ['id', 'title', 'company', 'location', 'required_skills',
                  'preferred_skills', 'salary_range', 'match_score', 'skill_gap']
for job in jobs:
    for field in required_fields:
        assert field in job, f"職缺 {job.get('id', '未知')} 缺少欄位: {field}"

# 檢查4: skill_gap 正確性
for job in jobs:
    required = set(job['required_skills'])
    expected_gap = required - candidate_skills
    actual_gap = set(job['skill_gap'])
    assert actual_gap == expected_gap, f"職缺 {job['id']} skill_gap 計算錯誤"

print("✅ 所有驗證通過！")
```

### **常見問題**
```
Q: 生成的職缺數量不對？
A: 檢查 generate_mock_jobs.py 中的循環範圍

Q: 匹配度分佈不符合要求？
A: 調整 overlap_count 的隨機範圍

Q: skill_gap 計算錯誤？
A: 確認使用集合運算: set(required) - set(candidate_skills)

Q: JSON 格式錯誤？
A: 使用 json.dump(..., ensure_ascii=False, indent=2)
```

---

## 📋 **Phase 4: 品質驗證檢查清單 (@ANALYST)**

### **執行前檢查**
```
□ Phase 3 已完成
□ data/mock/jobs.json 存在且包含 50 個職缺
□ pytest 已安裝 (pip install pytest)
```

### **執行任務**
```
□ 建立 tests/test_mock_data.py
□ 撰寫測試案例 (5個測試函數)
□ 執行測試: pytest tests/test_mock_data.py -v
□ 生成數據分析報告: reports/mock_data_analysis.md
□ 計算數據品質指標
```

### **執行後驗證**
```
# 1. 執行測試套件
pytest tests/test_mock_data.py -v

預期輸出：
test_job_count PASSED                   [ 20%]
test_match_distribution PASSED          [ 40%]
test_required_fields PASSED             [ 60%]
test_skill_gap_accuracy PASSED          [ 80%]
test_match_score_calculation PASSED     [100%]

5 passed in X.XXs ✅

# 2. 檢查測試覆蓋率
pytest tests/test_mock_data.py --cov=data/mock --cov-report=term

預期：覆蓋率 > 80%

# 3. 驗證分析報告
cat reports/mock_data_analysis.md

必須包含：
□ 數據概覽
□ 技能覆蓋分析
□ 數據品質指標
□ 測試結果摘要
□ 結論與建議
```

### **完成標準**
```
✅ 所有測試 100% 通過
✅ 數據品質報告完整
✅ 無數據異常或錯誤
✅ 測試覆蓋率達標
✅ 分析報告邏輯清晰
```

### **測試執行腳本**
```
#!/bin/bash
# run_tests.sh

echo "🧪 開始執行 Mock 數據品質驗證..."

# 執行測試
pytest tests/test_mock_data.py -v --tb=short

if [ $? -eq 0 ]; then
    echo "✅ 所有測試通過！"
    
    # 生成報告
    python -c "
import json
from datetime import datetime

with open('data/mock/jobs.json', 'r') as f:
    jobs = json.load(f)

report = f'''
# Mock 數據分析報告

**生成時間**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## 數據概覽
- 總職缺數: {len(jobs)}
- 高匹配度 (70-90%): {len([j for j in jobs if 0.7 <= j['match_score'] < 0.9])}
- 中匹配度 (50-70%): {len([j for j in jobs if 0.5 <= j['match_score'] < 0.7])}
- 低匹配度 (30-50%): {len([j for j in jobs if 0.3 <= j['match_score'] < 0.5])}

## 測試結果
✅ 所有測試通過

## 結論
Mock 數據品質達標，可進入下一階段開發。
'''

with open('reports/mock_data_analysis.md', 'w') as f:
    f.write(report)

print('✅ 報告已生成: reports/mock_data_analysis.md')
"
else
    echo "❌ 測試失敗，請檢查錯誤訊息"
    exit 1
fi
```

### **常見問題**
```
Q: pytest 找不到模組？
A: 確認當前目錄在專案根目錄，且 __init__.py 存在

Q: 測試失敗但數據看起來正確？
A: 檢查浮點數比較，使用 abs(a - b) < 0.01

Q: 報告生成失敗？
A: 確認 reports/ 目錄存在且有寫入權限

Q: 測試執行很慢？
A: 正常，50個職缺全面驗證需要時間
```

---

## 🎯 **整體流程驗證**

### **最終檢查清單**
```
# 完整性檢查
□ data/mock/jobs.json (50個職缺) ✓
□ data/providers/base.py ✓
□ data/providers/mock.py ✓
□ data/providers/crawler.py ✓
□ data/mock_data_schema.json ✓
□ data/provider_interface_spec.md ✓
□ tests/test_mock_data.py ✓
□ reports/mock_data_analysis.md ✓

# 功能性檢查
□ 匹配度分佈正確 (20/20/10) ✓
□ 技能缺口計算準確 ✓
□ 所有測試通過 ✓
□ 數據品質達標 ✓
```

### **一鍵驗證腳本**
```
#!/bin/bash
# validate_phase2.sh

echo "🔍 Phase 2 完整驗證..."

# 檢查檔案存在性
files=(
    "data/mock/jobs.json"
    "data/providers/base.py"
    "data/providers/mock.py"
    "data/mock_data_schema.json"
    "tests/test_mock_data.py"
)

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ $file 不存在"
        exit 1
    fi
done

# 執行測試
pytest tests/test_mock_data.py -v

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Phase 2 (步驟1B) 全部完成！"
    echo ""
    echo "下一步："
    echo "  Phase 2 步驟2: 開發職缺解析器"
else
    echo "❌ 驗證失敗，請檢查錯誤"
    exit 1
fi
```

---

## 📊 **進度追蹤表**

| Phase | Agent | 狀態 | 檢查點 | 備註 |
|-------|-------|------|--------|------|
| Phase 1 | INFRA | ⬜ | 目錄結構 | 環境準備 |
| Phase 2 | ARCH | ⬜ | Schema 設計 | 架構定義 |
| Phase 3 | CODER | ⬜ | 50個職缺 | 程式實現 |
| Phase 4 | ANALYST | ⬜ | 測試通過 | 品質驗證 |

**標記說明：**
- ⬜ 未開始
- 🔄 進行中
- ✅ 已完成
- ❌ 失敗/需修正

---

## 🚀 **快速啟動指令**

```
# 啟動 Phase 1
@INFRA 執行 Phase 1 環境準備

# 啟動 Phase 2
@ARCH 執行 Phase 2 架構設計

# 啟動 Phase 3
@CODER 執行 Phase 3 程式實現

# 啟動 Phase 4
@ANALYST 執行 Phase 4 品質驗證

# 一鍵驗證
bash validate_phase2.sh
```

---
**檢查清單準備完成！**
**隨時可以開始執行 Phase 1-4！**
```

***

## 🚀 **立即執行**

```bash
# 貼入內容
nano docs/agent_context/phase2/05_phase_checklist_context.md

# 驗證
wc -l docs/agent_context/phase2/05_phase_checklist_context.md
# 預期：約 460 行
```
