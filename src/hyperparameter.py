params = {
    "sections" :["income", "essentials", 'committed_money', "irregular_expense", "net_position"],
    
    "collection_order": {
        "income": (
            "net_income: Net monthly income (primary, after tax can not zero)"
            "secondary_income: Secondary income (freelance, rental, side work — may be zero)"
            "other_income: Other income (child support, government payments, distributions — may  be zero)"
        ),

        "essentials": (
            "housing: Rent or mortgage (or combined if both apply)"
            "food: Groceries and regular dining combined"
            "transport: Car payment, fuel, public transport — combined total"
            "insurance: All insurance policies combined (health, car, home, life)"
            "phone: Monthly phone bill"
            "internet: Monthly internet (zero if included in rent)"
            "subscriptions: All streaming, software, memberships — combined total"
            "loans: All debt minimum payments (car loan, student loan, credit cards, Klarna, etc.) — combined minimums only"
            "childcare: Monthly childcare costs (may be zero)"
            "gym: Gym or fitness costs (may be zero)"
            "other_essentials: Any other fixed monthly costs not covered above (may be zero)"
        ),
        "committed_money": (
            "savings: Monthly savings contribution (may be zero)"
            "investments: Monthly investment or pension contribution (may be zero)"
            "extra_debt_payments: Any extra debt payments above minimums (may be zero)"
        ),
        "irregular_expense": (
            "Collect 3–6 annual expenses. For each, get a name and annual cost."
             "Examples: holidays, Christmas/gifts, car maintenance, home maintenance, boat costs, insurance premiums paid annually, school fees, medical costs."
             'Store as an array: [{"name": "Holidays", "annual_cost": 40000}, ...]'

        ),
        "net_position": (
            "liquidity_reserve: Total cash in savings accounts or emergency fund (current balance, not monthly — may be zero)"
            "investments_balance: Total value of investment accounts and stocks"
            "pension_balance: Total pension or retirement account value"
            "property_equity: Property market value minus mortgage balance (may be zero)"
            "other_assets: Any other wealth-building assets (e.g. boat, vehicle value — may be zero)"
            "mortgage_balance: Outstanding mortgage balance (may be zero)"
            "car_or_boat_loan: Car or boat loan balance (may be zero)"
            "student_loan: Student loan balance (may be zero)"
            "credit_and_short_term: Credit cards, Klarna, and other short-term debt — combined balance (may be zero)"
            "other_liabilities: Any other liabilities (may be zero)"
        ),
    },
    "output_temp": { 

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
}

cell_design = {
    "Command Center":{
        # "B11", "B12", "B13",
        # "D19", "D20", "D21", "D22",
        # "B28", "B32", "B33", "B34", "B35"
    },
    "Irregular Expense System": {
        # "B11", "B12", "B13",
        # "B16", "B17", "B18",
        # "B22", "B23", "B24",
        # "B27", "B28", "B29",
        # "B32", "B33", "B34",
        # "B37", "B38", "B39",
    }, 
    "Net Position Snapshot": {
        # "B16", "B17", "B18", "B19",
        # "B24", "B25", "B26", "B27", "B28"
    }, 
    "Monthly Activation": {
        # "B11"
    }
}
            