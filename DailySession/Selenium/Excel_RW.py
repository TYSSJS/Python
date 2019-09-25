import xlrd
# read from the excel
# to install the read mode
# >>>pip install xlrd

loc="C:\\Users\\Amritha\\PycharmProjects\\PythonProject\\pySelenium\\Book1.xlsx"
wb=xlrd.open_workbook(loc)
sheet1=wb.sheet_by_index(0)
print(sheet1.cell_value(0,0))
print("ROW:",sheet1.nrows)
print("COLUMNS:",sheet1.ncols)

for i in range(sheet1.nrows):
    print(sheet1.cell_value(i,0))

list = []

for i in range(sheet1.ncols):
    l=sheet1.cell_value(0,i)
    list.append(l)
print(list)

print(sheet1.row_values(1))
print(sheet1.row_values(2))



