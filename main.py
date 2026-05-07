from src.service.prompt_service import GeneratePrompt
from src.core.data_processor import ProcessData
from uuid import uuid4
# chat_history = [
#     {
#         "ai_question": "1hi",
#         "user_answer": "1lkvjnkls"
#     },
#     {
#         "ai_question": "2hi2",
#         "user_answer": "2lkvjnkls"
#     },
#     {
#         "ai_question": "3hi2",
#         "user_answer": "3lkvjnkls"
#     }
# ]
# last_chat, prev_history = ProcessData.ProcessChat(chat_history=chat_history)

# print("Last Chat: ",last_chat)
# print("Previous Chat: ",prev_history)
# prompt = GeneratePrompt.income_prompt(last_chat=last_chat, previous_history=prev_history)

# # print(prompt)
data =  [
      {
          "ai_question": "1hi",
          "user_answer": "1lkvjnkls"
      },
      {
          "ai_question": "2hi2",
          "user_answer": "2lkvjnkls"
      },
      {
          "ai_question": "3hi2",
          "user_answer": "3lkvjnkls"
      }
  ]

print('read all data')
ProcessData.read_all_session_data()
print('read all data')
ProcessData.update_session_data( data)

session_id = uuid4()

print(session_id)