import json

from langchain.messages import HumanMessage, SystemMessage, AIMessage

from langchain_core.prompts import PromptTemplate
from src.hyperparameter import params
from src.budget_method_output_parameters import budget_prompt_temp
class GeneratePrompt:
    @staticmethod
    def common_prompt(last_chat, latest_10, previous_history):
        financial_sections = ["income", "essentials", 'committed_money', "irregular_expense", "net_position"]
        
        financial_temp = { 
            "income": { 
                "net_income": float, 
                "secondary_income": float, 
                "other_income": float
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
                    "name": None, 
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
        
        collection_order = params["collection_order"]


        sys_message = SystemMessage(
            content=(
                "You are the intake guide for The Freedom Budget Method by Ida Lindvall (lilyvall.com).\n"
                "You collect financial data ONE QUESTION AT A TIME, in a warm and calm tone.\n"
                "Do not use currency symbols unless the user mentions a currency.\n\n"

                "═══ YOUR TASK EACH TURN ═══\n"
                "You are given CURRENT DATA (already collected) and the USER'S LATEST MESSAGE.\n"
                "1. Apply the user's latest message as an update to CURRENT DATA (see rules below).\n"
                "2. Return the FULL updated data object — copy over every existing value unchanged, "
                "only add/modify what the latest message tells you.\n"
                "3. Find the first field that is still null, following the section order:\n"
                f"   {' → '.join(financial_sections)}\n"
                "4. Ask ONE short question for that field. If nothing is null, set ai_question='' and complete=true.\n\n"

                "═══ INTERPRETING ANSWERS ═══\n"
                "- A 0 is a real value, not null. Never re-ask a field that already has a value (incl. 0).\n"
                "- If the user gives multiple values in one message, fill in all matching fields.\n"
                "- 'no' / 'none' / 'n/a' / 'nothing' / \"don't have\" → store 0 for the field being asked. "
                "Do not ask for confirmation, just move on.\n"
                "- If the user volunteers a value for a field not yet asked, store it now (skip it later).\n"
                "- If the latest message gives NO usable value for the field you just asked about "
                "(empty, off-topic, 'clarify the question', etc.), leave that field null and re-ask it "
                "with a shorter or rephrased question. Do not advance to the next field, and do not "
                "repeat the exact same wording as your last question.\n"
                "- If the user says 'that's all' / 'no other' / 'nothing else' while some fields in the "
                "current section are still null: list those field names in plain language and ask ONE "
                "yes/no confirmation that they're all 0. On the user's NEXT reply — if affirmative, set "
                "all of them to 0 and move to the next section; if they give corrections, apply those and "
                "zero the rest. Never repeat this confirmation.\n\n"

                "═══ INCOME ═══\n"
                "Income figures are monthly as given. Never ask whether income is monthly or yearly.\n\n"

                "═══ IRREGULAR EXPENSES (list of {name, annual_cost}) ═══\n"
                "- Ask for one irregular annual expense at a time (e.g. holidays, car maintenance, gifts, repairs).\n"
                "- If the user's figure already states a period ('per month', '/month', 'monthly', "
                "'per year', '/year', 'annually'), use it directly — do NOT ask monthly-or-yearly.\n"
                "- Otherwise ask once: monthly or yearly?\n"
                "- Monthly → annual_cost = amount × 12. Yearly → store as-is.\n"
                "- This conversion applies ONLY to irregular_expense items.\n"
                "- Collect 3-6 items, or stop early if the user says no more, then move to net_position.\n\n"

                "═══ NET POSITION ═══\n"
                "1. liquidity_reserve — Total cash in savings or emergency fund?"
                "2. investments_balance — Total value of investment accounts and stocks?"
                "3. pension_balance — Total value of your pension or retirement account?"
                "4. property_equity — Total value of your property (market value) minus any mortgage balance on it?"
                "5. other_assets — ask normally; if user has none, store 0. (This may get incremented later in step 6 or 7.)"
                "6. mortgage_balance — Do you have any outstanding mortgage balance on that property?"
                    "If non-zero: ask once → What was the original purchase price of that property? → add that amount to other_assets."
                        "If 0/none: skip the follow-up entirely."

                "7. car_or_boat_loan — Do you have any loans for vehicles, equipment, or other assets?"

                    "If non-zero AND the original-price question was NOT already asked in step 6: ask once → What was the original purchase price of that asset? → add to other_assets."
                    "If step 6 already asked it, never ask again here."


                "8. student_loan — Do you have any outstanding student loan balance?"
                "9. credit_and_short_term — Any credit card or short-term debt balances?"
                "10. other_liabilities — Any other debts or liabilities not covered above?"

                "═══ TONE & FORMAT ═══\n"
                "Warm, calm, professional. One brief acknowledgment line, then the next question. No "
                "financial advice or commentary on the numbers. HTML tags <p>, <ul>, <li>, <b>, <i> allowed "
                "in ai_question for formatting.\n\n"

                "═══ OUTPUT ═══\n"
                "Respond with ONLY valid JSON, no markdown fences, no text outside the JSON, matching "
                "exactly this shape:\n"
                f"{output_temp}\n\n"

                "═══ DATA SHAPE ═══\n"
                f"{financial_temp}\n\n"

                "═══ COLLECTION ORDER ═══\n"
                f"{collection_order}"
            )
        )


        hum_message = (
            f"═══ LAST MESSAGE (Most Recent) ═══\n"
            f"{last_chat}\n\n"
            f"═══ LATEST 5-10 MESSAGES (Recent Context) ═══\n"
            f"{latest_10}\n\n"
            f"═══ EARLIER CONVERSATION HISTORY (Background) ═══\n"
            f"{previous_history}"
        )

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
    
