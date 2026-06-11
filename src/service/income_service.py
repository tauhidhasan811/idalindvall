from src.core.session import Session
from src.core.data_processor import ProcessData
from src.core.generate_prompt import GeneratePrompt



class IncomeService:

    @staticmethod
    # def analysis_chat(financial_section: str, chat_history: list[dict], chat_model):
    def analysis_chat( chat_history: list[dict], chat_model):

        # "sections" :["income", "essentials", 'committed_money', "irregular_expense", "net_position"]
        last_message, history = ProcessData.process_chat_history(chat_history=chat_history)

        prompt = GeneratePrompt.common_prompt(
                    # financial_section=financial_section,
                    last_chat=last_message, 
                    previous_history=history
                )

        # if financial_section == "income":
        #     prompt = GeneratePrompt.income_prompt(last_chat=last_message, previous_history=history)

        # elif financial_section == "essentials":
        #     prompt = GeneratePrompt.essentials_prompt(last_chat=last_message, previous_history=history)
        
        response = chat_model.get_response(prompt=prompt)
        # print(type(response))
        clean_response = ProcessData.CleanData(response.content)
        return clean_response

