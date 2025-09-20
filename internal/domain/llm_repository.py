from internal.domain.llm_model import Model
from typing import List

class LLMRepository:
    def get_model_list(self) -> List[str]: pass
    def get_model_by_name(self, name: str) -> Model: pass