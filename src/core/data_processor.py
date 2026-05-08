import json
from uuid import uuid4
from typing import List, Dict

class ProcessData:

    @staticmethod
    def process_chat_history(chat_history: List[Dict]):
        last_conv = {}
        if len(chat_history)> 0:
            chat = chat_history[-1]
            last_conv['ai_question'] = chat.get("ai_question", "No Question")
            last_conv['user_answer'] = chat.get("user_answer", "No response")
        chat_history.pop()

        return last_conv, chat_history
            
            



