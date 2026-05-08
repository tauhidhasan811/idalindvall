from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()
class ConfigAnthropic:
    def __init__(self, model_name='claude-haiku-4-5-20251001'):
        self.model_name = model_name

    def get_anthropic_model(self):
        model = ChatAnthropic(
            model_name=self.model_name,
            temperature=0.8
        )
        return model