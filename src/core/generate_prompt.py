from langchain.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import PromptTemplate

class GeneratePrompt:

    @staticmethod
    def income_prompt(last_chat, previous_history):
        final_output_temp = { 
            "question": "Ask your question to user and if any complete give thanks and tell to step",
            "message": "your conversational reply to the user if all question and answer are complete", 
            "progress": 0-100, 
            "complete": False, 
            "data": { 
                "net_income": int, 
                "secondary_income": int, 
                "other_income": int
            }
        }

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
                    "net_income: Net monthly income (primary, after tax can not zero)"
                    "secondary_income: Secondary income (freelance, rental, side work — may be zero)"
                    "other_income: Other income (child support, government payments, distributions — may  be zero)"

                f"Finally if all data are completly given then update complete value true Give the response the this following structure hardly {final_output_temp}"
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