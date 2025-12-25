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
