from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.route.income_route import router as income_router
from api.route.budget_method_route import router as budget_route

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(income_router)
app.include_router(budget_route)