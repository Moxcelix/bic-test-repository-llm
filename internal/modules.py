from internal.infrastructure.llm_repository import InMemoryLLMRepository
from internal.infrastructure.deepseek_llm import DeepSeekModel
from internal.application.send_query_to_model import SendQueryToModelUC
from internal.application.get_model_list import GetModelListUC
from internal.config.env import Env

from internal.app import App

class Modules:
    def __init__(self):
        self.env = Env()
        self.deepseek_model = DeepSeekModel(self.env)
        self.llm_repository = InMemoryLLMRepository(self.deepseek_model)
        self.send_query_to_model_uc = SendQueryToModelUC(self.llm_repository)
        self.get_model_list_uc = GetModelListUC(self.llm_repository)

    def create_app(self) -> App:
        app = App(
            self.send_query_to_model_uc,
            self.get_model_list_uc)
        return app