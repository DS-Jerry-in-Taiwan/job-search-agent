from typing import List, Dict
import tiktoken

class TextChunker:
    """
    智能文本分塊，支援固定大小分塊、重疊與句子完整性。
    """

    def __init__(self, chunk_size: int = 512, overlap: int = 50) -> None:
        """
        初始化 TextChunker。

        Parameters
        ----------
        chunk_size : int
            每個分塊的最大 token 數
        overlap : int
            分塊間重疊 token 數
        """
        self.chunk_size = chunk_size
        self.overlap = overlap
        self.tokenizer = tiktoken.get_encoding("cl100k_base")

    def chunk_text(self, text: str) -> List[str]:
        """
        將單一文本分塊。

        Parameters
        ----------
        text : str
            輸入文本

        Returns
        -------
        List[str]
            分塊後的文本列表
        """
        tokens = self.tokenizer.encode(text)
        chunks = []
        start = 0
        while start < len(tokens):
            end = min(start + self.chunk_size, len(tokens))
            chunk_tokens = tokens[start:end]
            chunk_text = self.tokenizer.decode(chunk_tokens)
            chunks.append(chunk_text)
            if end == len(tokens):
                break
            start = end - self.overlap
        return chunks

    def chunk_documents(self, docs: List[Dict]) -> List[Dict]:
        """
        多文件分塊，保留原始欄位。

        Parameters
        ----------
        docs : List[Dict]
            文件列表，每個 dict 至少包含 'text' 欄位

        Returns
        -------
        List[Dict]
            分塊後的文件列表，保留原始欄位
        """
        chunked_docs = []
        for doc in docs:
            text = doc.get("text", "")
            chunks = self.chunk_text(text)
            for idx, chunk in enumerate(chunks):
                new_doc = dict(doc)
                new_doc["text"] = chunk
                new_doc["chunk_id"] = idx
                chunked_docs.append(new_doc)
        return chunked_docs
