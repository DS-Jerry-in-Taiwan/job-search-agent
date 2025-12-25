# ✅ 第7份檔案內容

請將以下**完整內容**貼入 `docs/agent_context/phase2/07_agent_automation_protocol.md`：

```markdown
# Phase 2 - Agent 自動化協議

**階段**: Day 1 步驟1B - Mock職缺生成  
**執行模式**: 混合模式  
**版本**: v1.0

---

## 🤖 執行模式定義

### **混合模式（推薦）**

```
Phase 1 (INFRA) → 自動執行
Phase 2 (ARCH)  → 【Checkpoint 1】人工確認
Phase 3 (CODER) → 自動執行
Phase 4 (ANALYST) → 【Checkpoint 2】人工確認
```

**理由**:
- INFRA：環境設置標準化，自動執行即可
- ARCH：架構設計影響後續開發，需人工確認
- CODER：實現遵循架構，自動執行即可
- ANALYST：最終驗證品質，需人工確認

---

## 🔄 Agent 交接流程

### **標準交接格式**

```
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @INFRA
📍 Phase: Phase 1 - 環境準備
⏰ 完成時間: [時間戳]

✅ 執行結果
  ✅ 建立目錄結構
  ✅ 安裝相依套件
  ✅ 配置環境變數

📁 輸出檔案
  ✅ data/mock/jobs/ (已建立)
  ✅ src/data_providers/ (已建立)
  ✅ tests/ (已建立)
  ✅ requirements.txt (已更新)

🔍 自動驗證
  ✅ 目錄結構正確
  ✅ Python 環境正常
  ✅ 套件安裝成功

👉 下一步
  交接給: @ARCH
  執行模式: 自動啟動
━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## ✅ Checkpoint 機制

### **Checkpoint 1：架構設計確認**

**觸發時機**: @ARCH 完成 Phase 2

**檢查項目**:
```
□ data_schema.json 已建立且格式正確
□ BaseProvider 介面定義完整
□ MockProvider 繼承結構清晰
□ CrawlerProvider 預留擴展點
□ 匹配度計算邏輯合理
□ 檔案命名規範一致
```

**確認選項**:
```
✅ 確認通過         → @CODER 開始 Phase 3
🔍 詳細檢查         → 顯示完整 schema
❌ 問題：[描述]     → 暫停，@ARCH 修正
🔄 重新執行 Phase 2 → @ARCH 重新設計
⏸️ 暫停             → 暫停整體流程
```

---

### **Checkpoint 2：測試驗證確認**

**觸發時機**: @ANALYST 完成 Phase 4

**檢查項目**:
```
□ 50個 Mock 職缺已生成（20高/20中/10低）
□ pytest 測試100%通過（6個測試案例）
□ 數據品質報告完整
□ 匹配度分布符合預期
□ 檔案大小合理（< 100KB）
□ 執行時間 < 5秒
```

**確認選項**:
```
✅ 確認通過         → Phase 2 完成 🎉
🔍 詳細檢查         → 顯示測試報告
❌ 問題：[描述]     → 暫停，@CODER 修正
🔄 重新執行 Phase 3/4 → 重新實現/測試
⏸️ 暫停             → 暫停整體流程
```

---

## 🚨 錯誤處理協議

### **Phase 執行失敗**

```
❌ Phase X 執行失敗
Agent: @[角色名]
錯誤類型: [ImportError/FileNotFoundError/TestFailure/...]
錯誤訊息: [具體錯誤]

建議操作：
1. 🔄 修正後重新執行 Phase X
2. 🔙 回退到 Phase X-1 重新開始
3. 🔍 查看詳細日誌
4. 🛑 中止整個 Phase 2
```

**常見錯誤處理**:

| 錯誤類型 | 處理方式 |
|---------|---------|
| 套件安裝失敗 | @INFRA 重新執行，檢查 requirements.txt |
| Schema 驗證失敗 | @ARCH 修正 data_schema.json |
| 測試失敗 | @CODER 修正程式碼，@ANALYST 重新測試 |
| 數據品質不符 | @CODER 調整生成邏輯 |

---

## 🔍 自動驗證標準

### **Phase 1 (INFRA) 驗證**

```
# 自動檢查清單
✓ tree data/mock/jobs 有輸出
✓ tree src/data_providers 有輸出
✓ ls tests/ 顯示檔案
✓ python --version 正常
✓ pip list | grep pydantic 有結果
```

### **Phase 2 (ARCH) 驗證**

```
# 自動檢查清單
✓ cat data/mock/data_schema.json 有內容
✓ python -c "import json; json.load(open('data/mock/data_schema.json'))" 無錯誤
✓ grep -r "class BaseProvider" src/
✓ grep -r "class MockProvider" src/
✓ wc -l data/mock/data_schema.json > 50
```

### **Phase 3 (CODER) 驗證**

```
# 自動檢查清單
✓ python -c "from src.data_providers.base_provider import BaseProvider" 無錯誤
✓ python -c "from src.data_providers.mock_provider import MockProvider" 無錯誤
✓ ls -lh data/mock/jobs/*.json 有檔案
✓ python -m pytest --collect-only 顯示6個測試
```

