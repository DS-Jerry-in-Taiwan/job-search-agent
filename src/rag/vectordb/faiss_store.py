from typing import List, Dict, Any, Optional
from .base import VectorStoreBase
import faiss
import numpy as np
import uuid
import os

class FaissVectorStore(VectorStoreBase):
    """
    FAISS 向量資料庫介面，支援向量儲存、檢索、metadata 過濾與索引持久化。
    """

    def __init__(self, dim: int, metric: str = "l2") -> None:
        """
        初始化 FAISS 向量資料庫。

        Parameters
        ----------
        dim : int
            向量維度
        metric : str
            相似度度量方式 ("l2" 或 "ip")
        """
        if metric == "l2":
            self.index = faiss.IndexFlatL2(dim)
        elif metric == "ip":
            self.index = faiss.IndexFlatIP(dim)
        else:
            raise ValueError("metric must be 'l2' or 'ip'")
        self.dim = dim
        self.ids: List[str] = []
        self.metadatas: List[Dict[str, Any]] = []

    def add(self, vectors: List[List[float]], metadatas: List[Dict[str, Any]]) -> List[str]:
        if len(vectors) != len(metadatas):
            raise ValueError("vectors and metadatas must have the same length")
        arr = np.array(vectors, dtype="float32")
        if arr.shape[1] != self.dim:
            raise ValueError(f"vector dimension mismatch: expected {self.dim}, got {arr.shape[1]}")
        self.index.add(arr)
        new_ids = [str(uuid.uuid4()) for _ in range(len(vectors))]
        self.ids.extend(new_ids)
        self.metadatas.extend(metadatas)
        return new_ids

    def search(self, query_vector: List[float], top_k: int, filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        if len(query_vector) != self.dim:
            raise ValueError(f"query_vector dimension mismatch: expected {self.dim}, got {len(query_vector)}")
        if self.index.ntotal == 0:
            return []
        arr = np.array([query_vector], dtype="float32")
        D, I = self.index.search(arr, top_k * 2)  # 先多取，後面過濾
        results = []
        for idx, score in zip(I[0], D[0]):
            if idx < 0 or idx >= len(self.ids):
                continue
            meta = self.metadatas[idx]
            id_ = self.ids[idx]
            if filters:
                match = all(meta.get(k) == v for k, v in filters.items())
                if not match:
                    continue
            results.append({"id": id_, "score": float(score), "metadata": meta})
            if len(results) >= top_k:
                break
        return results

    def delete(self, ids: List[str]) -> bool:
        # FAISS IndexFlatL2 不支援動態刪除，只能重建索引
        idxs = [self.ids.index(i) for i in ids if i in self.ids]
        if not idxs:
            return False
        keep_mask = [i not in idxs for i in range(len(self.ids))]
        kept_vecs = self.index.reconstruct_n(0, self.index.ntotal)[keep_mask]
        kept_ids = [id_ for i, id_ in enumerate(self.ids) if keep_mask[i]]
        kept_metas = [meta for i, meta in enumerate(self.metadatas) if keep_mask[i]]
        self.index = faiss.IndexFlatL2(self.dim)
        if len(kept_vecs) > 0:
            self.index.add(np.array(kept_vecs, dtype="float32"))
        self.ids = kept_ids
        self.metadatas = kept_metas
        return True

    def save(self, path: str) -> None:
        faiss.write_index(self.index, str(path) + ".faiss")
        # metadata/ids
        meta_path = str(path) + ".meta"
        # 確保與 faiss index 同目錄
        import pathlib
        pathlib.Path(meta_path).parent.mkdir(parents=True, exist_ok=True)
        # 強制同步寫入，避免 pytest 臨時目錄延遲
        import io
        with open(meta_path, "wb") as f:
            np.savez(f, ids=np.array(self.ids), metas=np.array(self.metadatas, dtype=object))

    def load(self, path: str) -> None:
        self.index = faiss.read_index(str(path) + ".faiss")
        meta_path = str(path) + ".meta"
        if not os.path.exists(meta_path):
            raise FileNotFoundError(f"Metadata file not found: {meta_path}")
        meta = np.load(meta_path, allow_pickle=True)
        self.ids = list(meta["ids"])
        self.metadatas = list(meta["metas"])
