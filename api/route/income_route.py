from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.schema.chat_schema import ChatSchema
from fastapi.responses import StreamingResponse
from src.service.income_service import IncomeService
from src.core.chat_with_anthropic import ChatController
from src.hyperparameter import params


router = APIRouter(prefix='/api/ai/financial_section', tags=['Financial Section'])

chat_model = ChatController()


@router.post('/chat')
async def create_new_session(chat_data: ChatSchema):
    try:
        # if chat_data.financial_section not in params['sections']:
        #     return JSONResponse(
        #         status_code=400,
        #         content={
        #             'status': False,
        #             'status_code': 400,
        #             'message': f"Only accepted {params['sections']} sections"
        #         }
        #     )
        chat_history_dict = [item.dict() for item in chat_data.chat_history]
        # financial_section = chat_data.financial_section
        response = IncomeService.analysis_chat(#financial_section=financial_section,
                                            chat_history=chat_history_dict, 
                                            chat_model=chat_model)
        
        message = JSONResponse(
            status_code=200,
            content={
                'status': True,
                'status_code': 200,
                'message': response
            }
        )

        return message
    # except ValueError as ex:

    except Exception as ex:

        message = JSONResponse(
            status_code=500,
            content={
                'status': False,
                'status_code': 500,
                'message': str(ex)
            }
        )

        return message


    
