from pydantic import BaseModel
from typing import List, Dict

class ChatItems(BaseModel):
    ai_question: str
    user_answer: str

class ChatSchema(BaseModel):
    chat_history: List[ChatItems]