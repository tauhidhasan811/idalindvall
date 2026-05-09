# import json
# from openpyxl import load_workbook
# from openpyxl.styles import PatternFill, Font
# from openpyxl.cell import MergedCell
# from src.cellmaper import get_cell_map

# file_path = 'Freedom.xlsx'
# wb = load_workbook(file_path)


from src.core.create_excel import CreateExcel

# data = {
#     "Command Center": {
#         "monthly_income": {
#             "primary_income": 85000.0,
#             "secondary_income": 15000.0,
#             "other_income": 5000.0,
#         },

#         "structural_allocation": {
#             "essentials": {
#                 "suggested_percentage": 50,
#                 "your_percentage": 52.5,
#                 "allocated_amount": 55125.0,
#                 "status": "Healthy"
#             },

#             "wealth_building": {
#                 "suggested_percentage": 20,
#                 "your_percentage": 18.0,
#                 "allocated_amount": 18900.0,
#                 "status": "Good"
#             },

#             "future_buffer": {
#                 "suggested_percentage": 10,
#                 "your_percentage": 12.0,
#                 "allocated_amount": 12600.0,
#                 "status": "Strong"
#             },

#             "guilt_free_living": {
#                 "suggested_percentage": 20,
#                 "your_percentage": 17.5,
#                 "allocated_amount": 18375.0,
#                 "status": "Balanced"
#             },

#             "total_allocated_percentage": 100.0,
#             "structure_status": "SYSTEM STABLE"
#         },

#         "irregular_expense_provision": {
#             "monthly_irregular_provision": 8500.0,
#             "included_in": "Future Buffer"
#         },

#         "automation_reminder": {
#             "wealth_building_transfer": {
#                 "amount": 18900.0,
#                 "instruction": "Transfer to investment account automatically"
#             },

#             "future_buffer_transfer": {
#                 "amount": 12600.0,
#                 "instruction": "Transfer to emergency savings"
#             },

#             "guilt_free_living_transfer": {
#                 "amount": 18375.0,
#                 "instruction": "Transfer to spending account"
#             },

#             "irregular_provision_transfer": {
#                 "amount": 8500.0,
#                 "instruction": "Transfer to irregular expense reserve"
#             }
#         }
#     },

#     "Irregular Expense System": {
#         "categories": {
#             "Home & Property": {
#                 "Home insurance (annual)": {
#                     "annualCost": 24000.0,
#                     "monthlyProvision": 2000.0,
#                     "notes": "Renew every January",
#                     "category": "Home & Property"
#                 },

#                 "Home maintenance & repairs": {
#                     "annualCost": 36000.0,
#                     "monthlyProvision": 3000.0,
#                     "notes": "General repairs",
#                     "category": "Home & Property"
#                 }
#             },

#             "Transport": {
#                 "Car insurance (annual)": {
#                     "annualCost": 48000.0,
#                     "monthlyProvision": 4000.0,
#                     "notes": "Premium coverage",
#                     "category": "Transport"
#                 },

#                 "Road tax": {
#                     "annualCost": 12000.0,
#                     "monthlyProvision": 1000.0,
#                     "notes": "",
#                     "category": "Transport"
#                 }
#             }
#         },

#         "totals": {
#             "totalAnnualIrregularCosts": 120000.0,
#             "totalMonthlyProvision": 10000.0,
#             "currency": "kr",
#             "note": "This feeds into your Command Center automatically"
#         },

#         "surpriseEliminationScore": {
#             "label": "How well is your structure engineering out financial volatility?",
#             "monthlyProvisionRunning": 10000.0,
#             "annualCostsCovered": True,
#             "coverageStatus": "Fully Covered",
#             "monthsOfExpensesProvisioned": 12.0,
#             "target": 12.0,
#             "targetStatus": "Target Achieved"
#         }
#     },

#     "Net Position Snapshot": {
#         "liquidityReserve": {
#             "label": "Cash & immediately accessible funds.",
#             "target": "5–10% of total assets",

#             "items": {
#                 "Cash & Immediate Access Buffers": {
#                     "currentValue": 250000.0,
#                     "targetStatus": "Healthy"
#                 }
#             },

#             "total": 250000.0
#         },

