from typing import List, Dict, Optional

class Memory:
    def __init__(self):
        self.short_term: List[Dict] = []
        self.long_term = None  # 可擴充為向量記憶

    def add(self, role: str, content: str):
        self.short_term.append({"role": role, "content": content})

    def get_recent(self, n: int = 5) -> List[Dict]:
        return self.short_term[-n:]

    def search(self, query: str, top_k: int = 3) -> List[Dict]:
        # 簡單關鍵字檢索（可擴充語意檢索/向量記憶）
        results = [item for item in self.short_term if query in item["content"]]
        return results[-top_k:]
