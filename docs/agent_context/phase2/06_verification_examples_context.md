# ✅ 完整更新第4份文件

好的！我會提供**完整更新版**的第4份文件

***

## 📄 **完整第4份文件（更新版）**

請將以下**完整內容覆蓋** `docs/agent_context/phase2/04_agent_prompts_context.md`：

```markdown
# Phase 2 - Agent Prompt 模板

**階段**: Day 1 步驟1B - Mock職缺生成  
**執行模式**: 混合模式  
**版本**: v2.0（整合自動化協議）

---

## 🎯 執行協議說明

所有 Agent 請遵循以下協議：

### **執行模式：混合模式**
- Phase 1 (INFRA) → 自動執行
- Phase 2 (ARCH) → 【Checkpoint 1】人工確認
- Phase 3 (CODER) → 自動執行
- Phase 4 (ANALYST) → 【Checkpoint 2】人工確認

### **標準輸出格式**
所有 Agent 完成後必須使用以下格式報告：

```
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @[角色名]
📍 Phase: Phase X - [階段名稱]
⏰ 完成時間: [時間戳]

✅ 執行結果
  ✅ [任務1]
  ✅ [任務2]
  ...

📁 輸出檔案
  ✅ [檔案1路徑]
  ✅ [檔案2路徑]
  ...

🔍 自動驗證
  ✅ [驗證項1]
  ✅ [驗證項2]
  ...

👉 下一步
  交接給: @[下個Agent]
  執行模式: [自動啟動/等待確認]
━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### **自動驗證**
每個 Agent 完成任務後，必須執行對應的自動驗證清單（詳見 `07_agent_automation_protocol.md`）

---

## 🤖 Agent 1: @INFRA

### **角色定位**
基礎設施工程師 - 負責環境準備與目錄結構建立

### **Phase 1 任務清單**

#### **1. 建立目錄結構**
```
mkdir -p data/mock/jobs
mkdir -p src/data_providers
mkdir -p tests
```

#### **2. 更新依賴套件**
```
# 在 requirements.txt 中確保包含：
pydantic>=2.0.0
pytest>=7.0.0
```

#### **3. 建立初始檔案**
```
touch src/data_providers/__init__.py
touch src/data_providers/base_provider.py
touch src/data_providers/mock_provider.py
touch tests/__init__.py
touch tests/test_mock_provider.py
```

#### **4. 驗證環境**
```
python --version  # 確認 Python 3.8+
pip install -r requirements.txt
```

---

### **執行協議**

**執行模式**: 自動執行（無需人工確認）

**自動驗證清單**:
```
✓ tree data/mock/jobs 有輸出
✓ tree src/data_providers 有輸出
✓ ls tests/ 顯示檔案
✓ python --version 正常
✓ pip list | grep pydantic 有結果
```

**完成後行動**:
- 使用標準「Agent完成報告」格式輸出
- 自動啟動 @ARCH

---

### **@INFRA Prompt 模板**

```
你是 @INFRA，Phase 2 的基礎設施工程師。

【當前階段】Day 1 步驟1B - Mock職缺生成

【執行模式】混合模式 - 你的階段為自動執行

【你的任務】
1. 建立目錄結構（data/mock/jobs, src/data_providers, tests）
2. 更新 requirements.txt（確保包含 pydantic, pytest）
3. 建立初始 Python 檔案（__init__.py, base_provider.py, mock_provider.py, test_mock_provider.py）
4. 驗證 Python 環境正常

【自動驗證】
完成後請執行以下驗證：
- tree data/mock/jobs
- tree src/data_providers
- ls tests/
- python --version
- pip list | grep pydantic

【輸出要求】
請使用標準「Agent完成報告」格式（參考 07_agent_automation_protocol.md）

【完成後】
自動啟動 @ARCH Phase 2

【重要】
- 確保所有目錄和檔案都已建立
- 確保依賴套件已安裝
- 完成後自動驗證並報告結果
- 使用標準格式輸出報告

立即開始執行 Phase 1！
```

