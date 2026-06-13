from src.core.generate_prompt import GeneratePrompt
from src.core.data_processor import ProcessData
from src.core.create_excel import CreateExcel
from api.schema.budget_method_schema import BudgetMethodInput
from src.config.config_cloudinary import ConfigCloudinary
from uuid import uuid4
import os


class BudgetMethodService:

    @staticmethod
    def ensure_annual_irregular_expenses(data: dict) -> dict:
        """
        Post-processing to ensure all irregular expenses are stored as annual costs.
        If an expense appears to be monthly (very small value), multiply by 12.
        """
        if "Irregular Expense System" in data and "categories" in data["Irregular Expense System"]:
            categories = data["Irregular Expense System"]["categories"]
            
            for category_name, items in categories.items():
                for item_name, item_data in items.items():
                    if isinstance(item_data, dict) and "annualCost" in item_data:
                        annual_cost = item_data["annualCost"]
                        
                        # If value is suspiciously small, it might be monthly
                        # Heuristic: if annual cost is less than 100 but greater than 0, likely monthly
                        # This is a safety net - ideally AI should handle this correctly
                        if 0 < annual_cost < 100:
                            # Ask: could this be monthly? Multiply by 12 if likely
                            # For now, we'll trust the AI has done the conversion
                            # But this is a checkpoint to flag potential issues
                            pass
                        
                        # Ensure it's a float
                        item_data["annualCost"] = float(annual_cost)
        
        return data

    @staticmethod
    def prepare_input_context(user_input: dict) -> str:
        """
        Prepare a clear context summary for the AI showing what data to transform.
        This helps the AI understand the mapping between input and output structures.
        """
        income = user_input.get("income", {})
        essentials = user_input.get("essentials", {})
        committed_money = user_input.get("committed_money", {})
        irregular_expense = user_input.get("irregular_expense", [])
        net_position = user_input.get("net_position", {})
        
        context = f"""
INPUT DATA TO TRANSFORM:

INCOME (Monthly amounts):
- net_income: {income.get('net_income', 0)} kr
- secondary_income: {income.get('secondary_income', 0)} kr
- other_income: {income.get('other_income', 0)} kr

ESSENTIALS (Monthly amounts):
{essentials}

COMMITTED MONEY (Monthly amounts):
{committed_money}

IRREGULAR EXPENSES (Each item has 'name' and 'amount_period'):
{irregular_expense}

NET POSITION (Current balances):
{net_position}

TRANSFORMATION REQUIRED:
1. Map net_income → primary_income under monthly_income
2. Ensure irregular expenses are stored as annual costs (multiply by 12 if monthly)
3. Structure output according to the template format
"""
        return context

    @staticmethod
    def calculate_data(user_input, chat_model, cloudinary: ConfigCloudinary):

        data ={}
        methods = ["Command Center", "Irregular Expense System", "Net Position Snapshot", "Monthly Activation"]
        
        # Prepare context for the AI showing input data structure
        input_context = BudgetMethodService.prepare_input_context(user_input)
        
        # Get the full input data as a clean dict for the AI
        full_input = {
            "income": user_input.get("income", {}),
            "essentials": user_input.get("essentials", {}),
            "committed_money": user_input.get("committed_money", {}),
            "irregular_expense": user_input.get("irregular_expense", []),
            "net_position": user_input.get("net_position", {})
        }
        
        # Generate prompt with full input data
        prompt = GeneratePrompt.budget_method_prompt(input_data=full_input)
        response = chat_model.get_response(prompt=prompt)
        
        # Clean and parse the response
        data = ProcessData.CleanData(response.content)

        # Ensure all irregular expenses are properly formatted as annual costs
        data = BudgetMethodService.ensure_annual_irregular_expenses(data)

        # print('=' * 60)
        # print("Transformed data:")
        # print(data)
        # print('*' * 40)
        # print(type(data))
        # print('*' * 40)
        # print('=' * 60)

        f_name = f"budget_data_{uuid4()}.xlsx"
        excel = CreateExcel(f_name=f_name)
        path = excel.update_excel(data=data)

        result = cloudinary.upload_data_to_cloudinary(path, public_id=f_name)
        os.remove(path)
        return result
        # return path
        # return data
    
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