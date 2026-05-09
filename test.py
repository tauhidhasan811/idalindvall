import json
from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Font
from openpyxl.cell import MergedCell

file_path = 'Freedom.xlsx'
wb = load_workbook(file_path)

data = {
  "monthly_income": {
    "primary_income": 79000,
    "secondary_income": 4000,
    "other_income": 0,
    "total_monthly_income": 83000,
    "currency": "USD"
  },
  "structural_allocation": {
    "essentials": {
      "suggested_percentage": 50,
      "your_percentage": 36.45,
      "allocated_amount": 30250,
      "status": "Within recommended range"
    },
    "wealth_building": {
      "suggested_percentage": 20,
      "your_percentage": 6.02,
      "allocated_amount": 5000,
      "status": "Below recommended range"
    },
    "future_buffer": {
      "suggested_percentage": 15,
      "your_percentage": 6.02,
      "allocated_amount": 5000,
      "status": "Below recommended range"
    },
    "guilt_free_living": {
      "suggested_percentage": 15,
      "your_percentage": 0,
      "allocated_amount": 0,
      "status": "Not allocated"
    },
    "total_allocated_percentage": 48.49,
    "structure_status": "Incomplete allocation - review opportunity to increase wealth building and guilt-free living"
  },
  "irregular_expense_provision": {
    "monthly_irregular_provision": 2583.33,
    "included_in": "future_buffer"
  },
  "automation_reminder": {
    "wealth_building_transfer": {
      "amount": 5000,
      "instruction": "Transfer to investment/savings account on payday"
    },
    "future_buffer_transfer": {
      "amount": 5000,
      "instruction": "Transfer to dedicated savings account for irregular expenses on payday"
    },
    "guilt_free_living_transfer": {
      "amount": 0,
      "instruction": "Allocate funds for personal enjoyment and discretionary spending"
    },
    "irregular_provision_transfer": {
      "amount": 2583.33,
      "instruction": "Included in future_buffer transfer - accumulate for annual irregular expenses"
    }
  }
}

cell_map = {
    "B11": data["monthly_income"]["primary_income"],
    "B12": data["monthly_income"]["secondary_income"],
    "B13": data["monthly_income"]["other_income"],
    "B19": data["structural_allocation"]["essentials"]["suggested_percentage"],
    "C19": data["structural_allocation"]["essentials"]["your_percentage"],
    "D19": data["structural_allocation"]["essentials"]["allocated_amount"],
    "B20": data["structural_allocation"]["wealth_building"]["suggested_percentage"],
    "C20": data["structural_allocation"]["wealth_building"]["your_percentage"],
    "D20": data["structural_allocation"]["wealth_building"]["allocated_amount"],
    "E19": data["structural_allocation"]["wealth_building"]["status"],
    "B21": data["structural_allocation"]["future_buffer"]["suggested_percentage"],
    "C21": data["structural_allocation"]["future_buffer"]["your_percentage"],
    "D21": data["structural_allocation"]["future_buffer"]["allocated_amount"],
    "E21": data["structural_allocation"]["future_buffer"]["status"],
    "B22": data["structural_allocation"]["guilt_free_living"]["suggested_percentage"],
    "C22": data["structural_allocation"]["guilt_free_living"]["your_percentage"],
    "D22": data["structural_allocation"]["guilt_free_living"]["allocated_amount"],
    "E22": data["structural_allocation"]["guilt_free_living"]["status"],
    "E24": data["structural_allocation"]["structure_status"],
    "B28": data["irregular_expense_provision"]["monthly_irregular_provision"],
    "B32": data["automation_reminder"]["wealth_building_transfer"]["amount"],
    "C32": data["automation_reminder"]["wealth_building_transfer"]["instruction"],
    "B33": data["automation_reminder"]["future_buffer_transfer"]["amount"],
    "C33": data["automation_reminder"]["future_buffer_transfer"]["instruction"],
    "B34": data["automation_reminder"]["guilt_free_living_transfer"]["amount"],
    "C34": data["automation_reminder"]["guilt_free_living_transfer"]["instruction"],
    "B35": data["automation_reminder"]["irregular_provision_transfer"]["amount"],
    "C35": data["automation_reminder"]["irregular_provision_transfer"]["instruction"],
}

income_cells = {"B11", "B12", "B13", "D19", "D20", "D21", "D22", "B28", "B32", "B33", "B34", "B35"}


def get_top_left_cell(ws, cell_addr):
    """If cell_addr is part of a merged range, return the top-left cell of that range."""
    for merged_range in ws.merged_cells.ranges:
        if cell_addr in merged_range:
            # Return the top-left cell of the merged range
            return ws.cell(row=merged_range.min_row, column=merged_range.min_col)
    return ws[cell_addr]

# Remove the for loop over all sheets, target only "Command Center"
ws = wb["Command Center"]

for cell_addr, value in cell_map.items():
    cell = get_top_left_cell(ws, cell_addr)

    orig_fill = cell.fill
    orig_font = cell.font

    cell.value = value

    cell.fill = PatternFill(
        start_color=orig_fill.start_color,
        end_color=orig_fill.end_color,
        fill_type=orig_fill.fill_type
    )
    cell.font = Font(
        name=orig_font.name, size=orig_font.size,
        bold=orig_font.bold, italic=orig_font.italic,
        color=orig_font.color
    )

    if cell_addr in income_cells:
        cell.number_format = '#,##0 "kr"'

wb.save('updated_file.xlsx')
print("All cells updated successfully!")