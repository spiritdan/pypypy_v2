import openpyxl
wb = openpyxl.load_workbook('Marvel.xlsx')
sheet=wb['漫威宇宙']
sheetname = wb.sheetnames
print(sheetname)
A1_cell=sheet['A1']
A1_value=A1_cell.value
print(A1_value)