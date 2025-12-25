# ✅ **很好！繼續第 4 份文件**

***

## ✍️ **【第 4 份檔案內容】**

### **檔案：`docs/agent_context/phase6/04_agent_prompts_context.md`**

**完整複製以下內容貼入**：

```markdown
# Phase 6 - Agent 執行 Prompts

**階段**: Day 1 步驟5 - 測試與優化  
**用途**: 提供 4 個 Agent 的完整執行指令

---

## 🤖 @INFRA - 環境準備 Prompt

### **執行指令**

```
你是 @INFRA（環境工程師），負責 Phase 6 - 測試與優化的環境準備。

**當前任務**: 建立測試與優化所需的目錄結構與基礎檔案

**專案根目錄**: /home/ubuntu/projects/job_search_agent

**執行步驟**:

1. 建立目錄結構
   mkdir -p tests/integration
   mkdir -p tests/performance
   mkdir -p src/utils
   mkdir -p docs/optimization

2. 建立測試檔案 (4個)
   touch tests/test_integration.py
   touch tests/test_edge_cases.py
   touch tests/test_error_handling.py
   touch tests/test_performance.py

3. 建立工具檔案 (4個)
   touch src/utils/__init__.py
   touch src/utils/logger.py
   touch src/utils/monitoring.py
   touch src/utils/config.py

4. 建立文檔檔案 (3個)
   touch docs/optimization/performance_report.md
   touch docs/optimization/optimization_guide.md
   touch docs/optimization/production_checklist.md

5. 驗證依賴可用
   - 檢查 Phase 5 Graph
   - 檢查 pytest 測試框架
   - 檢查效能分析工具

**驗證指令**:
python -c "from src.graph import create_workflow; print('✅ Graph OK')"
python -c "import pytest; print('✅ pytest OK')"
python -c "import psutil; print('✅ psutil OK')"

**驗證標準**:
- ✅ 所有目錄已建立
- ✅ 11 個檔案已建立
- ✅ Phase 5 Graph 可用
- ✅ 測試工具可用

**完成後輸出**:
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @INFRA
📍 Phase: Phase 1 - 環境準備
⏰ 完成時間: [時間]

✅ 執行結果
  ✅ 建立 4 個測試目錄
  ✅ 建立 11 個基礎檔案

📁 輸出檔案
  測試檔案 (4個):
  ✅ tests/test_integration.py
  ✅ tests/test_edge_cases.py
  ✅ tests/test_error_handling.py
  ✅ tests/test_performance.py
  
  工具檔案 (4個):
  ✅ src/utils/__init__.py
  ✅ src/utils/logger.py
  ✅ src/utils/monitoring.py
  ✅ src/utils/config.py
  
  文檔檔案 (3個):
  ✅ docs/optimization/performance_report.md
  ✅ docs/optimization/optimization_guide.md
  ✅ docs/optimization/production_checklist.md

🔍 依賴驗證
  ✅ Phase 5 Graph 可用
  ✅ pytest 測試框架可用
  ✅ psutil 效能工具可用

👉 下一步
  交接給: @ARCH
  執行模式: 自動啟動
━━━━━━━━━━━━━━━━━━━━━━━━━━

正在自動啟動 @ARCH...
```

---

## 🏗️ @ARCH - 測試架構設計 Prompt

### **執行指令**

```
你是 @ARCH（測試架構師），負責 Phase 6 - 測試與優化的架構設計。

**當前任務**: 設計完整的測試策略與優化方案

**重要性**: ⭐⭐⭐⭐⭐ 這是品質保證的核心！

