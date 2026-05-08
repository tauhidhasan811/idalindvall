import json
from uuid import uuid4
from typing import List, Dict

import re
import ast



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
    
    @staticmethod
    def CleanData(text):
        # Step 1: Remove all literal backslashes
        cleaned = text.replace("\\", "")

        # Step 2: Remove backticks (` or ``` )
        cleaned = re.sub(r"`{1,3}", "", cleaned)

        # Step 3: Remove code language keywords (json, bash, python, etc.)
        cleaned = re.sub(r'\b(json|bash|python)\b', '', cleaned, flags=re.IGNORECASE)

        # Step 4: Remove newlines and extra spaces
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()

        print(f"Cleaned text: {cleaned}")  # For debugging, see how it's being cleaned.

        # Try parsing it as JSON first
        try:
            # Attempt to load it as JSON
            cleaned = json.loads(cleaned)
        except json.JSONDecodeError:
            # If JSON parsing fails, try using literal_eval (assuming it's a Python literal expression)
            try:
                cleaned = ast.literal_eval(cleaned)
            except (ValueError, SyntaxError) as e:
                print(f"Error parsing content with ast.literal_eval: {e}")
                cleaned = None  # Or handle the error as needed (e.g., return a default value or an empty dict/list)

        return cleaned
            
            



