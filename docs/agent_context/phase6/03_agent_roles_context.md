# ✅ **很好！繼續第 3 份文件（繁體中文版）**

***

## ✍️ **【第 3 份檔案內容】**

### **檔案：`docs/agent_context/phase6/03_agent_roles_context.md`**

**完整複製以下內容貼入**：

```markdown
# Phase 6 - Agent 角色與職責

**階段**: Day 1 步驟5 - 測試與優化  
**團隊模式**: 4 Agent 協作（自動執行）

---

## 🎪 Agent 團隊總覽

在測試與優化階段，4 個 Agent 的角色如下：

| Agent | 角色 | 核心職責 | 產出物 |
|-------|------|---------|--------|
| **@INFRA** | 環境工程師 | 建立測試環境 | 目錄結構 + 11檔案 |
| **@ARCH** | 測試架構師 | 設計測試策略 | 30+測試案例設計 |
| **@CODER** | 程式實現工程師 | 實現測試與工具 | 完整測試套件 |
| **@ANALYST** | 品質分析師 | 驗證與報告 | 效能分析報告 |

⚠️ **Phase 6 特點**: 無 Checkpoint，全程自動執行

---

## 🔧 @INFRA - 環境工程師

### **角色定位**
負責建立測試與優化所需的環境，確保測試工具、目錄結構完整。

### **核心職責**

1. **建立測試目錄結構**
   ```
   tests/integration/       # 整合測試目錄
   tests/performance/       # 效能測試目錄
   src/utils/              # 工具模組目錄
   docs/optimization/      # 優化文檔目錄
   ```

2. **建立基礎檔案 (11個)**
   ```
   測試檔案 (4個):
   ├─ tests/test_integration.py
   ├─ tests/test_edge_cases.py
   ├─ tests/test_error_handling.py
   └─ tests/test_performance.py
   
   工具檔案 (4個):
   ├─ src/utils/__init__.py
   ├─ src/utils/logger.py
   ├─ src/utils/monitoring.py
   └─ src/utils/config.py
   
   文檔檔案 (3個):
   ├─ docs/optimization/performance_report.md
   ├─ docs/optimization/optimization_guide.md
   └─ docs/optimization/production_checklist.md
   ```

3. **驗證測試工具可用**
   - pytest 可用
   - coverage 工具可用
   - 效能分析工具可用（psutil, memory_profiler）
   - Phase 5 Graph 可用

### **輸入**
- Phase 5 產出：完整可執行的 Graph
- 測試框架：pytest, coverage
- 效能工具：psutil, memory_profiler

### **輸出**
- ✅ 完整的目錄結構
- ✅ 11 個基礎檔案已建立
- ✅ 測試工具驗證通過

### **驗證標準**
```
# 檢查目錄
ls -la tests/integration tests/performance src/utils docs/optimization

# 檢查依賴
python -c "import pytest; print('✅ pytest OK')"
python -c "import psutil; print('✅ psutil OK')"
python -c "from src.graph import create_workflow; print('✅ Graph OK')"
```

### **執行時間**: ~2 分鐘

---

## 🏗️ @ARCH - 測試架構師

### **角色定位**
設計完整的測試策略與優化方案，這是品質保證的核心。

### **核心職責**

#### **1. 邊界測試架構設計**

**設計目標**: 涵蓋所有邊界情況

```
# tests/test_edge_cases.py 架構

測試案例清單 (10個):
1. test_empty_skills()           # 空技能清單
2. test_empty_jobs()             # 空職缺清單
3. test_large_skills_list()      # 大量技能（100+）
4. test_large_job_list()         # 大量職缺（1000+）
5. test_special_characters()     # 特殊字符處理
6. test_unicode_handling()       # Unicode 處理
7. test_null_values()            # Null 值處理
8. test_invalid_state()          # 無效 State
9. test_max_iterations()         # 最大迭代次數
10. test_circular_routing()      # 循環路由檢測
```

**設計要點**:
- ✅ 涵蓋空值、大量數據、特殊字符
- ✅ 驗證系統不會崩潰
- ✅ 確保錯誤訊息清晰

---

#### **2. 錯誤處理測試架構設計**

**設計目標**: 驗證系統的錯誤處理機制

```
# tests/test_error_handling.py 架構

