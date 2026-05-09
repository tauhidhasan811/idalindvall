from fastapi import APIRouter
from api.schema.budget_method_schema import BudgetMethodInput
from src.service.budget_method_service import BudgetMethodService
from src.core.chat_with_anthropic import ChatController
from src.config.config_cloudinary import ConfigCloudinary

cloudinary = ConfigCloudinary()
router = APIRouter(prefix='/api/ai/income', tags=['Budget Method'])

chat_model = ChatController()

@router.post('budget-method')
async def budget_method(budget_method : BudgetMethodInput):
    input_data = BudgetMethodService.convert_data_to_dict(budget_method=budget_method)
    response = BudgetMethodService.calculate_data(user_input=input_data, chat_model=chat_model, cloudinary=cloudinary)

    return response
