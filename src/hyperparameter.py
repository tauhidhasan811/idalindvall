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
        )
    },
    "output_temp": { 

        "income": { 
            "ai_question": "if Complete all question then (your conversational reply to the user if all question and answer are complete)", 
            "progress": 0-100, 
            "complete": False, 
            "data": { 
                "net_income": int, 
                "secondary_income": int, 
                "other_income": int
            }
        },
        "essentials": {
            "ai_question": "if Complete all question then (your conversational reply to the user if all question and answer are complete)", 
            "progress": 0-100, 
            "complete": False, 
            "data": { 
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
            }
        }
    }
}