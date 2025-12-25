from typing import List, Dict, Any

class ContextFormatter:
    """
    將組裝後的資料格式化為 LLM 友好 Markdown Prompt。
    """

    def format_context(self, query: str, jobs: List[Dict[str, Any]], analysis: Dict[str, Any]) -> str:
        """
        產生 LLM 輸入格式的 Markdown prompt。

        Parameters
        ----------
        query : str
            用戶查詢
        jobs : List[Dict[str, Any]]
            精選職缺
        analysis : Dict[str, Any]
            匹配分析、分數等

        Returns
        -------
        str
            LLM 輸入 Markdown prompt
        """
        pass
