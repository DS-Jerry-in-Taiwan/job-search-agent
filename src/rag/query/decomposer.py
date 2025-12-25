from typing import List, Any

class QueryDecomposer:
    """
    複雜查詢分解器，將複雜查詢拆解為多個子查詢並合併結果。
    """

    def decompose(self, query: str) -> List[str]:
        """
        將複雜查詢分解為多個子查詢。

        Parameters
        ----------
        query : str
            使用者輸入的複雜查詢

        Returns
        -------
        List[str]
            拆解後的子查詢列表
        """
        # 支援 AND/OR 拆解（簡易範例）
        if not isinstance(query, str) or not query.strip():
            raise ValueError("Query must be a non-empty string.")
        # 假設以 "或"、"和" 分割
        import re
        or_split = re.split(r"或|OR", query)
        sub_queries = []
        for part in or_split:
            and_split = re.split(r"和|AND", part)
            for sub in and_split:
                sub_queries.append(sub.strip())
        # 去除重複與空值
        return [q for q in set(sub_queries) if q]

    def merge_results(self, results: List[Any]) -> Any:
        """
        合併多個子查詢的檢索結果。

        Parameters
        ----------
        results : List[Any]
            各子查詢的檢索結果

        Returns
        -------
        Any
            合併後的最終結果
        """
        # 簡易合併：串接所有結果
        if not isinstance(results, list):
            raise ValueError("Results must be a list.")
        merged = []
        for r in results:
            if isinstance(r, list):
                merged.extend(r)
            else:
                merged.append(r)
        # 去重
        return list(set(merged))
