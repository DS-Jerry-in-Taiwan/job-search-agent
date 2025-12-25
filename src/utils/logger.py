"""AI Agent 日誌工具"""

import logging
from typing import Any

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

    def log_node_execution(self, node_name: str, duration: float) -> None:
        """記錄 Node 執行時間"""
        self.logger.info(f"Node '{node_name}' executed in {duration:.2f}s")

    def log_state_update(self, state_key: str, value: Any) -> None:
        """記錄 State 更新"""
        self.logger.debug(f"State updated: {state_key} = {value}")

    def log_error(self, error: Exception) -> None:
        """記錄錯誤"""
        self.logger.error(f"Error occurred: {error}", exc_info=True)

    def log_performance(self, metric: str, value: float) -> None:
        """記錄效能指標"""
        self.logger.info(f"Performance: {metric} = {value:.2f}")

# 全局實例
logger = AgentLogger()
