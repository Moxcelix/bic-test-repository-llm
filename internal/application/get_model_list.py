from internal.domain.llm_repository import LLMRepository
from typing import List

class GetModelListUC():
    def __init__(self, repo: LLMRepository):
        self.repo = repo

    def execute(self) -> List[str]:
        return self.repo.get_model_list()