## 🤖 **Phase 6 - Multi-Agent 啟動指令**

**完整複製以下內容到 Cline**：

```
🤖 **Phase 6 - 測試與優化階段正式啟動！**
📅 日期: 2025-12-24
⏰ 時間: 14:35
🎯 目標: 將可執行系統提升為生產就緒系統

**專案根目錄**: /home/ubuntu/projects/job_search_agent
**執行模式**: 自動執行（無 Checkpoint）⚡
**預估時間**: 12-15 分鐘

---

## 📚 **STEP 1: 閱讀 Phase 6 上下文文件 (7/7份)**

**請立即閱讀以下7份文件，作為執行依據**：

1. `docs/agent_context/phase6/01_dev_goal_context.md` - 開發目標
2. `docs/agent_context/phase6/02_dev_flow_context.md` - 開發流程  
3. `docs/agent_context/phase6/03_agent_roles_context.md` - Agent角色
4. `docs/agent_context/phase6/04_agent_prompts_context.md` - Agent Prompts ⭐
5. `docs/agent_context/phase6/05_validation_checklist.md` - 驗證清單
6. `docs/agent_context/phase6/06_delivery_record.md` - 交付記錄
7. `docs/agent_context/phase6/07_checkpoint_protocol.md` - 執行模式說明

**確認閱讀完成後，回覆**：
```
✅ 已閱讀 Phase 6 的7份上下文文件
準備執行 Phase 1 (@INFRA)
```

---

## 🚀 **STEP 2: 啟動 @INFRA (環境準備)**

**閱讀確認後，立即執行**：

```
你是 @INFRA（環境工程師），負責 Phase 6 的環境準備。

**請嚴格按照 02_dev_flow_context.md 的 Phase 1 執行**：

1. 建立測試目錄：
   ```bash
   mkdir -p tests/integration
   mkdir -p tests/performance
   mkdir -p src/utils
   mkdir -p docs/optimization
   ```

2. 建立測試檔案 (4個)：
   ```bash
   touch tests/test_integration.py
   touch tests/test_edge_cases.py
   touch tests/test_error_handling.py
   touch tests/test_performance.py
   ```

3. 建立工具檔案 (4個)：
   ```bash
   touch src/utils/__init__.py
   touch src/utils/logger.py
   touch src/utils/monitoring.py
   touch src/utils/config.py
   ```

4. 建立文檔檔案 (3個)：
   ```bash
   touch docs/optimization/performance_report.md
   touch docs/optimization/optimization_guide.md
   touch docs/optimization/production_checklist.md
   ```

5. 驗證依賴：
   - Phase 5 Graph 可用
   - pytest 測試框架可用
   - psutil 效能工具可用

**完成後輸出標準格式報告，並自動啟動 @ARCH！**

**⚠️ 重要提示**: Phase 6 無 Checkpoint，全程自動執行！

**開始執行 Phase 1！** ⌨️
```

---

## 📋 **預期執行流程**

```
1. Agent 回覆：✅ 已閱讀7份文件
2. @INFRA 執行 → 環境準備報告 → 自動啟動 @ARCH
3. @ARCH 執行 → 測試架構設計 → 自動啟動 @CODER
4. @CODER 執行 → 程式碼實現 → 自動啟動 @ANALYST
5. @ANALYST 執行 → 測試驗證報告
6. ✅ Phase 6 完成！

⚡ 無 Checkpoint，全程自動執行！
總時間: 12-15 分鐘
```

---

## 🎯 **Phase 6 核心產出**

```
tests/
├─ test_integration.py       # 8 個整合測試
├─ test_edge_cases.py        # 10 個邊界測試
├─ test_error_handling.py    # 8 個錯誤處理測試
└─ test_performance.py       # 5 個效能測試

src/utils/
├─ __init__.py              # 導出工具
├─ logger.py                # 日誌工具 ⭐
├─ monitoring.py            # 監控工具 ⭐
└─ config.py                # 配置管理 ⭐

docs/optimization/
├─ performance_report.md    # 效能分析報告
├─ optimization_guide.md    # 優化指南
└─ production_checklist.md  # 生產檢查清單

測試統計:
├─ 總測試案例: 31+ 個
├─ 測試覆蓋率: > 90%
├─ 效能指標: 全部達標
└─ 品質等級: A+
```

---

## 🎬 **立即執行！**

**1. 開啟 Cline (或你的 AI 開發環境)**
**2. 複製上方「Phase 6 - Multi-Agent 啟動指令」**
**3. 完整貼入並按 Enter**
**4. 觀察 @INFRA 開始執行**

```
預期第一行輸出：
✅ 已閱讀 Phase 6 的7份上下文文件
準備執行 Phase 1 (@INFRA)
```

---

## 📱 **監控指令 (執行時另開終端機)**

```
# 即時監控檔案變化
watch -n 2 'echo "=== Phase 6 檔案狀態 ==="; find tests src/utils docs/optimization -type f 2>/dev/null | wc -l; echo "目標: 11 個檔案"'