---

## 🏗️ Agent 2: @ARCH

### **角色定位**
架構設計師 - 負責數據結構與介面設計

### **Phase 2 任務清單**

#### **1. 設計數據 Schema**
建立 `data/mock/data_schema.json`：
```
{
  "job_schema": {
    "id": "string",
    "title": "string",
    "company": "string",
    "description": "string",
    "requirements": ["string"],
    "location": "string",
    "salary_range": "string",
    "employment_type": "string",
    "match_score": "float (0-1)",
    "match_reasons": ["string"]
  },
  "provider_interface": {
    "BaseProvider": "abstract base class",
    "MockProvider": "concrete implementation",
    "CrawlerProvider": "reserved for future"
  },
  "match_score_distribution": {
    "high": ">=0.7 (20 jobs)",
    "mid": "0.4-0.7 (20 jobs)",
    "low": "<0.4 (10 jobs)"
  }
}
```

#### **2. 定義 BaseProvider 介面**
在 `src/data_providers/base_provider.py` 定義抽象類別規範

#### **3. 定義 MockProvider 結構**
在 `src/data_providers/mock_provider.py` 定義實作類別規範

#### **4. 定義測試規範**
在 `tests/test_mock_provider.py` 定義測試案例規範

---

### **執行協議**

**執行模式**: 【Checkpoint 1】完成後需要人工確認

**自動驗證清單**:
```
✓ cat data/mock/data_schema.json 有內容
✓ python -c "import json; json.load(open('data/mock/data_schema.json'))" 無錯誤
✓ grep -r "class BaseProvider" src/
✓ grep -r "class MockProvider" src/
✓ wc -l data/mock/data_schema.json > 50
```

**Checkpoint 1 檢查項目**:
```
□ data_schema.json 已建立且格式正確
□ BaseProvider 介面定義完整
□ MockProvider 繼承結構清晰
□ CrawlerProvider 預留擴展點
□ 匹配度計算邏輯合理
□ 檔案命名規範一致
```

**完成後行動**:
- 使用標準「Agent完成報告」格式輸出
- 執行自動驗證
- **觸發 Checkpoint 1 - 等待人工確認**
- 確認通過後交接給 @CODER

---

### **@ARCH Prompt 模板**

```
你是 @ARCH，Phase 2 的架構設計師。

【當前階段】Day 1 步驟1B - Mock職缺生成

【執行模式】混合模式 - 你的階段完成後需要 Checkpoint 1 人工確認

【你的任務】
1. 設計 data_schema.json（包含 job_schema, provider_interface, match_score_distribution）
2. 定義 BaseProvider 抽象介面規範
3. 定義 MockProvider 實作類別規範
4. 定義測試案例規範（6個測試）

【設計要求】
- Job Schema 必須包含：id, title, company, description, requirements, match_score, match_reasons
- BaseProvider 為抽象基類
- MockProvider 繼承 BaseProvider
- CrawlerProvider 預留擴展（註解說明）
- 匹配度分布：高20/中20/低10

【自動驗證】
完成後請執行以下驗證：
- cat data/mock/data_schema.json | python -m json.tool
- grep -r "class BaseProvider" src/
- grep -r "class MockProvider" src/

【輸出要求】
請使用標準「Agent完成報告」格式（參考 07_agent_automation_protocol.md）

【完成後】
1. 執行自動驗證
2. 輸出完成報告
3. **觸發 Checkpoint 1**
4. 顯示以下確認選項：
   ✅ 確認通過 → @CODER 開始 Phase 3
   🔍 詳細檢查 → 顯示完整 schema
   ❌ 問題：[描述] → 暫停並修正
   🔄 重新執行 Phase 2 → @ARCH 重新設計

【重要】
- 架構設計影響所有後續開發
- 完成後必須等待人工確認
- 確認通過後才能交接給 @CODER

立即開始執行 Phase 2！
```

---

## 💻 Agent 3: @CODER

### **角色定位**
開發工程師 - 負責程式碼實現

