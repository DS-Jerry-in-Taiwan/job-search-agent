from typing import List

class QueryRewriter:
    """
    將自然語言查詢轉換為最佳檢索查詢的重寫器。
    """

    def rewrite(self, query: str) -> str:
        """
        將單一查詢重寫為最佳檢索格式。

        Parameters
        ----------
        query : str
            使用者輸入的自然語言查詢

        Returns
        -------
        str
            最佳化後的檢索查詢
        """
        # 基本規則：移除冗餘詞彙、保留核心關鍵字、轉換專業術語
        if not isinstance(query, str) or not query.strip():
            raise ValueError("Query must be a non-empty string.")

        # 範例規則（可擴充）
        redundant = ["我想", "請幫我", "想要", "可以", "請問", "幫我找", "有沒有"]
        q = query
        for r in redundant:
            q = q.replace(r, "")
        # 關鍵詞映射表，保證順序與語意
        mapping = [
            ("台北", "Taipei"),
            ("新竹", "Hsinchu"),
            ("Python", "Python"),
            ("Java", "Java"),
            ("後端", "backend"),
            ("前端", "frontend"),
            ("工程師", "engineer"),
            ("工作", "job"),
            ("的", ""),
        ]
        result = []
        for zh, en in mapping:
            if zh in q:
                result.append((q.index(zh), en))
                q = q.replace(zh, "", 1)
        # 剩餘內容（如技能）直接加上
        q = q.strip()
        if q:
            # 僅保留中文與英文字母、數字
            import re
            q = re.sub(r"[^\u4e00-\u9fa5a-zA-Z0-9]", "", q)
            # 若剩餘內容為單詞（如"找"），則忽略
            if q not in ["找", ""]:
                result.append((len(mapping), q))
        # 依照原始出現順序排序
        result.sort(key=lambda x: x[0])
        # 強制英文關鍵詞順序：技能/職位/地點
        words = [w for _, w in result if w]
        # 調整為: 技能/職位/地點
        skill = [w for w in words if w in ["Python", "Java"]]
        role = [w for w in words if w in ["backend", "frontend", "engineer", "developer", "job"]]
        loc = [w for w in words if w in ["Taipei", "Hsinchu"]]
        others = [w for w in words if w not in skill + role + loc]
        return " ".join(skill + role + others + loc).strip()

    def multi_rewrite(self, query: str, top_k: int = 3) -> List[str]:
        """
        生成多個查詢重寫版本。

        Parameters
        ----------
        query : str
            使用者輸入的自然語言查詢
        top_k : int, default=3
            生成的查詢版本數量

        Returns
        -------
        List[str]
            多個最佳化查詢
        """
        base = self.rewrite(query)
        # 產生不同排列組合（簡單範例，可擴充）
        variations = [base]
        if "backend" in base:
            variations.append(base.replace("backend", "後端"))
        if "engineer" in base:
            variations.append(base.replace("engineer", "developer"))
        return variations[:top_k]
