from typing import List, Dict, Any

class ContextAssembler:
    """
    將 Phase 10 檢索結果組裝為 LLM 最佳上下文格式。
    """

    def assemble(self, query: str, jobs: List[Dict[str, Any]], user_profile: Dict[str, Any]) -> str:
        """
        組裝 LLM 上下文。

        Parameters
        ----------
        query : str
            用戶查詢
        jobs : List[Dict[str, Any]]
            檢索後職缺列表
        user_profile : Dict[str, Any]
            用戶技能、經驗、地點偏好

        Returns
        -------
        str
            LLM 輸入上下文
        """
        pass
