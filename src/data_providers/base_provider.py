from abc import ABC, abstractmethod

class BaseProvider(ABC):
    @abstractmethod
    def fetch_jobs(self, **kwargs):
        """抽象方法：獲取職缺數據"""
        pass
