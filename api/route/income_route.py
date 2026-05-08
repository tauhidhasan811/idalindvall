from fastapi import APIRouter
from api.schema.chat_schema import ChatSchema

router = APIRouter(prefix='/api/ai/income', tags=['Income'])

@router.post('/create-session')
async def create_new_session(chat_data: ChatSchema):
    return 
    
