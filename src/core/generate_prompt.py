from langchain.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import PromptTemplate
from src.hyperparameter import params

class GeneratePrompt:


    @staticmethod
    def common_prompt(financial_section, last_chat, previous_history):
   
        financial_temp = params["output_temp"][financial_section]
        output_temp = {
            "ai_question": "if Complete all question then (your conversational reply to the user if all question and answer are complete)", 
            "progress": 0-100, 
            "complete": False, 
            "data": financial_temp
        }
        collection_order = params["collection_order"][financial_section]


        sys_message = SystemMessage(
            content=(
                "You are the intake guide for The Freedom Budget Method by Ida Lindvall (lilyvall.com). "
                "Conduct a warm, precise, one-question-at-a-time intake conversation to collect all the numbers needed to build a Freedom Budget spreadsheet."
                "VOICE: Calm, warm, precise."
                "Never preachy or shaming. One question at a time. " 
                "Short paragraphs. No bullet points. " 
                "Acknowledge briefly before asking the next question. " 
                "Accept estimates warmly (your best estimate is perfect — we can always refine it later)."
                "Do not offer advice or commentary on the numbers."
                "Do not explain the methodology unless asked."
                "collect data on that following order and if any input is not relevent ask them again"
                "COLLECT IN THIS ORDER"
                    f"{collection_order}"
                "Before finalize make complete ask again you give those value and if all are correct then we may proced"
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
    def budget_method_prompt(input_data):
        # final_output_temp = { 
        #     "ai_question": "Ask your question to user and if any complete give thanks and tell to step",
        #     "progress": 0-100, 
        #     "complete": False, 
            
        # }
        output_temp = {
            "monthly_income": {
                "primary_income": "float",
                "secondary_income": "float",
                "other_income": "float",
                "total_monthly_income": "float",
                "currency": "string"
            },
            "structural_allocation": {
                "essentials": {
                    "suggested_percentage": "float",
                    "your_percentage": "float",
                    "allocated_amount": "float",
                    "status": "string"
                },
                "wealth_building": {
                    "suggested_percentage": "float",
                    "your_percentage": "float",
                    "allocated_amount": "float",
                    "status": "string"
                },
                "future_buffer": {
                    "suggested_percentage": "float",
                    "your_percentage": "float",
                    "allocated_amount": "float",
                    "status": "string"
                },
                "guilt_free_living": {
                    "suggested_percentage": "float",
                    "your_percentage": "float",
                    "allocated_amount": "float",
                    "status": "string"
                },
                "total_allocated_percentage": "float",
                "structure_status": "string"
            },
            "irregular_expense_provision": {
                "monthly_irregular_provision": "float",
                "included_in": "string"
            },
            "automation_reminder": {
                "wealth_building_transfer": {
                    "amount": "float",
                    "instruction": "string"
                },
                "future_buffer_transfer": {
                    "amount": "float",
                    "instruction": "string"
                },
                "guilt_free_living_transfer": {
                    "amount": "float",
                    "instruction": "string"
                },
                "irregular_provision_transfer": {
                    "amount": "float",
                    "instruction": "string"
                }
            }
        }

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
    
