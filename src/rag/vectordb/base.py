from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

class VectorStoreBase(ABC):
    """
    向量資料庫抽象基底類別，定義向量儲存、檢索、過濾、刪除、持久化等介面。
    """

    @abstractmethod
    def add(self, vectors: List[List[float]], metadatas: List[Dict[str, Any]]) -> List[str]:
        """
        新增多個向量及其 metadata。

        Parameters
        ----------
        vectors : List[List[float]]
            向量列表
        metadatas : List[Dict[str, Any]]
            metadata 字典列表

        Returns
        -------
        List[str]
            新增向量的唯一 ID 列表
        """
        pass

    @abstractmethod
    def search(self, query_vector: List[float], top_k: int, filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        以 query_vector 進行相似度檢索，支援 metadata 過濾。

        Parameters
        ----------
        query_vector : List[float]
            查詢向量
        top_k : int
            返回前 K 筆
        filters : Optional[Dict[str, Any]]
            metadata 過濾條件

        Returns
        -------
        List[Dict[str, Any]]
            檢索結果，每筆包含 id, score, metadata
        """
        pass

    @abstractmethod
    def delete(self, ids: List[str]) -> bool:
        """
        刪除指定 id 的向量。

        Parameters
        ----------
        ids : List[str]
            欲刪除的向量 ID

        Returns
        -------
        bool
            是否成功
        """
        pass

    @abstractmethod
    def save(self, path: str) -> None:
        """
        將索引持久化至檔案。

        Parameters
        ----------
        path : str
            儲存檔案路徑
        """
        pass

    @abstractmethod
    def load(self, path: str) -> None:
        """
        從檔案載入索引。

        Parameters
        ----------
        path : str
            載入檔案路徑
        """
        pass
