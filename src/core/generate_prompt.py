from langchain.messages import HumanMessage, SystemMessage, AIMessage

from langchain_core.prompts import PromptTemplate
from src.hyperparameter import params
from src.budget_method_output_parameters import budget_prompt_temp
class GeneratePrompt:


    @staticmethod
    def common_prompt(last_chat, previous_history):
        financial_sections = ["income", "essentials", 'committed_money', "irregular_expense", "net_position"]
        
        financial_temp = { 
            "income": { 
                "net_income": int, 
                "secondary_income": int, 
                "other_income": int
            },
            "essentials": {
                "housing": float, 
                "food": float, 
                "transport": float, 
                "insurance": float, 
                "phone": float, 
                "internet": float, 
                "subscriptions": float, 
                "loans": float, 
                "childcare": float, 
                "gym": float, 
                "other_essentials": float
            },
            "committed_money": {
                "savings": float,
                "investments": float,
                "extra_debt_payments": float,
            },
            "irregular_expense": [
                {
                    "name": str, 
                    "annual_cost": float
                },
                {
                    "name": str, 
                    "annual_cost": float
                }
            ],
            
            "net_position": {
                "liquidity_reserve": float, 
                "investments_balance": float, 
                "pension_balance": float, 
                "property_equity": float, 
                "other_assets": float, 
                "mortgage_balance": float, 
                "car_or_boat_loan": float, 
                "student_loan": float, 
                "credit_and_short_term": float, 
                "other_liabilities": float
            }
        }
        
        output_temp = {
            "ai_question": "if Complete all question then (your conversational reply to the user if all question and answer are complete)", 
            "progress": 0-100, 
            "complete": False, 
            "current_section": "financial_section_name",
            "current_progress": 0-100,
            "current_complete": False,


            "data": financial_temp
        }
        
        # collection_order = params["collection_order"][financial_section]
        collection_order = params["collection_order"]


        sys_message = SystemMessage(
            content=(
                "You are the intake guide for The Freedom Budget Method by Ida Lindvall (lilyvall.com). "
                "Conduct a warm, precise, one-question-at-a-time intake conversation to collect all the numbers needed to build a Freedom Budget spreadsheet."
                "VOICE: Calm, warm, precise."
                "Never preachy or shaming. One question at a time. " 
                "Short paragraphs. and use html tag like <p>, <ul>, <li>" 
                "Acknowledge briefly before asking the next question. " 
                "Accept estimates warmly (your best estimate is perfect — we can always refine it later)."
                "Do not offer advice or commentary on the numbers."
                "Do not explain the methodology unless asked."
                "All response use html tag like <p>, <ul>, <li>, <table>, italic, bold"
                "collect data on that following order and if any input is not relevent ask them again"
                # "Currency is Swedish krona(kr) so do not need to mension the currecy on amount show like  {amount} SEK  "
                
                "COLLECT IN THIS ORDER"
                    f"financial sections are {financial_sections}"
                        f"{collection_order}"
                "Before finalize make complete ask again you give those value and if all are correct then we may proced if all step completed then"
                f"Finally if all data are completly given then update complete value true Give the response the this following structure hardly {output_temp} "
                "And all response must After every user reply, respond with ONLY valid JSON in this exact structure — no text before or after, no markdown fence "
                "If user last chat like user answer are not relevent with the question then again repeat the question and tell them to answe"
                
            )
        )


        hum_message = f"Last chat: {last_chat}Previous chat : {previous_history}"

        temp = PromptTemplate(
            template="{sys_message} \n\n {hum_message}",
            input_variables=["sys_message", "hum_message"]
        )

        prompt = temp.invoke(
            input={
                "sys_message": sys_message.content,
                "hum_message": hum_message
            }
        )

        return prompt
    

    @staticmethod
    # def budget_method_prompt(input_data, budget_method_name):
    def budget_method_prompt(input_data):


        # output_temp = budget_prompt_temp[budget_method_name]
        output_temp = budget_prompt_temp

        sys_message = SystemMessage(
            content=(
                "You are the intake guide for The Freedom Budget Method by Ida Lindvall. "
                "Your task is to calculate the Command Center budget data based on the user's provided financial input. "
                "Return ONLY valid JSON. Do not include explanations, markdown, or text before or after the JSON. "
                f"The JSON must follow this exact structure: {output_temp}. "
                "Replace each 'float' placeholder with a numeric float value. "
                "Replace each 'string' placeholder with a string value. "
                "If a value is missing from the user input, use 0.0 for float fields and an empty string for string fields. "
                "All percentages must be numeric values, for example 56.0, not '56%'. "
                "All currency amounts must be numeric values only, without currency symbols or commas."
            )
        )

        hum_message = f"User input data: {input_data}"

        temp = PromptTemplate(
            template="{sys_message}\n\n{hum_message}",
            input_variables=["sys_message", "hum_message"]
        )
        prompt = temp.invoke(
            input={
                "sys_message": sys_message.content,
                "hum_message": hum_message
            }
        )

        return prompt
    
