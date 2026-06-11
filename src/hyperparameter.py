params = {
    "sections" :["income", "essentials", 'committed_money', "irregular_expense", "net_position"],
    
    "collection_order": {
        "income": (
            "🏦 INCOME SECTION\n"
            "1. Net income: 'What is your net monthly income (after tax)? This cannot be zero.'\n"
            "2. Secondary income: 'Do you have secondary income (freelance, rental, side work, etc.)? (may be zero)'\n"
            "3. Other income: 'Any other income sources (child support, government payments, distributions, etc.)? (may be zero)'\n"
        ),

        "essentials": (
            "📊 ESSENTIALS SECTION (all monthly amounts)\n"
            "1. Housing: 'What is your monthly housing cost (rent or mortgage)?'\n"
            "2. Food: 'Monthly groceries and regular dining combined?'\n"
            "3. Transport: 'Car payment, fuel, public transport - combined total per month?'\n"
            "4. Insurance: 'All insurance (health, car, home, life) combined per month?'\n"
            "5. Phone: 'Monthly phone bill?'\n"
            "6. Internet: 'Monthly internet (zero if included in rent)?'\n"
            "7. Subscriptions: 'All streaming, software, memberships combined per month?'\n"
            "8. Loans: 'All debt minimum payments (car, student, credit cards, Klarna, etc.) combined per month?'\n"
            "9. Childcare: 'Monthly childcare costs? (may be zero)'\n"
            "10. Gym: 'Gym or fitness costs per month? (may be zero)'\n"
            "11. Other essentials: 'Any other fixed monthly costs? (may be zero)'\n"
        ),
        "committed_money": (
            "💰 COMMITTED MONEY SECTION (all monthly amounts)\n"
            "1. Savings: 'How much do you save monthly? (may be zero)'\n"
            "2. Investments: 'Monthly investment or pension contribution? (may be zero)'\n"
            "3. Extra debt payments: 'Any extra debt payments above minimums per month? (may be zero)'\n"
        ),
        "irregular_expense": (
            "📅 IRREGULAR EXPENSE SECTION (ANNUAL amounts)\n"
            "Collect 3–6 annual expenses. For each:\n"
            "1. Ask: 'What is one annual expense you have?' (e.g., holidays, Christmas gifts, car maintenance, home maintenance, insurance premiums paid annually, school fees, medical costs)\n"
            "2. Get amount: 'How much does that cost per year?' OR 'Is that yearly or monthly?'\n"
            "3. If monthly → Multiply by 12 and store as annual_cost\n"
            "4. If annual → Store directly as annual_cost\n"
            "5. Store as: {\"name\": \"[expense name]\", \"annual_cost\": [annual value]}\n"
            "6. Continue collecting until 3-6 irregular expenses are listed\n"
        ),
        "net_position": (
            "💎 NET POSITION SECTION (current balances, NOT monthly)\n"
            "ASSETS:\n"
            "1. Liquidity reserve: 'Total cash in savings/emergency fund?'\n"
            "2. Investments balance: 'Total value of investment accounts and stocks?'\n"
            "3. Pension balance: 'Total pension or retirement account value?'\n"
            "4. Property equity: 'Property market value minus mortgage balance? (may be zero)'\n"
            "5. Other assets: 'Any other wealth-building assets like boat, vehicle value? (may be zero)'\n"
            "LIABILITIES:\n"
            "6. Mortgage balance: 'Outstanding mortgage balance? (may be zero)'\n"
            "7. Car or boat loan: 'Car or boat loan balance? (may be zero)'\n"
            "8. Student loan: 'Student loan balance? (may be zero)'\n"
            "9. Credit and short-term: 'Credit cards, Klarna, other short-term debt combined balance? (may be zero)'\n"
            "10. Other liabilities: 'Any other liabilities? (may be zero)'\n"
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
            