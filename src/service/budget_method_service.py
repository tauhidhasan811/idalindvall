from src.core.generate_prompt import GeneratePrompt
from src.core.data_processor import ProcessData
from src.core.create_excel import CreateExcel
from api.schema.budget_method_schema import BudgetMethodInput
from src.config.config_cloudinary import ConfigCloudinary
from uuid import uuid4
import os


class BudgetMethodService:

    @staticmethod
    def calculate_data(user_input, chat_model, cloudinary: ConfigCloudinary):

        data ={}
        methods = ["Command Center", "Irregular Expense System", "Net Position Snapshot", "Monthly Activation"]
        for m in methods:
            prompt = GeneratePrompt.budget_method_prompt(input_data=user_input, budget_method_name=m)
            response = chat_model.get_response(prompt=prompt)
            # print(type(response))
            clean_response = ProcessData.CleanData(response.content)

            data[m] = clean_response

        print('=' * 60)
        print(data)
        print('*' * 40)
        print(type(data))
        print('*' * 40)
        print('=' * 60)

        f_name = str(uuid4())
        excel = CreateExcel(f_name=f_name)
        path = excel.update_excel(data=data)

        result = cloudinary.upload_data_to_cloudinary(path)
        os.remove(path)
        return result
    
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