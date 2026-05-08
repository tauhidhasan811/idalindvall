from src.config.config_anthropic import ConfigAnthropic

class ChatController:
    def __init__(self):
        self.model = ConfigAnthropic().get_anthropic_model()

    def get_response(self, prompt):
        response = self.model.invoke(prompt)
        return response
    


# from typing import List
# from collections.abc import AsyncIterable

# from src.config.config_anthropic import ConfigAnthropic



# class ChatController:
#     def __init__(self):
#         self.agent = ConfigAnthropic().get_anthropic_model()

#     def __call_agent(self, prompt):
#         return self.agent.invoke(prompt)

#     async def __call_agent_stream(self, prompt) -> AsyncIterable[str]:
#         async for chunk in self.agent.astream(prompt):
#             content = getattr(chunk, "content", None)

#             if isinstance(content, str) and content:
#                 yield content
#             elif isinstance(content, list):
#                 for item in content:
#                     if isinstance(item, dict) and item.get("type") == "text":
#                         text = item.get("text", "")
#                         if text:
#                             yield text


#     def __get_agent_response(self, prompt):
#         response = self.__call_agent(prompt=prompt)
#         content = response.content
#         return content

#     async def get_response(self, prompt) -> AsyncIterable[str]:
#         try:
#             content= self.__get_agent_response(prompt=prompt)
#             async for chunk in self.__call_agent_stream(prompt=prompt):
#                 yield chunk
#         except Exception as e:
#             yield f"Error: {str(e)}"


        
