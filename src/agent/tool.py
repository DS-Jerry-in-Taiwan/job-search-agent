from typing import Callable, Any, Dict
from pydantic import BaseModel, ValidationError

class Tool:
    def __init__(
        self,
        name: str,
        func: Callable,
        description: str,
        parameters: Dict
    ):
        self.name = name
        self.func = func
        self.description = description
        self.parameters = parameters

    def run(self, **kwargs) -> Any:
        # 參數驗證（可用 Pydantic 擴充）
        try:
            if self.parameters:
                # 將 self.parameters 轉換為 __annotations__ 格式
                annotations = {k: v[0] for k, v in self.parameters.items()}
                required = {k for k, v in self.parameters.items() if v[1] is ...}
                model_dict = {"__annotations__": annotations}
                model = type(f"{self.name}Params", (BaseModel,), model_dict)
                validated = model(**kwargs)
                return self.func(**validated.dict())
            else:
                return self.func(**kwargs)
        except ValidationError as e:
            raise ValueError(f"Tool '{self.name}' 參數驗證失敗: {e}")

    def to_llm_schema(self) -> Dict:
        # 轉換為 OpenAI Function Calling 格式
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters
        }
