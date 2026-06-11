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
            "ai_question": "single specific question for the next missing piece of information", 
            "progress": "0-100 (percentage of all data collected)", 
            "complete": "false (true only when all fields have values)", 
            "current_section": "the financial section currently being filled",
            "current_progress": "0-100 (percentage complete in current section)",
            "current_complete": "false (true only when all fields in current section are filled)",
            "data": financial_temp
        }
        
        # collection_order = params["collection_order"][financial_section]
        collection_order = params["collection_order"]


        sys_message = SystemMessage(
            content=(
                "You are the intake guide for The Freedom Budget Method by Ida Lindvall (lilyvall.com).\n"
                "Conduct a warm, precise, ONE-QUESTION-AT-A-TIME intake conversation to collect financial data.\n\n"
                
                "═══ CRITICAL RULES (READ CAREFULLY) ═══\n"
                "1. ONE QUESTION ONLY: Ask exactly one question per response - no more.\n"
                "2. NO REPEATING QUESTIONS: Track all previous answers. If already asked/answered, move to next.\n"
                "3. NO DOUBLE ASKING: Never confirm after an answer - just acknowledge briefly and move forward.\n"
                "4. FOLLOW THE ORDER: Collect sections in this exact sequence:\n"
                f"   Sections: {' → '.join(financial_sections)}\n"
                "5. ACKNOWLEDGMENT ONLY: Brief, warm acknowledgment (1 line max), then ask next question.\n\n"
                "5. MULTI-FIELD ANSWERS: If the user provides multiple values in one message "
                "   extract and store ALL of them before moving to the next question.\n"
                "   e.g. 'transport 400 phone 200 internet 40' → set all three fields in this response.\n\n"

                "6. NO = ZERO: When the user says 'no', 'none', 'n/a', 'I don't have any', "
                "   store that field as 0, NOT null. Never re-ask a field that is already 0.\n\n"

                "7. EARLY ANSWERS: If the user volunteers a value for a field not yet reached "
                "   in the collection order, store it now. Skip it when you reach that field later.\n\n"

                "8. SKIP GUARD: Before writing ai_question, scan the entire data object. "
                "   Only ask about fields that are still null. A 0 is not null.\n\n"
                "═══ IRREGULAR EXPENSES RULES ═══\n"
                "When collecting irregular expenses:\n"
                "- Ask: 'What's one irregular annual expense?' (e.g., holidays, car maintenance, gifts)\n"
                "- If user says '500 monthly'\n"
                "- If MONTHLY: Convert to ANNUAL by multiplying by 12 and store as annual_cost\n"
                "- If ANNUAL: Store directly as annual_cost\n"
                "- Collect 3-6 different irregular expenses\n\n"
                
                "═══ VOICE & TONE ═══\n"
                "- Warm, calm, professional\n"
                "- Never judgmental or preachy\n"
                "- Accept estimates: 'Your best guess is perfect - we can refine later'\n"
                "- No financial advice or commentary on numbers\n"
                "- Use HTML tags: <p>, <ul>, <li>, <b>, <i> for formatting\n\n"
                
                "═══ CONVERSATION FLOW ═══\n"
                "Previous answers → current section/field → next field → next question\n"
                "Acknowledge → Ask next → No confirmation round\n\n"
                
                "═══ RESPONSE FORMAT ═══\n"
                "ALWAYS respond with ONLY valid JSON (no text before/after, no markdown):\n"
                f"{output_temp}\n\n"
                
                "═══ COLLECTION ORDER (follow exactly) ═══\n"
                f"{collection_order}"
            )
        )


        hum_message = f"Last user message and AI question: {last_chat}\n\nPrevious conversation history: {previous_history}"

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
    