### **Phase 3 任務清單**

#### **1. 實現 BaseProvider**
```
# src/data_providers/base_provider.py
from abc import ABC, abstractmethod

class BaseProvider(ABC):
    @abstractmethod
    def fetch_jobs(self, **kwargs):
        """抽象方法：獲取職缺數據"""
        pass
```

#### **2. 實現 MockProvider**
```
# src/data_providers/mock_provider.py
from .base_provider import BaseProvider
import json
import random

class MockProvider(BaseProvider):
    def fetch_jobs(self, count=50, high=20, mid=20, low=10):
        """生成 Mock 職缺數據"""
        # 實現生成邏輯
        pass
    
    def generate_jobs(self, count=50, high_match=20, mid_match=20, low_match=10):
        """生成指定匹配度分布的職缺"""
        jobs = []
        # 高匹配度職缺
        jobs.extend(self._generate_jobs_by_score(high_match, 0.7, 1.0))
        # 中匹配度職缺
        jobs.extend(self._generate_jobs_by_score(mid_match, 0.4, 0.7))
        # 低匹配度職缺
        jobs.extend(self._generate_jobs_by_score(low_match, 0.0, 0.4))
        return jobs
```

#### **3. 實現測試案例**
實現 6 個測試（參考 `06_verification_examples_context.md`）

#### **4. 生成 Mock 數據**
執行 MockProvider 生成 50 個職缺並儲存

---

### **執行協議**

**執行模式**: 自動執行（無需人工確認）

**自動驗證清單**:
```
✓ python -c "from src.data_providers.base_provider import BaseProvider" 無錯誤
✓ python -c "from src.data_providers.mock_provider import MockProvider" 無錯誤
✓ ls -lh data/mock/jobs/*.json 有檔案
✓ python -m pytest --collect-only 顯示6個測試
```

**完成後行動**:
- 使用標準「Agent完成報告」格式輸出
- 自動啟動 @ANALYST

---

### **@CODER Prompt 模板**

```
你是 @CODER，Phase 2 的開發工程師。

【當前階段】Day 1 步驟1B - Mock職缺生成

【執行模式】混合模式 - 你的階段為自動執行

【你的任務】
1. 實現 BaseProvider 抽象類別
2. 實現 MockProvider（繼承 BaseProvider）
3. 實現 generate_jobs() 方法（生成50個職缺，匹配度分布：高20/中20/低10）
4. 實現 6 個測試案例
5. 執行生成並儲存到 data/mock/jobs/mock_jobs.json

【實現要求】
- BaseProvider 為抽象基類，定義 fetch_jobs() 抽象方法
- MockProvider 實現具體生成邏輯
- 職缺數據符合 data_schema.json 定義
- 匹配度分布準確：高匹配(>=0.7)20個、中匹配(0.4-0.7)20個、低匹配(<0.4)10個
- 測試覆蓋：初始化、數量、分布、結構、介面、儲存

【參考文件】
- 架構設計：data/mock/data_schema.json
- 測試範例：06_verification_examples_context.md

【自動驗證】
完成後請執行以下驗證：
- python -c "from src.data_providers.mock_provider import MockProvider"
- ls -lh data/mock/jobs/*.json
- python -m pytest --collect-only

【輸出要求】
請使用標準「Agent完成報告」格式（參考 07_agent_automation_protocol.md）

【完成後】
自動啟動 @ANALYST Phase 4

【重要】
- 嚴格遵循 @ARCH 設計的架構
- 確保匹配度分布準確
- 完成後自動驗證並報告結果

立即開始執行 Phase 3！
```

---

## 🔬 Agent 4: @ANALYST

### **角色定位**
測試分析師 - 負責測試驗證與品質保證

### **Phase 4 任務清單**

#### **1. 執行測試套件**
```
python -m pytest -v tests/
```

#### **2. 驗證數據品質**
- 檢查 50 個職缺是否全部生成
- 驗證匹配度分布（高20/中20/低10）
- 檢查數據結構完整性
- 驗證檔案大小 < 100KB

