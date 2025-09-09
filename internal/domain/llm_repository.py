from .llm_model import Model
from typing import List

class LLMRepository:
    def get_model_list() -> List[str]: pass
    def get_model_by_name(name: str) -> Model: pass