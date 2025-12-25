from typing import List, Dict, Any, Optional
from whoosh import index
from whoosh.fields import Schema, TEXT, ID, STORED
from whoosh.qparser import QueryParser
import os
import shutil
import tempfile

class BM25Store:
    """
    Whoosh BM25 關鍵字檢索封裝。
    """

    def __init__(self, index_path: str) -> None:
        """
        初始化 BM25Store，指定索引路徑。
        """
        self.index_path = index_path
        self.schema = Schema(id=ID(stored=True, unique=True), content=TEXT(stored=True), metadata=STORED)
        # 若 index_path 目錄存在但未初始化索引，需自動建立
        if os.path.exists(index_path) and index.exists_in(index_path):
            self.ix = index.open_dir(index_path)
        else:
            os.makedirs(index_path, exist_ok=True)
            self.ix = index.create_in(index_path, self.schema)

    def add_documents(self, docs: List[Dict[str, Any]]) -> None:
        """
        新增多筆文件進入索引。
        """
        writer = self.ix.writer()
        for i, doc in enumerate(docs):
            doc_id = doc.get("id", str(i))
            content = doc["content"]
            metadata = doc.get("metadata", {})
            writer.update_document(id=doc_id, content=content, metadata=metadata)
        writer.commit(optimize=True)

    def search(self, query: str, top_k: int = 10, filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        關鍵字搜尋，支援過濾條件。
        """
        qp = QueryParser("content", schema=self.schema)
        # 若查詢為空，使用萬用字元查詢所有文件
        q = qp.parse(query if query.strip() else "*")
        results = []
        with self.ix.searcher() as searcher:
            # Whoosh 的預設 analyzer 不會將 "doc" 匹配到 "doc0"、"doc1" 等，需用萬用字元查詢
            if query.strip():
                # 若查詢字串不含萬用字元，則自動加上尾端萬用字元
                if "*" not in query and "?" not in query:
                    q = qp.parse(query + "*")
                hits = searcher.search(q, limit=top_k * 2)
            else:
                hits = list(searcher.documents())
            for hit in hits:
                meta = hit["metadata"]
                if filters:
                    match = all(meta.get(k) == v for k, v in filters.items())
                    if not match:
                        continue
                results.append({
                    "id": hit["id"],
                    "score": float(hit.get("score", 1.0)),
                    "content": hit["content"],
                    "metadata": meta
                })
                if len(results) >= top_k:
                    break
        return results
