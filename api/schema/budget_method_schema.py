from pydantic import BaseModel, Field
from typing import List


class IncomeItem(BaseModel):
    net_income: float = 0.0
    secondary_income: float = 0.0
    other_income: float = 0.0


class EssentialsItem(BaseModel):
    housing: float = 0.0
    food: float = 0.0
    transport: float = 0.0
    insurance: float = 0.0
    phone: float = 0.0
    internet: float = 0.0
    subscriptions: float = 0.0
    loans: float = 0.0
    childcare: float = 0.0
    gym: float = 0.0
    other_essentials: float = 0.0


class CommittedMoneyItem(BaseModel):
    savings: float = 0.0
    investments: float = 0.0
    extra_debt_payments: float = 0.0


class IrregularExpenseItem(BaseModel):
    name: str = ""
    annual_cost: float = 0.0


class NetPositionItem(BaseModel):
    liquidity_reserve: float = 0.0
    investments_balance: float = 0.0
    pension_balance: float = 0.0
    property_equity: float = 0.0
    other_assets: float = 0.0
    mortgage_balance: float = 0.0
    car_or_boat_loan: float = 0.0
    student_loan: float = 0.0
    credit_and_short_term: float = 0.0
    other_liabilities: float = 0.0


class BudgetMethodInput(BaseModel):
    income: IncomeItem = Field(default_factory=IncomeItem)
    essentials: EssentialsItem = Field(default_factory=EssentialsItem)
    committed_money: CommittedMoneyItem = Field(default_factory=CommittedMoneyItem)
    irregular_expense: List[IrregularExpenseItem] = Field(default_factory=list)
    net_position: NetPositionItem = Field(default_factory=NetPositionItem)