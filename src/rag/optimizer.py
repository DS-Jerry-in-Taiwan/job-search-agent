from typing import Any, Dict, List, Tuple, Optional
import threading
import time

class LRUCache:
    def __init__(self, capacity: int = 1000):
        self.capacity = capacity
        self.cache: Dict[Any, Any] = {}
        self.order: List[Any] = []
        self.lock = threading.Lock()

    def get(self, key: Any) -> Optional[Any]:
        with self.lock:
            if key in self.cache:
                self.order.remove(key)
                self.order.insert(0, key)
                return self.cache[key]
            return None

    def put(self, key: Any, value: Any):
        with self.lock:
            if key in self.cache:
                self.order.remove(key)
            elif len(self.cache) >= self.capacity:
                old_key = self.order.pop()
                del self.cache[old_key]
            self.cache[key] = value
            self.order.insert(0, key)

    def __contains__(self, key: Any) -> bool:
        return key in self.cache

    def __len__(self) -> int:
        return len(self.cache)

class RAGOptimizer:
    def __init__(self, cache_size: int = 1000):
        self.embedding_cache = LRUCache(cache_size)
        self.batch_queue: List[Tuple[str, Any]] = []
        self.cache_hits = 0
        self.cache_misses = 0

    def cache_embedding(self, key: str, value: Any):
        self.embedding_cache.put(key, value)

    def get_cached_embedding(self, key: str) -> Optional[Any]:
        result = self.embedding_cache.get(key)
        if result is not None:
            self.cache_hits += 1
        else:
            self.cache_misses += 1
        return result

    def cache_hit_rate(self) -> float:
        total = self.cache_hits + self.cache_misses
        return self.cache_hits / total if total > 0 else 0.0

    def add_to_batch(self, query: str, meta: Any):
        self.batch_queue.append((query, meta))

    def get_batch(self, batch_size: int = 8) -> List[Tuple[str, Any]]:
        batch = self.batch_queue[:batch_size]
        self.batch_queue = self.batch_queue[batch_size:]
        return batch

    def prewarm(self, queries: List[str]):
        # 預熱快取（可根據實際 embedding 實現）
        for q in queries:
            self.cache_embedding(q, None)

    def optimize(self, docs, user_profile):
        # 目前僅 pass-through，未來可擴充排序/去重/精選等
        return docs
