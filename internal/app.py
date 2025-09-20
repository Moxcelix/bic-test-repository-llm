from internal.application.send_query_to_model import SendQueryToModelUC
from internal.application.get_model_list import GetModelListUC

class App:
    def __init__(self,
                  send_query_to_model_uc: SendQueryToModelUC, 
                  get_model_list_uc: GetModelListUC):
        self.send_query_to_model_uc = send_query_to_model_uc
        self.get_model_list_uc = get_model_list_uc

    def run(self):
        while True:
            msg = input()

            if msg == 'model-list':
                result = self.get_model_list_uc.execute()
                for r in result:
                    print(r)
            elif msg == 'send-query':
                model_name = input('model name:')
                text = input('text:')
                temperature = float(input('temperature:'))
                max_tokens = int(input('max tokens:'))
                result = self.send_query_to_model_uc.execute(
                    model_name, text, temperature, max_tokens)
                print(result)
            elif msg == 'test':
                model_name = 'deepseek-chat'
                text = 'привет, как дела?'
                temperature = 0.7
                max_tokens = 256
                result = self.send_query_to_model_uc.execute(
                    model_name, text, temperature, max_tokens)
                print(result)
            elif msg == 'exit':
                break
