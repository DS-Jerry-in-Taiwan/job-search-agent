"""LLMClient 實作（Mock版）

提供 generate(prompt: str) -> str 方法，回傳固定 JSON 字串。
"""

class LLMClient:
    def generate(self, prompt: str) -> str:
        # 可根據 prompt 模擬不同回應
        if "識別意圖" in prompt:
            return '{"intents": ["search_job", "analyze_salary"]}'
        if "提取" in prompt:
            return '{"location": "台北", "skill": "AI", "salary_range": "80萬以上"}'
        return '{}'
