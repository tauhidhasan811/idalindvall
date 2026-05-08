import json
from uuid import uuid4

class Session:
    def __init__(self, session_path):
        self.session_path = session_path

    def __create_session_id(self):
        session_id = str(uuid4())
        json_data = self.read_all_session_data()
        if session_id in json_data:
            session_id = str(uuid4())

        return session_id

    
    def create_new_session(self):
        id = self.__create_session_id()
        update_id = self.update_session_data(session_id=id, session_data=[])
        return update_id
    
    def read_one_session_data(self, session_id):
        all_data = self.read_all_session_data()
        data = all_data[session_id]
        return data
    

    def read_all_session_data(self):
        json_data = {}
        with open(self.session_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        return json_data
    

    def update_session_data(self, session_id: str, session_data: list):
        json_data = self.read_all_session_data()
        json_data[session_id] = session_data
        with open(self.session_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=4)
        return session_id