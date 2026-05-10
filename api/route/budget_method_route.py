import pydantic_core
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from api.schema.budget_method_schema import BudgetMethodInput
from src.service.budget_method_service import BudgetMethodService
from src.core.chat_with_anthropic import ChatController
from src.config.config_cloudinary import ConfigCloudinary

cloudinary = ConfigCloudinary()
router = APIRouter(prefix='/api/ai/income', tags=['Budget Method'])

chat_model = ChatController()

@router.post('budget-method')
async def budget_method(budget_method : BudgetMethodInput):
    try:
        input_data = BudgetMethodService.convert_data_to_dict(budget_method=budget_method)
        response = BudgetMethodService.calculate_data(user_input=input_data, chat_model=chat_model, cloudinary=cloudinary)

        message = JSONResponse(
            status_code=200,
            content={
                'status': True,
                'status_code': 200,
                'message': response
            }
        )

        return message
    
    except ValueError as ex:

        if type(ex) ==pydantic_core._pydantic_core.ValidationError:
            error = ex.errors()[0]['msg']
        
        else:
            error = str(ex)
        message = JSONResponse(
            status_code=400,
            content={
                'status': False,
                'status_code': 400,
                'message': error
            }
        )

        return message
    
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

    return response