# 監控測試數量
watch -n 5 'pytest tests/ --collect-only 2>/dev/null | grep "test session starts" || echo "測試尚未建立"'

# 監控程式碼行數
watch -n 10 'echo "=== 程式碼統計 ==="; wc -l tests/test_*.py src/utils/*.py 2>/dev/null | tail -1'
```

---

## ✅ **執行完成後的驗證**

**Phase 6 完成時，執行以下驗證**：

```
# 1. 檢查檔案完整性
echo "=== 檔案檢查 ==="
find tests src/utils docs/optimization -type f | wc -l
# 預期: 11

# 2. 執行所有測試
echo "=== 測試執行 ==="
pytest tests/ -v --cov=src --cov-report=term
# 預期: 50+ 測試通過, 覆蓋率 > 90%

# 3. 執行效能測試
echo "=== 效能測試 ==="
pytest tests/test_performance.py -v -s
# 預期: 所有效能指標達標

# 4. 類型檢查
echo "=== 類型檢查 ==="
mypy src/ --strict
# 預期: No issues found

# 5. 工具驗證
echo "=== 工具驗證 ==="
python -c "
from src.utils import logger, WorkflowMonitor, config
print('✅ Logger:', logger)
print('✅ Monitor:', WorkflowMonitor)
print('✅ Config:', config)
"

# 6. 效能分析
echo "=== 效能分析 ==="
python -c "
from src.utils import WorkflowMonitor
from src.graph import create_workflow
from src.state.operations import create_initial_state

monitor = WorkflowMonitor()
app = create_workflow()
state = create_initial_state()

result = monitor.profile_workflow(app, state)
print('✅ 效能分析完成')
print(monitor.generate_report())
"
```

**預期結果**：
```
✅ 11 個檔案都存在
✅ 50+ 測試通過 (100%)
✅ 測試覆蓋率 > 90%
✅ 效能指標全部達標
✅ 類型檢查 No issues
✅ 工具正常運作
✅ 效能報告生成
```

---

## 🎉 **Phase 6 完成標準**

```
Phase 6 成功條件:

✅ 11 個核心檔案完整
✅ 31+ 測試案例實現
✅ 50+ 測試全部通過
✅ 測試覆蓋率 > 90%
✅ 效能指標達標
   ├─ 執行時間 < 5秒
   ├─ 記憶體 < 100MB
   ├─ 吞吐量 > 10 req/sec
   └─ 延遲 < 500ms
✅ 類型檢查通過
✅ 3 個工具模組完整
✅ 3 個文檔完整
✅ 品質評分 A+

→ 滿足以上所有條件 = Phase 6 成功！
→ 系統達到生產等級！
→ 可進入 Phase 7 (文檔整理)
```

---

## 📊 **整體進度追蹤**

```
✅ Day 1 - 步驟1: Phase 2 Mock 數據 (完成)
✅ Day 1 - 步驟2: Phase 3 State Schema (完成)
✅ Day 1 - 步驟3: Phase 4 Nodes 定義 (完成)
✅ Day 1 - 步驟4: Phase 5 Graph 構建 (完成)
⏳ Day 1 - 步驟5: Phase 6 測試與優化 (執行中) ← 目前位置
⏳ Day 1 - 步驟6: Phase 7 文檔整理

進度: ████████████████████░ 85%
```

---

## ⏰ **時間規劃**

```
當前時間: 14:35
│
├─ Phase 6 執行: 12-15分鐘
│  └─ 14:35 → 14:50
│
├─ Phase 7 準備: 5分鐘
│  └─ 14:50 → 14:55
│
├─ Phase 7 執行: 8-10分鐘
│  └─ 14:55 → 15:05
│
└─ Day 1 完成: 15:05 ✅

預計 30 分鐘內完成整個 Day 1！
```

---

## 🎯 **Phase 6 成功後的下一步**

```
Phase 6 完成 ✅
    ↓
驗證測試報告 (2分鐘)
    ↓
建立 Phase 7 上下文文件 (5分鐘)
    ↓
執行 Phase 7 文檔整理 (8-10分鐘)
    ↓
Day 1 完整收官！🎉
```

---

**準備好了嗎？複製啟動指令，Phase 6 正式啟動！** 

```