測試案例清單 (8個):
1. test_node_exception()         # Node 執行異常
2. test_state_corruption()       # State 損壞
3. test_graph_compile_error()    # Graph 編譯錯誤
4. test_retry_mechanism()        # 重試機制
5. test_max_retries_exceeded()   # 超過重試上限
6. test_error_recovery()         # 錯誤恢復
7. test_graceful_degradation()   # 優雅降級
8. test_error_logging()          # 錯誤日誌記錄
```

**設計要點**:
- ✅ 驗證 error_handler_node 運作
- ✅ 確保系統不會因錯誤而崩潰
- ✅ 錯誤訊息清晰且可操作

---

#### **3. 整合測試增強架構設計**

**設計目標**: 端到端測試增強

```
# tests/test_integration.py 架構

測試案例清單 (8個):
1. test_full_workflow_real_data()     # 真實數據測試
2. test_concurrent_execution()        # 並發執行測試
3. test_state_persistence()           # State 持久化
4. test_workflow_interruption()       # 工作流程中斷
5. test_workflow_resume()             # 工作流程恢復
6. test_multiple_users()              # 多用戶測試
7. test_long_running_workflow()       # 長時間運行
8. test_resource_cleanup()            # 資源清理
```

**設計要點**:
- ✅ 使用真實數據測試
- ✅ 並發安全驗證
- ✅ 資源管理驗證

---

#### **4. 效能測試架構設計**

**設計目標**: 驗證效能指標

```
# tests/test_performance.py 架構

測試案例清單 (5個):
1. test_workflow_execution_time()     # 執行時間 < 5秒
2. test_memory_usage()                # 記憶體使用 < 100MB
3. test_throughput()                  # 吞吐量 > 10 req/sec
4. test_latency()                     # 延遲 < 500ms
5. test_scalability()                 # 可擴展性測試
```

**效能指標**:
```
目標值:
├─ 執行時間: < 5 秒
├─ 記憶體使用: < 100MB
├─ 吞吐量: > 10 req/sec
├─ 延遲: < 500ms
└─ 無記憶體洩漏
```

---

#### **5. 工具架構設計**

**日誌工具架構**:
```
# src/utils/logger.py

class AgentLogger:
    """AI Agent 日誌系統"""
    
    功能:
    ├─ log_node_execution()    # 記錄 Node 執行
    ├─ log_state_update()      # 記錄 State 更新
    ├─ log_error()             # 記錄錯誤
    └─ log_performance()       # 記錄效能指標
    
    特點:
    ├─ 分級日誌 (DEBUG/INFO/ERROR)
    ├─ 結構化日誌格式
    └─ 支援檔案與控制台輸出
```

**監控工具架構**:
```
# src/utils/monitoring.py

class WorkflowMonitor:
    """工作流程監控"""
    
    功能:
    ├─ profile_workflow()      # 分析工作流程
    ├─ get_bottlenecks()       # 識別瓶頸
    ├─ track_node_metrics()    # 追蹤 Node 指標
    └─ generate_report()       # 生成報告
    
    指標:
    ├─ 每個 Node 的執行時間
    ├─ State 傳遞開銷
    ├─ 記憶體使用情況
    └─ 識別效能瓶頸
```

**配置管理架構**:
```
# src/utils/config.py

class Config:
    """配置管理"""
    
    配置項:
    ├─ PerformanceConfig      # 效能配置
    │  ├─ max_execution_time
    │  ├─ max_memory_mb
    │  └─ max_retries
    │
    ├─ LoggingConfig          # 日誌配置
    │  ├─ log_level
    │  ├─ log_format
    │  └─ log_file
    │
    └─ from_env()             # 從環境變數載入
