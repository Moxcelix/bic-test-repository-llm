import requests
import json
from typing import Dict, Any, Optional

from internal.domain.llm_model import LLMModel
from internal.config.env import Env

class DeepSeekModel(LLMModel):
    def __init__(self, env: Env):
        self.api_key = env.DeepseekApiKey
        self.model = env.DeepseekModel
        self.base_url = env.DeepseekApiUrl
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def query(self, text: str, temperature: float = 0.7, max_tokens: int = 2048) -> str:
        try:
            payload = {
                "model": self.model,
                "messages": [
                    {
                        "role": "user",
                        "content": text
                    }
                ],
                "temperature": temperature,
                "max_tokens": max_tokens,
                "stream": False
            }
            
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            response.raise_for_status()
            
            result = response.json()
            return result['choices'][0]['message']['content']
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error: {e}")
        except KeyError as e:
            raise Exception(f"Unexpected API response format: {e}")
        except json.JSONDecodeError as e:
            raise Exception(f"JSON parsing error: {e}")