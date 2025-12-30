from typing import Any
import tiktoken

class ContextCompressor:
    """
    Token 壓縮控制，確保 LLM 輸入 < max_tokens。
    """

    def __init__(self, encoding: str = "cl100k_base"):
        self.encoding = encoding

    def count_tokens(self, text: str) -> int:
        enc = tiktoken.get_encoding(self.encoding)
        return len(enc.encode(text))

    def compress(self, context: str, max_tokens: int = 2000) -> str:
        """
        壓縮上下文內容至指定 token 數。
        優先保留前段與關鍵資訊，超出則截斷。
        """
        if self.count_tokens(context) <= max_tokens:
            return context
        # 粗略分段，逐步截斷
        lines = context.splitlines()
        compressed = []
        token_count = 0
        for line in lines:
            line_tokens = self.count_tokens(line)
            if token_count + line_tokens > max_tokens:
                break
            compressed.append(line)
            token_count += line_tokens
        # 若還超過，直接截斷字元
        result = "\n".join(compressed)
        while self.count_tokens(result) > max_tokens:
            result = result[:-10]
        return result