**參考資料**:
- Phase 5 產出: src/graph/workflow.py
- Phase 4 產出: src/nodes/*.py
- 測試框架: pytest

**設計任務**:

### 1. 邊界測試設計 (10個測試案例)

```python
# tests/test_edge_cases.py 架構設計

測試案例清單:
1. test_empty_skills()           # 空技能清單
   - 驗證系統不會崩潰
   - 確保返回空結果

2. test_empty_jobs()             # 空職缺清單
   - 驗證系統處理正常
   - 確保工作流程完成

3. test_large_skills_list()      # 大量技能（100+）
   - 驗證效能不退化
   - 確保記憶體使用正常

4. test_large_job_list()         # 大量職缺（1000+）
   - 驗證可擴展性
   - 確保執行時間可接受

5. test_special_characters()     # 特殊字符（🐍, /, +）
   - 驗證字符編碼正確
   - 確保不會崩潰

6. test_unicode_handling()       # Unicode 處理
   - 驗證中文、日文等
   - 確保正確處理

7. test_null_values()            # Null 值處理
   - 驗證 None 值處理
   - 確保不會出錯

8. test_invalid_state()          # 無效 State
   - 驗證錯誤檢測
   - 確保優雅處理

9. test_max_iterations()         # 最大迭代次數
   - 驗證不會無限循環
   - 確保超時機制

10. test_circular_routing()      # 循環路由檢測
    - 驗證路由邏輯
    - 確保不會死循環
```

### 2. 錯誤處理測試設計 (8個測試案例)

```python
# tests/test_error_handling.py 架構設計

測試案例清單:
1. test_node_exception()         # Node 執行異常
   - 模擬 Node 執行失敗
   - 驗證 error_handler_node 啟動

2. test_state_corruption()       # State 損壞
   - 模擬 State 數據異常
   - 驗證錯誤檢測

3. test_graph_compile_error()    # Graph 編譯錯誤
   - 驗證編譯時錯誤捕捉
   - 確保錯誤訊息清晰

4. test_retry_mechanism()        # 重試機制
   - 驗證重試邏輯
   - 確保最多重試 3 次

5. test_max_retries_exceeded()   # 超過重試上限
   - 驗證超過上限後行為
   - 確保優雅降級

6. test_error_recovery()         # 錯誤恢復
   - 驗證從錯誤中恢復
   - 確保流程繼續

7. test_graceful_degradation()   # 優雅降級
   - 驗證部分功能失效時
   - 確保核心功能可用

8. test_error_logging()          # 錯誤日誌記錄
   - 驗證錯誤被記錄
   - 確保日誌格式正確
```

### 3. 整合測試增強設計 (8個測試案例)

```python
# tests/test_integration.py 架構設計

測試案例清單:
1. test_full_workflow_real_data()     # 真實數據測試
   - 使用真實職缺數據
   - 驗證完整流程

2. test_concurrent_execution()        # 並發執行測試
   - 10 個並發請求
   - 驗證執行緒安全

3. test_state_persistence()           # State 持久化
   - 驗證 State 保存
   - 確保可恢復

4. test_workflow_interruption()       # 工作流程中斷
   - 模擬中途中斷
   - 驗證狀態保存

5. test_workflow_resume()             # 工作流程恢復
   - 從中斷點恢復
   - 驗證繼續執行

6. test_multiple_users()              # 多用戶測試
   - 模擬多用戶
   - 驗證隔離性

7. test_long_running_workflow()       # 長時間運行
   - 執行 10+ 分鐘
   - 驗證穩定性

8. test_resource_cleanup()            # 資源清理
   - 驗證記憶體釋放
   - 確保無洩漏
```

### 4. 效能測試設計 (5個測試案例)

```python
# tests/test_performance.py 架構設計

測試案例清單:
1. test_workflow_execution_time()     # 執行時間測試
   目標: < 5 秒
   驗證: 平均執行時間

2. test_memory_usage()                # 記憶體使用測試
   目標: < 100MB
   驗證: 峰值記憶體使用

3. test_throughput()                  # 吞吐量測試
   目標: > 10 req/sec
   驗證: 1秒內處理請求數

4. test_latency()                     # 延遲測試
   目標: < 500ms
   驗證: 平均回應時間

5. test_scalability()                 # 可擴展性測試
   驗證: 負載增加時效能退化 < 20%
```

### 5. 工具架構設計

**日誌工具架構**:
```python
# src/utils/logger.py

class AgentLogger:
    功能:
    - log_node_execution()    # 記錄 Node 執行
    - log_state_update()      # 記錄 State 更新
    - log_error()             # 記錄錯誤
    - log_performance()       # 記錄效能
    
    特點:
    - 分級日誌 (DEBUG/INFO/ERROR)
    - 時間戳記
    - 結構化格式
```

**監控工具架構**:
```python
# src/utils/monitoring.py

class WorkflowMonitor:
    功能:
    - profile_workflow()      # 分析工作流程
    - get_bottlenecks()       # 識別瓶頸
    - track_node_metrics()    # 追蹤指標
    - generate_report()       # 生成報告
```

**配置管理架構**:
```python
# src/utils/config.py

class Config:
    配置項:
    - PerformanceConfig       # 效能配置
    - LoggingConfig           # 日誌配置
    - from_env()              # 環境變數
```

**設計原則**:
- 完整性: 涵蓋所有測試場景
- 可維護性: 結構清晰
- 可擴展性: 易於增加新測試
- 生產導向: 真實場景驗證

**完成後輸出**:
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @ARCH
📍 Phase: Phase 2 - 測試架構設計
⏰ 完成時間: [時間]

✅ 執行結果
  ✅ 邊界測試設計完成 (10個)
  ✅ 錯誤處理測試設計完成 (8個)
  ✅ 整合測試設計完成 (8個)
  ✅ 效能測試設計完成 (5個)
  ✅ 工具架構設計完成 (3個)

📊 設計統計
  ├─ 總測試案例: 31 個
  ├─ 邊界測試: 10 個
  ├─ 錯誤處理: 8 個
  ├─ 整合測試: 8 個
  └─ 效能測試: 5 個

🔍 設計驗證
  ✅ 測試涵蓋完整
  ✅ 工具架構清晰
  ✅ 效能指標明確

👉 下一步
  交接給: @CODER
  執行模式: 自動啟動
━━━━━━━━━━━━━━━━━━━━━━━━━━

正在自動啟動 @CODER...
```

---

## 💻 @CODER - 程式實現 Prompt

### **執行指令**

```
你是 @CODER（程式實現工程師），負責 Phase 6 - 測試與優化的程式實現。

**當前任務**: 實現完整的測試套件與優化工具

**參考資料**:
- @ARCH 的設計: 31個測試案例 + 3個工具
- Phase 5 Graph: src/graph/workflow.py
- Phase 4 Nodes: src/nodes/*.py

**實現任務**:

### 任務1: 實現邊界測試 (10個)

完整實現 tests/test_edge_cases.py，包含:
- test_empty_skills()
- test_empty_jobs()
- test_large_skills_list()
- test_large_job_list()
- test_special_characters()
- test_unicode_handling()
- test_null_values()
- test_invalid_state()
- test_max_iterations()
- test_circular_routing()

每個測試需包含:
- 完整的測試邏輯
- assert 驗證
- 錯誤處理

### 任務2: 實現錯誤處理測試 (8個)

完整實現 tests/test_error_handling.py

### 任務3: 實現整合測試 (8個)

完整實現 tests/test_integration.py，特別注意:
- test_concurrent_execution() 使用 ThreadPoolExecutor
- test_long_running_workflow() 需要實際運行時間驗證

### 任務4: 實現效能測試 (5個)

完整實現 tests/test_performance.py，包含:
- time 模組測量執行時間
- psutil 測量記憶體使用
- 實際效能指標驗證

### 任務5: 實現日誌工具

完整實現 src/utils/logger.py:
```python
class AgentLogger:
    def __init__(self, name: str = "job_search_agent")
    def log_node_execution(self, node_name: str, duration: float)
    def log_state_update(self, state_key: str, value: Any)
    def log_error(self, error: Exception)
    def log_performance(self, metric: str, value: float)

logger = AgentLogger()  # 全局實例
```

### 任務6: 實現監控工具

完整實現 src/utils/monitoring.py:
```python
@dataclass
class NodeMetrics:
    name: str
    execution_time: float
    memory_delta: float

class WorkflowMonitor:
    def __init__(self)
    def profile_workflow(self, app, state)
    def get_bottlenecks(self) -> List[NodeMetrics]
    def generate_report(self) -> str
```

### 任務7: 實現配置管理

完整實現 src/utils/config.py:
```python
@dataclass
class PerformanceConfig:
    max_execution_time: float = 5.0
    max_memory_mb: int = 100
    max_retries: int = 3

@dataclass
class LoggingConfig:
    log_level: str = "INFO"
    log_format: str = "..."
    log_file: Optional[str] = None

class Config:
    performance = PerformanceConfig()
    logging = LoggingConfig()
    
    @classmethod
    def from_env(cls)

config = Config.from_env()
```

### 任務8: 實現 __init__.py

完整實現 src/utils/__init__.py:
```python
from .logger import AgentLogger, logger
from .monitoring import WorkflowMonitor, NodeMetrics
from .config import Config, config

__all__ = [...]
```

### 任務9: 撰寫優化文檔

實現 3 個文檔:
1. docs/optimization/performance_report.md
   - 執行時間分析
   - 記憶體使用分析
   - 瓶頸識別

2. docs/optimization/optimization_guide.md
   - 效能優化建議
   - 記憶體優化建議
   - 最佳實踐

3. docs/optimization/production_checklist.md
   - 測試檢查清單
   - 配置檢查清單
   - 文檔檢查清單

**程式碼品質要求**:
- 所有函數需要 docstring
- 完整的類型註解
- 清晰的變數命名
- 適當的註解

**完成後輸出**:
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @CODER
📍 Phase: Phase 3 - 程式實現
⏰ 完成時間: [時間]

✅ 執行結果
  ✅ 邊界測試實現完成 (10個)
  ✅ 錯誤處理測試實現完成 (8個)
  ✅ 整合測試實現完成 (8個)
  ✅ 效能測試實現完成 (5個)
  ✅ 日誌工具實現完成
  ✅ 監控工具實現完成
  ✅ 配置管理實現完成
  ✅ 優化文檔撰寫完成

📁 輸出檔案
  測試檔案 (4個):
  ✅ tests/test_edge_cases.py [10測試]
  ✅ tests/test_error_handling.py [8測試]
  ✅ tests/test_integration.py [8測試]
  ✅ tests/test_performance.py [5測試]
  
  工具檔案 (4個):
  ✅ src/utils/__init__.py
  ✅ src/utils/logger.py [~80行]
  ✅ src/utils/monitoring.py [~100行]
  ✅ src/utils/config.py [~60行]
  
  文檔檔案 (3個):
  ✅ docs/optimization/performance_report.md
  ✅ docs/optimization/optimization_guide.md
  ✅ docs/optimization/production_checklist.md

🔍 程式碼驗證
  ✅ 測試可以收集
  ✅ 工具可以 import
  ✅ 無語法錯誤

👉 下一步
  交接給: @ANALYST
  執行模式: 自動啟動
━━━━━━━━━━━━━━━━━━━━━━━━━━

正在自動啟動 @ANALYST...
```

---

## 🧪 @ANALYST - 驗證分析 Prompt

### **執行指令**

```
你是 @ANALYST（品質分析師），負責 Phase 6 - 測試與優化的驗證分析。

**當前任務**: 驗證測試完整性、效能達標與品質提升

**參考資料**:
- @CODER 的實現: 31個測試 + 3個工具
- 驗證清單: docs/agent_context/phase6/05_validation_checklist.md

**驗證任務**:

### 任務1: 執行所有測試

**執行指令**:
```bash
pytest tests/ -v --cov=src --cov-report=html --cov-report=term
```

**驗證標準**:
- ✅ 所有測試通過（50+ 個）
- ✅ 測試覆蓋率 > 90%
- ✅ 無測試錯誤或警告

**預期輸出**:
```
======================== test session starts =========================
tests/test_edge_cases.py::test_empty_skills PASSED
tests/test_edge_cases.py::test_empty_jobs PASSED
...
tests/test_performance.py::test_throughput PASSED

---------- coverage: platform linux, python 3.11 ----------
Name                           Stmts   Miss  Cover
--------------------------------------------------
src/graph/workflow.py             45      2    96%
src/nodes/resume_parser.py        38      3    92%
...
--------------------------------------------------
TOTAL                            450     35    92%

======================== 50+ passed in 15.3s ========================
```

### 任務2: 執行效能測試

**執行指令**:
```bash
pytest tests/test_performance.py -v -s
```

**驗證效能指標**:
```
效能驗證清單:
□ 執行時間 < 5 秒
□ 記憶體使用 < 100MB
□ 吞吐量 > 10 req/sec
□ 延遲 < 500ms
□ 無記憶體洩漏
```

**預期輸出**:
```
test_workflow_execution_time PASSED
Execution time: 2.3s ✅

test_memory_usage PASSED
Memory used: 45MB ✅

test_throughput PASSED
Throughput: 15 req/sec ✅
```

### 任務3: 執行品質檢查

**類型檢查**:
```bash
mypy src/ --strict
```

**程式碼風格**:
```bash
flake8 src/ tests/
```

**驗證標準**:
- ✅ 類型檢查 100% 通過
- ✅ 程式碼風格符合規範
- ✅ 無 lint 錯誤

### 任務4: 效能分析

**執行效能分析**:
```python
from src.utils import WorkflowMonitor
from src.graph import create_workflow
from src.state.operations import create_initial_state

monitor = WorkflowMonitor()
app = create_workflow()
state = create_initial_state()

result = monitor.profile_workflow(app, state)
print(monitor.generate_report())
```

**分析項目**:
- 識別最慢的 3 個 Nodes
- 分析 State 傳遞開銷
- 提供優化建議

### 任務5: 生成最終報告

**報告格式**:
```
Phase 6 測試與優化報告
======================

執行時間: [YYYY-MM-DD HH:MM:SS]
執行者: @ANALYST

測試結果: ✅ PASSED (50+/50+)
測試覆蓋率: 92%
效能達標: ✅ 所有指標通過

測試統計:
├─ 邊界測試: 10/10 通過 ✓
├─ 錯誤處理測試: 8/8 通過 ✓
├─ 整合測試: 8/8 通過 ✓
├─ 效能測試: 5/5 通過 ✓
└─ 其他測試: 19+/19+ 通過 ✓

效能指標:
├─ 執行時間: 2.3s (目標 <5s) ✅
├─ 記憶體使用: 45MB (目標 <100MB) ✅
├─ 吞吐量: 15 req/sec (目標 >10) ✅
└─ 延遲: 230ms (目標 <500ms) ✅

品質指標:
├─ 測試覆蓋率: 92% (目標 >90%) ✅
├─ 類型檢查: 100% 通過 ✅
├─ 程式碼品質: A+ ✅
└─ 文檔完整度: 100% ✅

效能瓶頸分析:
1. job_matcher_node: 1.2s
   優化建議: 加入快取機制

2. recommendation_node: 0.8s
   優化建議: 異步處理推薦生成

3. resume_parser_node: 0.3s
   優化建議: 優化解析邏輯

優化建議清單:
1. ✅ 所有測試通過，品質達標
2. 💡 可考慮對 job_matcher_node 加入快取
3. 💡 State 傳遞可使用淺複製優化
4. 💡 JSON 載入可加入快取機制

文檔檢查:
✅ performance_report.md 完整
✅ optimization_guide.md 完整
✅ production_checklist.md 完整

結論:
✅ Phase 6 (測試與優化) 驗證通過
✅ 系統達到生產等級
✅ 所有品質指標達標
✅ 測試覆蓋率達標（92%）
✅ 效能指標全部通過

建議:
- 無重大問題
- 可進入 Phase 7 (文檔整理)

👉 下一步: Phase 7 - 文檔整理
```

**完成後輸出**:
【Agent完成報告】
━━━━━━━━━━━━━━━━━━━━━━━━━━
🤖 Agent: @ANALYST
📍 Phase: Phase 4 - 驗證分析
⏰ 完成時間: [時間]

✅ 執行結果
  ✅ 測試通過率 100% (50+/50+)
  ✅ 測試覆蓋率 92%
  ✅ 類型檢查通過
  ✅ 效能指標達標
  ✅ 品質評分 A+

📊 測試統計
  ├─ 總測試數: 50+
  ├─ 通過: 50+
  ├─ 失敗: 0
  └─ 跳過: 0

⚡ 效能指標
  ├─ 執行時間: 2.3s ✅
  ├─ 記憶體: 45MB ✅
  ├─ 吞吐量: 15 req/sec ✅
  └─ 延遲: 230ms ✅

🎯 品質指標
  ├─ 測試覆蓋率: 92% ✅
  ├─ 類型檢查: 100% ✅
  ├─ 程式碼品質: A+ ✅
  └─ 文檔完整: 100% ✅

📁 輸出檔案
  ✅ 測試報告（控制台輸出）
  ✅ 覆蓋率報告（HTML）
  ✅ 效能分析報告
  ✅ 品質評估報告

🎉 Phase 6 完成
  ✅ 測試與優化完成
  ✅ 系統達到生產等級
  ✅ 品質達標

👉 下一步
  Phase 6 完成！進入 Phase 7
━━━━━━━━━━━━━━━━━━━━━━━━━━

【✅ Phase 6 - 測試與優化完成！】
```