```

---

### **設計原則**

1. **完整性**
   - 測試涵蓋所有邊界情況
   - 錯誤處理全面
   - 效能指標明確

2. **可維護性**
   - 測試案例清晰
   - 工具模組化設計
   - 配置可調整

3. **生產導向**
   - 真實場景測試
   - 效能達標驗證
   - 監控機制完善

### **輸入**
- Phase 5 的完整 Graph
- 測試需求分析

### **輸出**
- ✅ 30+ 測試案例設計
- ✅ 3 個工具模組架構
- ✅ 優化策略文檔

### **執行時間**: ~3 分鐘

---

## 💻 @CODER - 程式實現工程師

### **角色定位**
將 @ARCH 的測試架構與工具設計轉化為可執行的程式碼。

### **核心職責**

#### **1. 實現邊界測試 (10個測試)**

```
# tests/test_edge_cases.py
"""邊界測試套件 - 完整實現"""

import pytest
from src.graph import create_workflow
from src.state.operations import create_initial_state

def test_empty_skills():
    """測試空技能清單"""
    app = create_workflow()
    state = create_initial_state()
    state["user_profile"]["skills"] = []
    
    result = app.invoke(state)
    
    assert result["job_state"]["matched_jobs"] == []
    assert result["is_complete"] == True

def test_large_job_list():
    """測試大量職缺處理（1000個）"""
    app = create_workflow()
    state = create_initial_state()
    
    # 模擬 1000 個職缺
    large_jobs = [
        {"job_id": f"job_{i}", "title": f"Job {i}"}
        for i in range(1000)
    ]
    state["job_state"]["jobs"] = large_jobs
    
    result = app.invoke(state)
    assert result["is_complete"] == True

def test_special_characters():
    """測試特殊字符處理"""
    app = create_workflow()
    state = create_initial_state()
    state["user_profile"]["skills"] = ["Python 🐍", "AI/ML", "C++"]
    
    result = app.invoke(state)
    assert result["is_complete"] == True

# ... 其他 7 個邊界測試
```

#### **2. 實現錯誤處理測試 (8個測試)**

```
# tests/test_error_handling.py
"""錯誤處理測試套件 - 完整實現"""

import pytest
from src.graph import create_workflow
from src.state.operations import create_initial_state

def test_retry_mechanism():
    """測試重試機制"""
    app = create_workflow()
    state = create_initial_state()
    
    # 模擬需要重試的情況
    state["system"]["error_message"] = "Test retry"
    
    result = app.invoke(state)
    
    # 驗證重試機制
    assert result["system"]["retry_count"] <= 3

# ... 其他 7 個錯誤處理測試
```

#### **3. 實現整合測試 (8個測試)**

```
# tests/test_integration.py
"""整合測試增強 - 完整實現"""

import pytest
from src.graph import create_workflow
from src.state.operations import create_initial_state
from concurrent.futures import ThreadPoolExecutor

def test_concurrent_execution():
    """測試並發執行"""
    app = create_workflow()
    
    def run_workflow():
        state = create_initial_state()
        return app.invoke(state)
    
    # 並發執行 10 次
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(run_workflow) for _ in range(10)]
        results = [f.result() for f in futures]
    
    # 驗證所有執行成功
    assert all(r["is_complete"] for r in results)

# ... 其他 7 個整合測試
```

#### **4. 實現效能測試 (5個測試)**

```
# tests/test_performance.py
"""效能測試套件 - 完整實現"""

import pytest
from src.graph import create_workflow
from src.state.operations import create_initial_state
import time
import psutil
import os

def test_workflow_execution_time():
    """測試執行時間 < 5秒"""
    app = create_workflow()
    state = create_initial_state()
    
    start_time = time.time()
    result = app.invoke(state)
    execution_time = time.time() - start_time
    
    assert execution_time < 5.0
    print(f"Execution time: {execution_time:.2f}s")

def test_memory_usage():
    """測試記憶體使用 < 100MB"""
    process = psutil.Process(os.getpid())
    
    initial_memory = process.memory_info().rss / 1024 / 1024  # MB
    
    app = create_workflow()
    state = create_initial_state()
    result = app.invoke(state)
    
    final_memory = process.memory_info().rss / 1024 / 1024
    memory_used = final_memory - initial_memory
    
    assert memory_used < 100
    print(f"Memory used: {memory_used:.2f}MB")