#         "wealthVelocityAssets": {
#             "label": "Investments and property assets.",

#             "items": {
#                 "Investments (funds, stocks, ETFs)": {
#                     "currentValue": 450000.0
#                 },

#                 "Pension / retirement accounts": {
#                     "currentValue": 350000.0
#                 },

#                 "Property — full market value": {
#                     "currentValue": 6500000.0,
#                     "notes": "Current estimated market value"
#                 },

#                 "Other wealth-building assets": {
#                     "currentValue": 100000.0
#                 }
#             },

#             "total": 7400000.0,
#             "targetStatus": "Growing"
#         },

#         "structuralLiabilities": {
#             "label": "Outstanding liabilities.",

#             "items": {
#                 "Mortgage": {
#                     "currentValue": 3200000.0,
#                     "notes": "Remaining home loan"
#                 },

#                 "Car loan": {
#                     "currentValue": 180000.0
#                 },

#                 "Student loans": {
#                     "currentValue": 90000.0
#                 },

#                 "Credit cards & short-term debt": {
#                     "currentValue": 25000.0
#                 },

#                 "Other liabilities": {
#                     "currentValue": 10000.0
#                 }
#             },

#             "total": 3505000.0,
#             "targetStatus": "Manageable"
#         },

#         "propertyEquity": {
#             "label": "True ownership stake.",
#             "propertyMarketValue": 6500000.0,
#             "outstandingMortgage": 3200000.0,
#             "truePropertyEquity": 3300000.0,
#             "notes": "Property value minus mortgage"
#         },

#         "netStructuralPosition": {
#             "value": 3895000.0,
#             "status": "SYSTEM STABLE",
#             "notes": "Financial structure is healthy",
#             "currency": "kr"
#         },

#         "structuralBenchmarks": {
#             "label": "Financial benchmark indicators.",

#             "items": {
#                 "Liquidity Reserve %": {
#                     "value": 6.2,
#                     "target": "5–10% of total assets"
#                 },

#                 "Investments & Pension %": {
#                     "value": 21.5,
#                     "target": "Growing year on year"
#                 },

#                 "Property Equity %": {
#                     "value": 44.0,
#                     "target": "Your ownership share"
#                 },

#                 "Loan-to-Value (mortgage)": {
#                     "value": 49.2,
#                     "target": "<80% — under 70% is strong"
#                 },

#                 "Consumer Debt Ratio": {
#                     "value": 1.8,
#                     "target": "<5% of total assets"
#                 }
#             }
#         }
#     },

#     "Monthly Activation": {
#         "This Month": {
#             "overview": {
#                 "month": "May 2026",
#                 "incomeThisMonth": 105000.0,
#                 "structuralChanges": "Salary increased by 5%",
#                 "notes": {
#                     "income": "Income updated",
#                     "structuralChanges": "Added additional savings goal"
#                 }
#             },

#             "netPositionThisMonth": {
#                 "systemStatus": "SYSTEM STABLE",
#                 "statusNote": "Complete checklist and continue."
#             },

#             "monthlyActivationChecklist": {
#                 "label": "Monthly review checklist.",

#                 "items": {
#                     "income": {
#                         "task": "Review monthly income",
#                         "notes": "Confirmed",
#                         "category": "Income",
#                         "completed": True
#                     },

#                     "wealthBuilding": {
#                         "task": "Confirm investment transfer",
#                         "notes": "Transfer completed",
#                         "category": "Wealth Building",
#                         "completed": True
#                     },

#                     "futureBuffer": {
#                         "task": "Confirm emergency savings transfer",
#                         "notes": "Completed",
#                         "category": "Future Buffer",
#                         "completed": True
#                     },

#                     "guiltFree": {
#                         "task": "Transfer guilt-free spending amount",
#                         "notes": "Completed",
#                         "category": "Lifestyle",
#                         "completed": True
#                     }
#                 },

#                 "allCompleted": True
#             },

#             "nextSteps": {
#                 "nextReviewDate": "2026-06-01",
#                 "primaryStructuralFocus": "Increase investment allocation",
#                 "notes": "Reduce unnecessary subscriptions",

