from typing import List
from dotenv import load_dotenv
import os
import openai
import time

load_dotenv()

class EmbeddingManager:
    """
    統一向量化管理，負責文本向量化與批次處理。
    """

    def __init__(self, model: str = "text-embedding-3-small", dimensions: int = 1536) -> None:
        """
        初始化 EmbeddingManager。

        Parameters
        ----------
        model : str
            使用的 embedding 模型名稱
        dimensions : int
            向量維度
        """
        self.model = model
        self.dimensions = dimensions
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise RuntimeError("OPENAI_API_KEY not set in environment or .env file.")
        openai.api_key = self.api_key

    def embed_text(self, text: str) -> List[float]:
        """
        將單一文本轉換為向量。

        Parameters
        ----------
        text : str
            輸入文本

        Returns
        -------
        List[float]
            向量表示
        """
        for attempt in range(3):
            try:
                response = openai.embeddings.create(
                    input=[text],
                    model=self.model
                )
                embedding = response.data[0].embedding
                if len(embedding) != self.dimensions:
                    raise ValueError(f"Embedding length {len(embedding)} != {self.dimensions}")
                return embedding
            except Exception as e:
                if attempt == 2:
                    raise
                time.sleep(1 + attempt)
        raise RuntimeError("Embedding failed after retries.")

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """
        批次文本向量化。

        Parameters
        ----------
        texts : List[str]
            多個輸入文本

        Returns
        -------
        List[List[float]]
            向量列表
        """
        if not texts:
            return []
        for attempt in range(3):
            try:
                response = openai.embeddings.create(
                    input=texts,
                    model=self.model
                )
                embeddings = [item.embedding for item in response.data]
                for emb in embeddings:
                    if len(emb) != self.dimensions:
                        raise ValueError(f"Embedding length {len(emb)} != {self.dimensions}")
                return embeddings
            except Exception as e:
                if attempt == 2:
                    raise
                time.sleep(1 + attempt)
        raise RuntimeError("Batch embedding failed after retries.")
