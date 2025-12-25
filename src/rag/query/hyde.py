from typing import List

class HyDEGenerator:
    """
    生成假設性文檔（Hypothetical Document Embeddings）以提升檢索準確度。
    """

    def generate_hypothetical_doc(self, query: str) -> str:
        """
        根據查詢生成一份理想職缺描述。

        Parameters
        ----------
        query : str
            使用者查詢

        Returns
        -------
        str
            生成的假設性文檔
        """
        # 範例：根據查詢生成職缺描述
        if not isinstance(query, str) or not query.strip():
            raise ValueError("Query must be a non-empty string.")
        # 可根據查詢內容組合描述（簡易版）
        return (
            f"We are seeking a talented {query}.\n"
            "Responsibilities include backend development, API design, and cloud deployment.\n"
            "Required skills: Python, Docker, Kubernetes.\n"
            "Company culture: Open, innovative, team-oriented."
        )

    def generate_multiple(self, query: str, top_k: int = 3) -> List[str]:
        """
        生成多份假設性文檔。

        Parameters
        ----------
        query : str
            使用者查詢
        top_k : int, default=3
            生成文檔數量

        Returns
        -------
        list[str]
            多份假設性文檔
        """
        base = self.generate_hypothetical_doc(query)
        # 產生不同風格（簡易範例）
        variations = [base]
        variations.append(base.replace("backend", "frontend"))
        variations.append(base.replace("team-oriented", "remote-friendly"))
        return variations[:top_k]

    def evaluate_quality(self, doc: str) -> float:
        """
        評估生成文檔的品質分數（0~1）。

        Parameters
        ----------
        doc : str
            生成的假設性文檔

        Returns
        -------
        float
            品質分數（0~1）
        """
        # 簡易評分：長度與關鍵詞判斷
        score = 0.5
        if "Responsibilities" in doc and "Required skills" in doc:
            score += 0.25
        if "Company culture" in doc:
            score += 0.25
        return min(score, 1.0)
