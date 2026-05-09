from src.core.generate_prompt import GeneratePrompt
from src.core.data_processor import ProcessData
from api.schema.budget_method_schema import BudgetMethodInput

class BudgetMethodService:

    @staticmethod
    def calculate_data(user_input, chat_model):
        prompt = GeneratePrompt.budget_method_prompt(input_data=user_input)
        response = chat_model.get_response(prompt=prompt)
        # print(type(response))
        clean_response = ProcessData.CleanData(response.content)
        return clean_response
    
    @staticmethod
    def convert_data_to_dict(budget_method: BudgetMethodInput):

        input_data = {
            "income": budget_method.income.model_dump(),
            "essentials": budget_method.essentials.model_dump(),
            "committed_money": budget_method.committed_money.model_dump(),
            "irregular_expense": [
                item.model_dump() for item in budget_method.irregular_expense
            ],
            "net_position": budget_method.net_position.model_dump()
        }

        return input_data