from internal.domain.llm_repository import LLMRepository
from internal.domain.llm_model import Model
from typing import List, Dict


class InMemoryLLMRepository(LLMRepository):
    def __init__(self, deepseek_model: Model):
        self.model_list: Dict[str, Model] = {
            'deepseek-chat': deepseek_model
        }

    def get_model_list(self) -> List[str]:
        return list(self.model_list.keys())

    def get_model_by_name(self, name: str) -> Model:
        if name not in self.model_list:
            raise KeyError(f"Model '{name}' not found in repository")
        return self.model_list[name]