import json
from uuid import uuid4
from typing import List, Dict

class ProcessData:

    @staticmethod
    def read_all_session_data():
        path = r'data\session_data\session_data.json'
        json_data = {}
        with open(path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        print(json_data)

    @staticmethod
    def update_session_data(session_data: list):
        path = r'data\session_data\session_data.json'
        json_data = {}
        with open(path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        print(json_data)
        session_id = str(uuid4())
        if session_id in json_data:
            session_id = str(uuid4())
        json_data[session_id] = session_data
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=4)



    @staticmethod
    def ProcessChat(chat_history: List[Dict]):
        last_conv = {}
        if len(chat_history)> 0:
            chat = chat_history[-1]
            last_conv['ai_question'] = chat.get("ai_question", "No Question")
            last_conv['user_answer'] = chat.get("user_answer", "No response")
        chat_history.pop()

        return last_conv, chat_history
            
            