# ... 其他 3 個效能測試
```

#### **5. 實現日誌工具**

```
# src/utils/logger.py
"""AI Agent 日誌工具"""

import logging
from typing import Any
from datetime import datetime

class AgentLogger:
    """AI Agent 日誌系統"""
    
    def __init__(self, name: str = "job_search_agent"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def log_node_execution(self, node_name: str, duration: float):
        """記錄 Node 執行時間"""
        self.logger.info(f"Node '{node_name}' executed in {duration:.2f}s")
    
    def log_state_update(self, state_key: str, value: Any):
        """記錄 State 更新"""
        self.logger.debug(f"State updated: {state_key} = {value}")
    
    def log_error(self, error: Exception):
        """記錄錯誤"""
        self.logger.error(f"Error occurred: {error}", exc_info=True)
    
    def log_performance(self, metric: str, value: float):
        """記錄效能指標"""
        self.logger.info(f"Performance: {metric} = {value:.2f}")

# 全局實例
logger = AgentLogger()
```

#### **6. 實現監控工具**

```
# src/utils/monitoring.py
"""工作流程監控工具"""

import time
from typing import Dict, List
from dataclasses import dataclass

@dataclass
class NodeMetrics:
    """Node 效能指標"""
    name: str
    execution_time: float
    memory_delta: float

class WorkflowMonitor:
    """工作流程監控"""
    
    def __init__(self):
        self.metrics: List[NodeMetrics] = []
        self.start_time = None
    
    def profile_workflow(self, app, state):
        """分析工作流程效能"""
        self.start_time = time.time()
        result = app.invoke(state)
        total_time = time.time() - self.start_time
        
        return {
            "total_time": total_time,
            "node_metrics": self.metrics,
            "result": result
        }
    
    def get_bottlenecks(self) -> List[NodeMetrics]:
        """獲取效能瓶頸（前3名）"""
        return sorted(
            self.metrics,
            key=lambda x: x.execution_time,
            reverse=True
        )[:3]
    
    def generate_report(self) -> str:
        """生成效能報告"""
        report = "效能分析報告\n"
        report += "=" * 50 + "\n\n"
        
        report += "Node 執行時間:\n"
        for metric in self.metrics:
            report += f"  {metric.name}: {metric.execution_time:.2f}s\n"
        
        report += "\n效能瓶頸:\n"
        for node in self.get_bottlenecks():
            report += f"  ⚠️ {node.name}: {node.execution_time:.2f}s\n"
        
        return report
```

#### **7. 實現配置管理**

```
# src/utils/config.py
"""配置管理"""

from dataclasses import dataclass
from typing import Optional
import os

@dataclass
class PerformanceConfig:
    """效能配置"""
    max_execution_time: float = 5.0  # 秒
    max_memory_mb: int = 100
    max_retries: int = 3
    
@dataclass
class LoggingConfig:
    """日誌配置"""
    log_level: str = "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    log_file: Optional[str] = None

class Config:
    """全局配置"""
    
    performance = PerformanceConfig()
    logging = LoggingConfig()
    
    @classmethod
    def from_env(cls):
        """從環境變數載入配置"""
        cls.performance.max_execution_time = float(
            os.getenv("MAX_EXECUTION_TIME", "5.0")
        )
        cls.performance.max_memory_mb = int(
            os.getenv("MAX_MEMORY_MB", "100")
        )
        cls.logging.log_level = os.getenv("LOG_LEVEL", "INFO")
        return cls

# 全局配置實例
config = Config.from_env()
```

#### **8. 實現 __init__.py**

```
# src/utils/__init__.py
"""工具模組"""

from .logger import AgentLogger, logger
from .monitoring import WorkflowMonitor, NodeMetrics
from .config import Config, config

__all__ = [
    "AgentLogger",
    "logger",
    "WorkflowMonitor",
    "NodeMetrics",
    "Config",
    "config",
]
```

#### **9. 撰寫優化文檔**

```
# docs/optimization/performance_report.md
# docs/optimization/optimization_guide.md
# docs/optimization/production_checklist.md

（完整內容見 Phase 3 文檔）
```

### **輸入**
- @ARCH 的測試設計與工具架構

### **輸出**
- ✅ 4 個測試檔案（31+ 測試案例）
- ✅ 4 個工具檔案
- ✅ 3 個優化文檔
- ✅ 所有測試可執行

### **驗證標準**
```
# 測試可以收集
pytest tests/ --collect-only

# 工具可以 import
python -c "from src.utils import logger, WorkflowMonitor; print('OK')"
```

### **執行時間**: ~5 分鐘

---

## 🧪 @ANALYST - 品質分析師

### **角色定位**
驗證測試完整性、效能達標與品質提升，生成最終報告。

### **核心職責**

#### **1. 執行所有測試**

```
# 執行完整測試套件
pytest tests/ -v --cov=src --cov-report=html

# 預期結果: 50+ 測試通過
```

**驗證標準**:
- ✅ 所有測試通過（100%）
- ✅ 測試覆蓋率 > 90%
- ✅ 無測試錯誤

#### **2. 效能驗證**

```
# 執行效能測試
pytest tests/test_performance.py -v -s

# 驗證指標
```

**效能指標驗證**:
```
✅ 執行時間: < 5 秒
✅ 記憶體使用: < 100MB
✅ 吞吐量: > 10 req/sec
✅ 延遲: < 500ms
✅ 無記憶體洩漏
```

#### **3. 品質驗證**

```
# 測試覆蓋率
pytest --cov=src --cov-report=term-missing

# 程式碼品質
mypy src/ --strict
flake8 src/ tests/
```

**品質標準**:
- ✅ 測試覆蓋率 > 90%
- ✅ 類型檢查 100% 通過
- ✅ 程式碼風格符合規範

#### **4. 效能分析**

```
# 使用監控工具分析
from src.utils import WorkflowMonitor
from src.graph import create_workflow
from src.state.operations import create_initial_state

monitor = WorkflowMonitor()
app = create_workflow()
state = create_initial_state()

result = monitor.profile_workflow(app, state)
print(monitor.generate_report())
```

#### **5. 生成最終報告**

```
Phase 6 測試與優化報告
======================

執行時間: 2025-12-24 14:20
執行者: @ANALYST

測試結果: ✅ PASSED (50+/50+)
測試覆蓋率: 92%
效能達標: ✅ 所有指標通過

測試統計:
├─ 邊界測試: 10/10 通過 ✓
├─ 錯誤處理測試: 8/8 通過 ✓
├─ 整合測試: 8/8 通過 ✓
├─ 效能測試: 5/5 通過 ✓
└─ 其他測試: 19/19 通過 ✓

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

效能瓶頸:
├─ job_matcher_node: 1.2s
├─ recommendation_node: 0.8s
└─ resume_parser_node: 0.3s

優化建議:
1. job_matcher_node 可加入快取機制
2. State 傳遞可使用淺複製
3. JSON 載入可加入快取

結論:
✅ Phase 6 (測試與優化) 完成
✅ 系統達到生產等級
✅ 所有品質指標達標
→ 可進入 Phase 7 (文檔整理)
```

### **執行時間**: ~4 分鐘

---

## 🔄 Agent 協作流程

```
@INFRA (環境準備)
    ↓
    建立測試環境與11個檔案
    ↓
@ARCH (測試架構設計)
    ↓
    設計30+測試案例與工具架構
    ↓
@CODER (程式實現)
    ↓
    實現完整測試套件與工具
    ↓
@ANALYST (驗證分析)
    ↓
    執行測試與效能分析
    ↓
    ✅ Phase 6 完成
```

**⚠️ 無 Checkpoint，全程自動執行！**

---

## 🎯 團隊協作原則

1. **品質優先**
   - 測試覆蓋率 > 90%
   - 所有效能指標達標
   - 生產等級品質

2. **效能導向**
   - 持續監控效能
   - 識別瓶頸
   - 提供優化建議

3. **文檔完善**
   - 測試案例清晰
   - 優化指南完整
   - 生產檢查清單詳盡

4. **自動化驗證**
   - 自動執行測試
   - 自動生成報告
   - 自動品質檢查

---

**Phase 6 讓 AI Agent 達到生產等級！** 🚀
```
