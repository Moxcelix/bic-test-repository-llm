import os
from dotenv import load_dotenv

class Env:
    def __init__(self):
        load_dotenv() 
        self.DeepseekApiKey = os.environ['DEEPSEEK_API_KEY']
        self.DeepseekApiUrl = os.environ['DEEPSEEK_API_URL']
        self.DeepseekModel = os.environ['DEEPSEEK_MODEL']