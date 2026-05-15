from datetime import datetime


def get_cell_map(data, budget_method_name):

    # current_month = datetime.now().strftime("%B")
    current_month_year = datetime.now().strftime("%B %Y")

    # =========================
    # Command Center
    # =========================
    if budget_method_name == "Command Center":
        return {
            "B11": data["monthly_income"]["primary_income"],
            "B12": data["monthly_income"]["secondary_income"],
            "B13": data["monthly_income"]["other_income"],

            # "C19": data["structural_allocation"]["essentials"]["your_percentage"],

            # "C20": data["structural_allocation"]["wealth_building"]["your_percentage"],
            # "E20": data["structural_allocation"]["wealth_building"]["status"],

            # "C21": data["structural_allocation"]["future_buffer"]["your_percentage"],
            # "E21": data["structural_allocation"]["future_buffer"]["status"],

            # "C22": data["structural_allocation"]["guilt_free_living"]["your_percentage"],
            # "E22": data["structural_allocation"]["guilt_free_living"]["status"],

            # "B28": data["irregular_expense_provision"]["monthly_irregular_provision"]
        }

    # =========================
    # Irregular Expense System
    # =========================
    elif budget_method_name == "Irregular Expense System":
        return {

            # Home & Property
            "B11": data["categories"]["Home & Property"]["Home insurance (annual)"]["annualCost"],
            "B12": data["categories"]["Home & Property"]["Home maintenance & repairs"]["annualCost"],
            "B13": data["categories"]["Home & Property"]["Appliance replacement fund"]["annualCost"],

            # Transport
            "B16": data["categories"]["Transport"]["Car insurance (annual)"]["annualCost"],
            "B17": data["categories"]["Transport"]["Car service / MOT"]["annualCost"],
            "B18": data["categories"]["Transport"]["Road tax"]["annualCost"],
            "B19": data["categories"]["Transport"]["Tyres & maintenance"]["annualCost"],


            # Family
            "B22": data["categories"]["Family"]["School fees / activities"]["annualCost"],
            "B23": data["categories"]["Family"]["Children's clothing & equipment"]["annualCost"],
            "B24": data["categories"]["Family"]["Birthday & Christmas gifts"]["annualCost"],

            # Lifestyle
            "B27": data["categories"]["Lifestyle"]["Holidays & travel"]["annualCost"],
            "B28": data["categories"]["Lifestyle"]["Clothing & seasonal wardrobe"]["annualCost"],
            "B29": data["categories"]["Lifestyle"]["Annual memberships"]["annualCost"],
            # Health
            "B32": data["categories"]["Health"]["Dental / medical (annual)"]["annualCost"],
            "B33": data["categories"]["Health"]["Glasses / contacts"]["annualCost"],
            "B34": data["categories"]["Health"]["Other health costs"]["annualCost"],


            # Other
            "B37": data["categories"]["Other"]["Other annual cost 1"]["annualCost"],
            "B38": data["categories"]["Other"]["Other annual cost 2"]["annualCost"],
            "B39": data["categories"]["Other"]["Other annual cost 3"]["annualCost"],
        }

    # =========================
    # Net Position Snapshot
    # =========================
    elif budget_method_name == "Net Position Snapshot":
        return {

            # Liquidity Reserve
            "B12": data["liquidityReserve"]["items"]["Cash & Immediate Access Buffers"]["currentValue"],

            # Wealth Velocity Assets
            "B16": data["wealthVelocityAssets"]["items"]["Investments (funds, stocks, ETFs)"]["currentValue"],
            "B17": data["wealthVelocityAssets"]["items"]["Pension / retirement accounts"]["currentValue"],
            "B18": data["wealthVelocityAssets"]["items"]["Property — full market value"]["currentValue"],
            "B19": data["wealthVelocityAssets"]["items"]["Other wealth-building assets"]["currentValue"],

            # Structural Liabilities
            "B24": data["structuralLiabilities"]["items"]["Mortgage"]["currentValue"],
            "B25": data["structuralLiabilities"]["items"]["Car loan"]["currentValue"],
            "B26": data["structuralLiabilities"]["items"]["Student loans"]["currentValue"],
            "B27": data["structuralLiabilities"]["items"]["Credit cards & short-term debt"]["currentValue"],
            "B28": data["structuralLiabilities"]["items"]["Other liabilities"]["currentValue"],
        }

    # =========================
    # Monthly Activation
    # =========================
    elif budget_method_name == "Monthly Activation":
        return {
            # "B10": current_month
            "B10": current_month_year,
            "B11": data["Income this month (after tax)"]


        }

    # =========================
    # Default Empty Response
    # =========================
    return {}
