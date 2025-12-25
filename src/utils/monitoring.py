"""工作流程監控工具"""

import time
from typing import List
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
