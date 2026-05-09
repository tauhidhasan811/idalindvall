budget_prompt_temp = {
    "Command Center": {
        "monthly_income": {
            "primary_income": "float",
            "secondary_income": "float",
            "other_income": "float",
        },

        "structural_allocation": {
            "essentials": {
                "suggested_percentage": "integer_percentage",
                "your_percentage": "decimal_float",
                "allocated_amount": "float",
                "status": "string"
            },

            "wealth_building": {
                "suggested_percentage": "integer_percentage",
                "your_percentage": "decimal_float",
                "allocated_amount": "float",
                "status": "string"
            },

            "future_buffer": {
                "suggested_percentage": "integer_percentage",
                "your_percentage": "decimal_float",
                "allocated_amount": "float",
                "status": "string"
            },

            "guilt_free_living": {
                "suggested_percentage": "integer_percentage",
                "your_percentage": "decimal_float",
                "allocated_amount": "float",
                "status": "string"
            },

            "total_allocated_percentage": "decimal_float",
            "structure_status": "string"
        },

        "irregular_expense_provision": {
            "monthly_irregular_provision": "float",
            "included_in": "string"
        },

        "automation_reminder": {
            "wealth_building_transfer": {
                "amount": "float",
                "instruction": "string"
            },

            "future_buffer_transfer": {
                "amount": "float",
                "instruction": "string"
            },

            "guilt_free_living_transfer": {
                "amount": "float",
                "instruction": "string"
            },

            "irregular_provision_transfer": {
                "amount": "float",
                "instruction": "string"
            }
        }
    },

    "Irregular Expense System": {

        "home_and_property": [
            {
                "expense": "string",
                "annual_cost": "float",
                "monthly_provision": "float",
                "notes": "string",
                "category": "string"
            }
        ],

        "transport": [
            {
                "expense": "string",
                "annual_cost": "float",
                "monthly_provision": "float",
                "notes": "string",
                "category": "string"
            }
        ],

        "family_and_children": [
            {
                "expense": "string",
                "annual_cost": "float",
                "monthly_provision": "float",
                "notes": "string",
                "category": "string"
            }
        ],

        "lifestyle": [
            {
                "expense": "string",
                "annual_cost": "float",
                "monthly_provision": "float",
                "notes": "string",
                "category": "string"
            }
        ],

        "health_and_wellbeing": [
            {
                "expense": "string",
                "annual_cost": "float",
                "monthly_provision": "float",
                "notes": "string",
                "category": "string"
            }
        ],

        "other": [
            {
                "expense": "string",
                "annual_cost": "float",
                "monthly_provision": "float",
                "notes": "string",
                "category": "string"
            }
        ],

        "totals": {
            "total_annual_irregular_costs": "float",
            "total_monthly_provision": "float",
            "feeds_into": "string"
        },

        "surprise_elimination_score": {
            "monthly_provision_running": {
                "amount": "float",
                "status": "string"
            },

            "annual_costs_fully_covered": {
                "value": "boolean",
                "status": "string"
            },

            "months_of_expenses_provisioned": {
                "months": "integer",
                "target": "integer",
                "status": "string"
            }
        }
    },


    "Net Position Snapshot": {

        "liquidity_reserve": {
            "cash_and_immediate_access_buffers": {
                "current_value": "float",
                "target_status": "string",
                "standard": "string"
            }
        },

        "wealth_velocity_assets": {
            "investments": "float",
            "pension_retirement_accounts": "float",
            "property_market_value": "float",
            "other_wealth_building_assets": "float",

            "total_wealth_velocity": {
                "amount": "float",
                "status": "string"
            }
        },

        "structural_liabilities": {
            "mortgage": {
                "amount": "float",
                "notes": "string"
            },

            "car_loan": {
                "amount": "float",
                "notes": "string"
            },

            "student_loans": {
                "amount": "float",
                "notes": "string"
            },

            "credit_cards_and_short_term_debt": {
                "amount": "float",
                "notes": "string"
            },

            "other_liabilities": {
                "amount": "float",
                "notes": "string"
            },

            "total_structural_liabilities": {
                "amount": "float",
                "status": "string"
            }
        },

        "property_equity": {
            "property_market_value": "float",
            "outstanding_mortgage": "float",

            "true_property_equity": {
                "amount": "float",
                "formula": "property_market_value - outstanding_mortgage"
            }
        },

        "net_structural_position": {
            "amount": "float",
            "status": "string",
            "guidance": "string"
        },

        "structural_benchmarks": {

            "liquidity_reserve_percentage": {
                "value": "decimal_float",
                "target": "string"
            },

            "investments_and_pension_percentage": {
                "value": "decimal_float",
                "target": "string"
            },

            "property_equity_percentage": {
                "value": "decimal_float",
                "description": "string"
            },

            "loan_to_value_mortgage": {
                "value": "decimal_float",
                "target": "string"
            },

            "consumer_debt_ratio": {
                "value": "decimal_float",
                "target": "string"
            }
        }
    },
    "Monthly Activation": {

        "this_month": {
            "month": "string",
            "income_this_month_after_tax": "float",
            "structural_changes_this_month": "string"
        },

        "net_position_this_month": {
            "system_status": {
                "status": "string",
                "guidance": "string"
            }
        },

        "monthly_activation_checklist": [
            {
                "task": "string",
                "completed": "boolean",
                "notes": "string",
                "category": "string"
            }
        ],

        "next_steps": {
            "next_review_date": "string",
            "primary_structural_focus_this_month": "string",
            "notes": "string"
        },

        "system_message": "string"
    }
}