### **Phase 4 (ANALYST) 驗證**

```
# 自動檢查清單
✓ python -m pytest -v 100% 通過
✓ ls data/mock/jobs/*.json | wc -l 輸出 1-3
✓ python -c "import json; jobs=json.load(open('data/mock/jobs/mock_jobs.json')); assert len(jobs)==50"
✓ grep -r "品質報告" tests/ 有結果
```

---

## 📊 執行狀態追蹤

### **狀態定義**

```
⬜ 待執行 (Pending)
🔄 執行中 (Running)
⏸️ 暫停 (Paused)
✅ 已完成 (Completed)
❌ 失敗 (Failed)
🔍 檢查中 (Reviewing)
```

### **狀態轉換**

```
⬜ → 🔄 → ✅ (正常流程)
⬜ → 🔄 → ❌ → 🔄 (失敗重試)
✅ → 🔍 → ✅ (Checkpoint 通過)
✅ → 🔍 → 🔄 (Checkpoint 退回)
🔄 → ⏸️ → 🔄 (暫停後繼續)
```

---

## 🎯 完整執行範例

### **正常流程（混合模式）**

```
開始 Phase 2
 ↓
@INFRA Phase 1 🔄
 ↓ (自動驗證通過)
@INFRA Phase 1 ✅
 ↓ (自動啟動)
@ARCH Phase 2 🔄
 ↓ (自動驗證通過)
@ARCH Phase 2 ✅ → 【Checkpoint 1】🔍
 ↓ (人工確認：✅ 確認通過)
@CODER Phase 3 🔄
 ↓ (自動驗證通過)
@CODER Phase 3 ✅
 ↓ (自動啟動)
@ANALYST Phase 4 🔄
 ↓ (自動驗證通過)
@ANALYST Phase 4 ✅ → 【Checkpoint 2】🔍
 ↓ (人工確認：✅ 確認通過)
Phase 2 完成 🎉
```

### **異常流程（測試失敗）**

```
@ANALYST Phase 4 🔄
 ↓ (3個測試失敗)
@ANALYST Phase 4 ❌
 ↓ (錯誤：test_generate_jobs 失敗)
人工決策：🔄 重新執行 Phase 3
 ↓
@CODER Phase 3 🔄 (修正邏輯)
 ↓
@CODER Phase 3 ✅
 ↓
@ANALYST Phase 4 🔄 (重新測試)
 ↓
@ANALYST Phase 4 ✅ → 【Checkpoint 2】🔍
 ↓
Phase 2 完成 🎉
```

---

## 🔐 安全與品質保證

### **必須人工確認的關鍵點**

1. **Checkpoint 1（架構設計）**
   - 確保資料結構符合需求
   - 確保擴展性預留到位
   - 確保介面設計合理

2. **Checkpoint 2（最終驗證）**
   - 確保測試完整覆蓋
   - 確保數據品質達標
   - 確保執行效能合格

### **可自動執行的環節**

1. **環境設置**（INFRA）
   - 標準化操作，低風險
   
2. **程式實現**（CODER）
   - 遵循架構，可自動驗證

---

## 📝 執行日誌格式

### **標準日誌結構**

```
[2024-12-23 15:30:00] Phase 2 開始
[2024-12-23 15:30:05] @INFRA Phase 1 開始
[2024-12-23 15:30:15] @INFRA Phase 1 完成 ✅
[2024-12-23 15:30:16] @ARCH Phase 2 開始
[2024-12-23 15:31:20] @ARCH Phase 2 完成 ✅
[2024-12-23 15:31:21] 【Checkpoint 1】等待人工確認...
[2024-12-23 15:32:00] 【Checkpoint 1】確認通過 ✅
[2024-12-23 15:32:01] @CODER Phase 3 開始
[2024-12-23 15:34:30] @CODER Phase 3 完成 ✅
[2024-12-23 15:34:31] @ANALYST Phase 4 開始
[2024-12-23 15:35:45] @ANALYST Phase 4 完成 ✅
[2024-12-23 15:35:46] 【Checkpoint 2】等待人工確認...
[2024-12-23 15:36:00] 【Checkpoint 2】確認通過 ✅
[2024-12-23 15:36:01] Phase 2 完成 🎉
```

---

## ✅ 協議確認清單

使用本協議前，請確認：

```
□ 已閱讀 Multi-Agent Workflow v3.0
□ 理解混合模式的 2 個 Checkpoint
□ 理解 Agent 交接流程
□ 理解自動驗證標準
□ 理解錯誤處理機制
□ 準備好在 Checkpoint 做決策
```

---

**🎉 Agent 自動化協議定義完成！**

**此協議確保**:
- ✅ 效率：自動執行非關鍵步驟
- ✅ 品質：人工確認關鍵決策
- ✅ 可控：錯誤及時發現處理
- ✅ 透明：執行狀態清晰可追蹤
```

***

## ✅ **請確認貼入**

貼入後請回覆：

```
✅ 07_agent_automation_protocol.md 內容已貼入 (約XXX行)
```

確認後，我們將進入 **Step 6：啟動確認** 🚀