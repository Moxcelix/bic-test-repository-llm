from internal.domain.llm_repository import LLMRepository
from internal.domain.llm_model import LLMModel

class SendQueryToModelUC:
    def __init__(self, repo: LLMRepository):
        self.repo = repo

    def execute(self, model_name: str, text: str, temperature: float, max_tokens: int) -> str:
        if not text or not text.strip():
            raise ValueError("Query text is empty")
        
        if temperature < 0 or temperature > 2:
            raise ValueError("Temperature must be between 0 and 2")
        
        if max_tokens <= 0 or max_tokens > 4096:
            raise ValueError("Max tokens value must be between 1 and 4096")

        try:
            model = self.repo.get_model_by_name(model_name)
        except KeyError as e:
            raise ValueError(f"Model '{model_name}' not found") from e
        
        try:
            response = model.query(
                text=text,
                temperature=temperature,
                max_tokens=max_tokens
            )
            return response
        except Exception as e:
            raise Exception(f"Error sending model request: {e}")