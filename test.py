# import json
# from openpyxl import load_workbook
# from openpyxl.styles import PatternFill, Font
# from openpyxl.cell import MergedCell
# from src.cellmaper import get_cell_map

# file_path = 'Freedom.xlsx'
# wb = load_workbook(file_path)


from src.core.create_excel import CreateExcel

data = {
    "Command Center": {
        "monthly_income": {
            "primary_income": 85000.0,
            "secondary_income": 15000.0,
            "other_income": 5000.0,
        },

        "structural_allocation": {
            "essentials": {
                "your_percentage": 52.5,
            },

            "wealth_building": {
                "your_percentage": 18.0,
                "status": "Good"
            },

            "future_buffer": {
                "your_percentage": 12.0,
                "status": "Strong"
            },

            "guilt_free_living": {
                "your_percentage": 17.5,
                "status": "Balanced"
            },
        },

        "irregular_expense_provision": {
            "monthly_irregular_provision": 8500.0,
        }
    },

    "Irregular Expense System": {
        "categories": {

            "Home & Property": {
                "Home insurance (annual)": {
                    "annualCost": 24000.0
                },

                "Home maintenance & repairs": {
                    "annualCost": 36000.0
                }
            },

            "Transport": {
                "Car insurance (annual)": {
                    "annualCost": 48000.0
                },

                "Car service / MOT": {
                    "annualCost": 18000.0
                },

                "Road tax": {
                    "annualCost": 12000.0
                }
            },

            "Family": {
                "School fees / activities": {
                    "annualCost": 60000.0
                },

                "Birthday & Christmas gifts": {
                    "annualCost": 15000.0
                }
            },

            "Lifestyle": {
                "Holidays & travel": {
                    "annualCost": 85000.0
                },

                "Clothing & seasonal wardrobe": {
                    "annualCost": 25000.0
                }
            },

            "Health": {
                "Dental / medical (annual)": {
                    "annualCost": 10000.0
                }
            },

            "Other": {
                "Other annual cost 1": {
                    "annualCost": 5000.0
                },

                "Other annual cost 2": {
                    "annualCost": 7000.0
                },

                "Other annual cost 3": {
                    "annualCost": 9000.0
                }
            }
        }
    },

    "Net Position Snapshot": {
        "Net Position Snapshot": {

            "liquidityReserve": {
                "items": {
                    "Cash & Immediate Access Buffers": {
                        "currentValue": 250000.0
                    }
                }
            },

            "wealthVelocityAssets": {
                "items": {

                    "Investments (funds, stocks, ETFs)": {
                        "currentValue": 450000.0
                    },

                    "Pension / retirement accounts": {
                        "currentValue": 350000.0
                    },

                    "Property — full market value": {
                        "currentValue": 6500000.0
                    },

                    "Other wealth-building assets": {
                        "currentValue": 100000.0
                    }
                }
            },

            "structuralLiabilities": {
                "items": {

                    "Mortgage": {
                        "currentValue": 3200000.0
                    },

                    "Car loan": {
                        "currentValue": 180000.0
                    },

                    "Student loans": {
                        "currentValue": 90000.0
                    },

                    "Credit cards & short-term debt": {
                        "currentValue": 25000.0
                    },

                    "Other liabilities": {
                        "currentValue": 10000.0
                    }
                }
            }
        }
    },

    "Monthly Activation": {}
}
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