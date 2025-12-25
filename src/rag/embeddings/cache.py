from typing import List, Optional

class EmbeddingCache:
    """
    向量快取機制，支援 LRU 策略與 hash 鍵管理。
    """

    def __init__(self, max_size: int = 1000) -> None:
        """
        初始化 EmbeddingCache。

        Parameters
        ----------
        max_size : int
            快取最大容量
        """
        self.max_size = max_size
        self.cache = {}
        self.order = []

    def get(self, text: str) -> Optional[List[float]]:
        """
        取得文本對應的向量（若存在）。

        Parameters
        ----------
        text : str
            輸入文本

        Returns
        -------
        Optional[List[float]]
            對應向量或 None
        """
        key = hash(text)
        if key in self.cache:
            # LRU: move to end
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return None

    def set(self, text: str, embedding: List[float]) -> None:
        """
        設定文本對應的向量。

        Parameters
        ----------
        text : str
            輸入文本
        embedding : List[float]
            對應向量
        """
        key = hash(text)
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.max_size:
            # 淘汰最舊
            oldest = self.order.pop(0)
            del self.cache[oldest]
        self.cache[key] = embedding
        self.order.append(key)

    def clear(self) -> None:
        """
        清空快取。
        """
        self.cache.clear()
        self.order.clear()
