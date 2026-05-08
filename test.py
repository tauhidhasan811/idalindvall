from openpyxl import load_workbook
from openpyxl.styles import PatternFill, Font

# Load the workbook
file_path = 'Freedom.xlsx'  # Replace with the path to your Excel file
wb = load_workbook(file_path)

# Value to update in B12
new_value = 'New Value'  # Replace with the value you want to set

# Iterate through all sheets in the workbook
for sheet in wb.sheetnames:
    ws = wb[sheet]
    
    # Get the cell B12
    cell = ws['B12']
    
    # Store the individual properties of the original formatting
    original_fill = cell.fill
    original_font = cell.font
    
    # Update the cell value
    cell.value = new_value
    
    # Recreate the fill and font styles by directly passing their properties
    # Re-assign new instances based on the original properties
    cell.fill = PatternFill(start_color=original_fill.start_color, 
                            end_color=original_fill.end_color, 
                            fill_type=original_fill.fill_type)
    cell.font = Font(name=original_font.name, size=original_font.size, 
                     bold=original_font.bold, italic=original_font.italic, 
                     color=original_font.color)

# Save the modified workbook
wb.save('updated_file.xlsx')  # This will save the updated file as a new one

print("Cell values updated successfully!")