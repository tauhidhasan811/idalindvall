from fastapi import APIRouter
from api.schema.chat_schema import ChatSchema
from fastapi.responses import StreamingResponse
from src.service.income_service import IncomeService
from src.core.chat_with_anthropic import ChatController


router = APIRouter(prefix='/api/ai/income', tags=['Income'])

chat_model = ChatController()


@router.post('/chat')
async def create_new_session(chat_data: ChatSchema):
    chat_history_dict = [item.dict() for item in chat_data.chat_history]
    financial_section = chat_data.financial_section
    response = IncomeService.analysis_chat(financial_section=financial_section,
                                           chat_history=chat_history_dict, 
                                           chat_model=chat_model)

    # response = chat_model.get_response(prompt=prompt)

    return response


    # chat_model.get_response(prompt=prompt)
    # return StreamingResponse(chat_model.get_response(prompt=prompt), media_type='text/event-stream')

    
