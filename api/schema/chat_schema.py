from pydantic import BaseModel
from typing import List, Dict

class ChatItems(BaseModel):
    ai_question: str
    user_answer: str

class ChatSchema(BaseModel):
    # financial_section: str
    chat_history: List[ChatItems]