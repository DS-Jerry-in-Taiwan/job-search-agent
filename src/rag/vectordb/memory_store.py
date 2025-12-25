from typing import List, Dict, Any, Optional
from .base import VectorStoreBase
import numpy as np
import uuid
import os

class InMemoryVectorStore(VectorStoreBase):
    """
    純 NumPy 實現的向量資料庫，適用於測試與小型資料集。
    """

    def __init__(self, dim: int) -> None:
        self.dim = dim
        self.vectors: List[List[float]] = []
        self.ids: List[str] = []
        self.metadatas: List[Dict[str, Any]] = []

    def add(self, vectors: List[List[float]], metadatas: List[Dict[str, Any]]) -> List[str]:
        if len(vectors) != len(metadatas):
            raise ValueError("vectors and metadatas must have the same length")
        arr = np.array(vectors, dtype="float32")
        if arr.shape[1] != self.dim:
            raise ValueError(f"vector dimension mismatch: expected {self.dim}, got {arr.shape[1]}")
        new_ids = [str(uuid.uuid4()) for _ in range(len(vectors))]
        self.vectors.extend(arr.tolist())
        self.ids.extend(new_ids)
        self.metadatas.extend(metadatas)
        return new_ids

    def search(self, query_vector: List[float], top_k: int, filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        if len(query_vector) != self.dim:
            raise ValueError(f"query_vector dimension mismatch: expected {self.dim}, got {len(query_vector)}")
        if not self.vectors:
            return []
        arr = np.array(self.vectors, dtype="float32")
        q = np.array(query_vector, dtype="float32")
        dists = np.linalg.norm(arr - q, axis=1)
        idxs = np.argsort(dists)
        results = []
        for idx in idxs:
            meta = self.metadatas[idx]
            id_ = self.ids[idx]
            if filters:
                match = all(meta.get(k) == v for k, v in filters.items())
                if not match:
                    continue
            results.append({"id": id_, "score": float(dists[idx]), "metadata": meta})
            if len(results) >= top_k:
                break
        return results

    def delete(self, ids: List[str]) -> bool:
        idxs = [self.ids.index(i) for i in ids if i in self.ids]
        if not idxs:
            return False
        keep_mask = [i not in idxs for i in range(len(self.ids))]
        self.vectors = [v for i, v in enumerate(self.vectors) if keep_mask[i]]
        self.ids = [id_ for i, id_ in enumerate(self.ids) if keep_mask[i]]
        self.metadatas = [meta for i, meta in enumerate(self.metadatas) if keep_mask[i]]
        return True

    def save(self, path: str) -> None:
        np.savez(path + ".npz", vectors=np.array(self.vectors, dtype="float32"),
                 ids=np.array(self.ids), metas=np.array(self.metadatas, dtype=object))

    def load(self, path: str) -> None:
        data = np.load(path + ".npz", allow_pickle=True)
        self.vectors = data["vectors"].tolist()
        self.ids = list(data["ids"])
        self.metadatas = list(data["metas"])
