import  r_excel
file_name = r_excel.excel('用例模板.xlsx')
# q = e.getRowsClosNum()
# q = e.setCellValue(1,10,'dccdcf')
column_3 = file_name.getColValues(3)
column_4 = file_name.getColValues(4)
column_5 = file_name.getColValues(5)

print(column_3,'\n',column_4,'\n',column_5)