#                 "hints": {
#                     "nextReviewDate": "Set reminder now",
#                     "primaryStructuralFocus": "Focus on one goal only"
#                 }
#             }
#         }
#     }
# }

data = {'Command Center': {'monthly_income': {'primary_income': 5200.0, 'secondary_income': 850.0, 'other_income': 200.0}, 'structural_allocation': {'essentials': {'your_percentage': 56.04}, 'wealth_building': {'your_percentage': 13.48, 'status': ''}, 'future_buffer': {'your_percentage': 30.48, 'status': ''}, 'guilt_free_living': {'your_percentage': 0.0, 'status': ''}}, 'irregular_expense_provision': {'monthly_irregular_provision': 425.0}}, 'Irregular Expense System': {'categories': {'Home & Property': {'Home insurance (annual)': {'annualCost': 0.0}, 'Home maintenance & repairs': {'annualCost': 0.0}}, 'Transport': {'Car insurance (annual)': {'annualCost': 0.0}, 'Car service / MOT': {'annualCost': 1200.0}, 'Road tax': {'annualCost': 0.0}}, 'Family': {'School fees / activities': {'annualCost': 0.0}, 'Birthday & Christmas gifts': {'annualCost': 0.0}}, 'Lifestyle': {'Holidays & travel': {'annualCost': 3000.0}, 'Clothing & seasonal wardrobe': {'annualCost': 0.0}}, 'Health': {'Dental / medical (annual)': {'annualCost': 900.0}}, 'Other': {'Other annual cost 1': {'annualCost': 0.0}, 'Other annual cost 2': {'annualCost': 0.0}, 'Other annual cost 3': {'annualCost': 0.0}}}}, 'Net Position Snapshot': {'liquidityReserve': {'items': {'Cash & Immediate Access Buffers': {'currentValue': 15000.0}}}, 'wealthVelocityAssets': {'items': {'Investments (funds, stocks, ETFs)': {'currentValue': 42000.0}, 'Pension / retirement accounts': {'currentValue': 38000.0}, 'Property — full market value': {'currentValue': 95000.0}, 'Other wealth-building assets': {'currentValue': 7000.0}}}, 'structuralLiabilities': {'items': {'Mortgage': {'currentValue': 120000.0}, 'Car loan': {'currentValue': 14000.0}, 'Student loans': {'currentValue': 9000.0}, 'Credit cards & short-term debt': {'currentValue': 2500.0}, 'Other liabilities': {'currentValue': 1000.0}}}}, 'Monthly Activation': {'income': {'net_income': 5200.0, 'secondary_income': 850.0, 'other_income': 200.0, 'total_income': 6250.0}, 'essentials': {'housing': 1600.0, 'food': 650.0, 'transport': 300.0, 'insurance': 250.0, 'phone': 60.0, 'internet': 80.0, 'subscriptions': 45.0, 'loans': 400.0, 'childcare': 500.0, 'gym': 40.0, 'other_essentials': 150.0, 'total_essentials': 4075.0, 'essentials_percentage': 65.2}, 'committed_money': {'savings': 700.0, 'investments': 500.0, 'extra_debt_payments': 200.0, 'total_committed': 1400.0, 'committed_percentage': 22.4}, 'irregular_expenses': {'items': [{'name': 'Car Maintenance', 'annual_cost': 1200.0, 'monthly_allocation': 100.0}, {'name': 'Vacation', 'annual_cost': 3000.0, 'monthly_allocation': 250.0}, {'name': 'Medical Expenses', 'annual_cost': 900.0, 'monthly_allocation': 75.0}], 'total_annual_irregular': 5100.0, 'total_monthly_allocation': 425.0, 'irregular_percentage': 6.8}, 'discretionary': {'total_discretionary': 350.0, 'discretionary_percentage': 5.6}, 'net_position': {'assets': {'liquidity_reserve': 15000.0, 'investments_balance': 42000.0, 'pension_balance': 38000.0, 'property_equity': 95000.0, 'other_assets': 7000.0, 'total_assets': 197000.0}, 'liabilities': {'mortgage_balance': 120000.0, 'car_or_boat_loan': 14000.0, 'student_loan': 9000.0, 'credit_and_short_term': 2500.0, 'other_liabilities': 1000.0, 'total_liabilities': 146500.0}, 'net_worth': 50500.0}, 'budget_summary': {'total_monthly_income': 6250.0, 'total_monthly_expenses': 5900.0, 'monthly_surplus': 350.0, 'budget_allocation': {'essentials_percentage': 65.2, 'committed_percentage': 22.4, 'irregular_percentage': 6.8, 'discretionary_percentage': 5.6}}}}
excel = CreateExcel()
excel.update_excel(data=data)


