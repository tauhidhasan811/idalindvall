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

###Irregular Expense System


  "Irregular Expense System": {
    "categories": {
      "Home & Property": {
        "Home insurance (annual)": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Home & Property"
        },
        "Home maintenance & repairs": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Home & Property"
        },
        "Appliance replacement fund": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Home & Property"
        }
      },

      "Transport": {
        "Car insurance (annual)": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Transport"
        },
        "Car service / MOT": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Transport"
        },
        "Road tax": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Transport"
        },
        "Tyres & maintenance": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Transport"
        }
      },

      "Family": {
        "School fees / activities": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Family"
        },
        "Children's clothing & equipment": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Family"
        },
        "Birthday & Christmas gifts": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Family"
        }
      },

      "Lifestyle": {
        "Holidays & travel": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Lifestyle"
        },
        "Clothing & seasonal wardrobe": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Lifestyle"
        },
        "Annual memberships": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Lifestyle"
        }
      },

      "Health": {
        "Dental / medical (annual)": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Health"
        },
        "Glasses / contacts": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Health"
        },
        "Other health costs": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Health"
        }
      },

      "Other": {
        "Other annual cost 1": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Other"
        },
        "Other annual cost 2": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Other"
        },
        "Other annual cost 3": {
          "annualCost": 0.0,
          "monthlyProvision": 0.0,
          "notes": "",
          "category": "Other"
        }
      }
    },

    "totals": {
      "totalAnnualIrregularCosts": 0.0,
      "totalMonthlyProvision": 0.0,
      "currency": "",
      "note": "This feeds into your Command Center automatically"
    },

    "surpriseEliminationScore": {
      "label": "How well is your structure engineering out financial volatility?",
      "monthlyProvisionRunning": 0.0,
      "annualCostsCovered": False,
      "coverageStatus": "",
      "monthsOfExpensesProvisioned": 0.0,
      "target": 0.0,
      "targetStatus": ""
    }
  },






###  Net Position Snapshot

    
  "Net Position Snapshot": {
    "liquidityReserve": {
      "label": "Cash & immediately accessible funds. Your Shock Absorber.",
      "target": "5–10% of total assets",
      "items": {
        "Cash & Immediate Access Buffers": {
          "currentValue": 0.0,
          "targetStatus": ""
        }
      },
      "total": 0.0
    },
    "wealthVelocityAssets": {
      "label": "Investments, pension, and property. Enter full property market value — equity is calculated automatically below.",
      "items": {
        "Investments (funds, stocks, ETFs)": {
          "currentValue": 0.0
        },
        "Pension / retirement accounts": {
          "currentValue": 0.0
        },
        "Property — full market value": {
          "currentValue": 0.0,
          "notes": "Enter full market value. Equity calculated below."
        },
        "Other wealth-building assets": {
          "currentValue": 0.0
        }
      },
      "total": 0.0,
      "targetStatus": ""
    },
    "structuralLiabilities": {
      "label": "Enter as positive numbers. Mortgage is used to calculate true property equity automatically.",
      "items": {
        "Mortgage": {
          "currentValue": 0.0,
          "notes": "Outstanding mortgage balance"
        },
        "Car loan": {
          "currentValue": 0.0
        },
        "Student loans": {
          "currentValue": 0.0
        },
        "Credit cards & short-term debt": {
          "currentValue": 0.0
        },
        "Other liabilities": {
          "currentValue": 0.0
        }
      },
      "total": 0.0,
      "targetStatus": ""
    },
    "propertyEquity": {
      "label": "Your true ownership stake in your property. Calculated from the values entered above.",
      "propertyMarketValue": 0.0,
      "outstandingMortgage": 0.0,
      "truePropertyEquity": 0.0,
      "notes": "Property value minus mortgage"
    },
    "netStructuralPosition": {
      "value": 0.0,
      "status": "",
      "notes": "If SYSTEM STABLE — return to your life.",
      "currency": ""
    },
    "structuralBenchmarks": {
      "label": "All percentages calculated against total assets — stable and meaningful regardless of liability level.",
      "items": {
        "Liquidity Reserve %": {
          "value": 0.0,
          "target": "5–10% of total assets"
        },
        "Investments & Pension %": {
          "value": 0.0,
          "target": "growing year on year"
        },
        "Property Equity %": {
          "value": 0.0,
          "target": "Your ownership share"
        },
        "Loan-to-Value (mortgage)": {
          "value": 0.0,
          "target": "<80% — under 70% is strong"
        },
        "Consumer Debt Ratio": {
          "value": 0.0,
          "target": "<5% of total assets"
        }
      }
    }
  }
,





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
    },



  "Monthly Activation": {
    "This Month": {
      "overview": {
        "month": "",
        "incomeThisMonth": 0.0,
        "structuralChanges": "",
        "notes": {
          "income": "Update in Command Center if different",
          "structuralChanges": "New job, pay rise, new expenses — note here"
        }
      },
      "netPositionThisMonth": {
        "systemStatus": "",
        "statusNote": "If SYSTEM STABLE — complete checklist and return to your life."
      },
      "monthlyActivationChecklist": {
        "label": "Tick each item. When all are done, the system is running for another month.",
        "items": {
          "income": {
            "task": "Review income — confirm this month's inflow",
            "notes": "Update Command Center if changed",
            "category": "Income",
            "completed": False
          },
          "wealthBuilding": {
            "task": "Confirm Wealth Building transfer executed",
            "notes": "Consistency is non-negotiable",
            "category": "Wealth Building",
            "completed": False
          },
          "futureBuffer": {
            "task": "Confirm Future Buffer transfer executed",
            "notes": "Stability is built deliberately",
            "category": "Future Buffer",
            "completed": False
          },
          "guiltFree": {
            "task": "Confirm Guilt-Free transfer to spending account",
            "notes": "Non-negotiable. You've earned this.",
            "category": "Guilt-Free",
            "completed": False
          },
          "irregular": {
            "task": "Confirm irregular provision running",
            "notes": "Check Irregular Expense System tab",
            "category": "Irregular",
            "completed": False
          },
          "netPosition": {
            "task": "Review Net Position Snapshot",
            "notes": "Update balances if needed",
            "category": "Net Position",
            "completed": False
          },
          "mindset": {
            "task": "Revisit Financial Power Declaration",
            "notes": "From your installation workbook",
            "category": "Mindset",
            "completed": False
          },
          "activation": {
            "task": "Set next review date",
            "notes": "Same time next month",
            "category": "Activation",
            "completed": False
          }
        },
        "allCompleted": False
      },
      "nextSteps": {
        "nextReviewDate": "",
        "primaryStructuralFocus": "",
        "notes": "",
        "hints": {
          "nextReviewDate": "Set it now so you don't have to remember",
          "primaryStructuralFocus": "One thing. Not five."
        }
      }
    }
  }

}