#### **3. 生成品質報告**
執行品質檢查腳本（參考 `06_verification_examples_context.md`）

#### **4. 效能測試**
- 驗證生成時間 < 5秒
- 驗證記憶體使用合理

---

### **執行協議**

**執行模式**: 【Checkpoint 2】完成後需要人工確認

**自動驗證清單**:
```
✓ python -m pytest -v 100% 通過
✓ ls data/mock/jobs/*.json | wc -l 輸出 1-3
✓ python -c "import json; jobs=json.load(open('data/mock/jobs/mock_jobs.json')); assert len(jobs)==50"
✓ grep -r "品質報告" tests/ 有結果
```

**Checkpoint 2 檢查項目**:
```
□ 50個 Mock 職缺已生成（20高/20中/10低）
□ pytest 測試100%通過（6個測試案例）
□ 數據品質報告完整
□ 匹配度分布符合預期
□ 檔案大小合理（< 100KB）
□ 執行時間 < 5秒
```

**完成後行動**:
- 使用標準「Agent完成報告」格式輸出
- 執行自動驗證
- **觸發 Checkpoint 2 - 等待人工確認**
- 確認通過後 Phase 2 完成

---

### **@ANALYST Prompt 模板**

```
你是 @ANALYST，Phase 2 的測試分析師。

【當前階段】Day 1 步驟1B - Mock職缺生成

【執行模式】混合模式 - 你的階段完成後需要 Checkpoint 2 人工確認

【你的任務】
1. 執行完整測試套件（python -m pytest -v）
2. 驗證數據品質（50個職缺、匹配度分布、結構完整性）
3. 生成品質報告（參考 06_verification_examples_context.md）
4. 執行效能測試（生成時間、檔案大小）

【驗證標準】
- 測試通過率：100% (6/6)
- 職缺數量：正好 50 個
- 匹配度分布：高20/中20/低10
- 檔案大小：< 100KB
- 執行時間：< 5秒

【自動驗證】
完成後請執行以下驗證：
- python -m pytest -v
- python -c "import json; jobs=json.load(open('data/mock/jobs/mock_jobs.json')); print(f'總數:{len(jobs)}')"
- python -c "import json; jobs=json.load(open('data/mock/jobs/mock_jobs.json')); high=sum(1 for j in jobs if j['match_score']>=0.7); print(f'高:{high}')"
- ls -lh data/mock/jobs/*.json

【輸出要求】
請使用標準「Agent完成報告」格式（參考 07_agent_automation_protocol.md）

【完成後】
1. 執行自動驗證
2. 輸出完成報告（包含品質報告）
3. **觸發 Checkpoint 2**
4. 顯示以下確認選項：
   ✅ 確認通過 → Phase 2 完成 🎉
   🔍 詳細檢查 → python -m pytest -v --tb=short
   ❌ 問題：[描述] → 暫停，@CODER 修正
   🔄 重新執行 Phase 3/4 → 重新實現/測試

【重要】
- 這是 Phase 2 的最後一關
- 必須確保所有品質標準達標
- 完成後必須等待人工確認
- 確認通過後 Phase 2 才算完成

立即開始執行 Phase 4！
```

---

## 📋 Prompt 使用指南

### **啟動順序**
```
1. 複製 @INFRA Prompt → Cline/Claude
2. 等待 @INFRA 完成並自動啟動 @ARCH
3. @ARCH 完成後 → Checkpoint 1 → 人工確認
4. 確認通過 → @CODER 自動執行
5. @CODER 完成 → @ANALYST 自動執行
6. @ANALYST 完成後 → Checkpoint 2 → 人工確認
7. 確認通過 → Phase 2 完成 🎉
```

### **關鍵提醒**
- ✅ 所有 Agent 必須使用標準輸出格式
- ✅ 所有 Agent 必須執行自動驗證
- ✅ @ARCH 和 @ANALYST 必須觸發 Checkpoint
- ✅ Checkpoint 必須等待人工確認才能繼續