# cell_map = {
#     "B11": data["monthly_income"]["primary_income"],
#     "B12": data["monthly_income"]["secondary_income"],
#     "B13": data["monthly_income"]["other_income"],
#     "B19": data["structural_allocation"]["essentials"]["suggested_percentage"],
#     "C19": data["structural_allocation"]["essentials"]["your_percentage"],
#     "D19": data["structural_allocation"]["essentials"]["allocated_amount"],
#     "B20": data["structural_allocation"]["wealth_building"]["suggested_percentage"],
#     "C20": data["structural_allocation"]["wealth_building"]["your_percentage"],
#     "D20": data["structural_allocation"]["wealth_building"]["allocated_amount"],
#     "E19": data["structural_allocation"]["wealth_building"]["status"],
#     "B21": data["structural_allocation"]["future_buffer"]["suggested_percentage"],
#     "C21": data["structural_allocation"]["future_buffer"]["your_percentage"],
#     "D21": data["structural_allocation"]["future_buffer"]["allocated_amount"],
#     "E21": data["structural_allocation"]["future_buffer"]["status"],
#     "B22": data["structural_allocation"]["guilt_free_living"]["suggested_percentage"],
#     "C22": data["structural_allocation"]["guilt_free_living"]["your_percentage"],
#     "D22": data["structural_allocation"]["guilt_free_living"]["allocated_amount"],
#     "E22": data["structural_allocation"]["guilt_free_living"]["status"],
#     "E24": data["structural_allocation"]["structure_status"],
#     "B28": data["irregular_expense_provision"]["monthly_irregular_provision"],
#     "B32": data["automation_reminder"]["wealth_building_transfer"]["amount"],
#     "C32": data["automation_reminder"]["wealth_building_transfer"]["instruction"],
#     "B33": data["automation_reminder"]["future_buffer_transfer"]["amount"],
#     "C33": data["automation_reminder"]["future_buffer_transfer"]["instruction"],
#     "B34": data["automation_reminder"]["guilt_free_living_transfer"]["amount"],
#     "C34": data["automation_reminder"]["guilt_free_living_transfer"]["instruction"],
#     "B35": data["automation_reminder"]["irregular_provision_transfer"]["amount"],
#     "C35": data["automation_reminder"]["irregular_provision_transfer"]["instruction"],
# }

# budget_method_name="Command Center"
# income_cells = {"B11", "B12", "B13", "D19", "D20", "D21", "D22", "B28", "B32", "B33", "B34", "B35"}
# cell_map = get_cell_map(data=data, budget_method_name=budget_method_name)


# def get_top_left_cell(ws, cell_addr):
#     """If cell_addr is part of a merged range, return the top-left cell of that range."""
#     for merged_range in ws.merged_cells.ranges:
#         if cell_addr in merged_range:
#             # Return the top-left cell of the merged range
#             return ws.cell(row=merged_range.min_row, column=merged_range.min_col)
#     return ws[cell_addr]

# # Remove the for loop over all sheets, target only "Command Center"
# ws = wb[budget_method_name]

# for cell_addr, value in cell_map.items():
#     cell = get_top_left_cell(ws, cell_addr)

#     orig_fill = cell.fill
#     orig_font = cell.font

#     cell.value = value

#     cell.fill = PatternFill(
#         start_color=orig_fill.start_color,
#         end_color=orig_fill.end_color,
#         fill_type=orig_fill.fill_type
#     )
#     cell.font = Font(
#         name=orig_font.name, size=orig_font.size,
#         bold=orig_font.bold, italic=orig_font.italic,
#         color=orig_font.color
#     )

#     if cell_addr in income_cells:
#         cell.number_format = '#,##0 "kr"'

# wb.save('updated_file.xlsx')
# print("All cells updated successfully!")