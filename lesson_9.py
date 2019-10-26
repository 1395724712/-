# coding=utf-8
import xlrd

book_2=xlrd.open_workbook("E:\\homework_1\\excel_2.xls")

sheets_2=book_2.sheets()

# print(sheets_2[0].name)
# rows=sheets_2[0].get_rows()
# for i in rows:
#     print(i[0].value)

print(sheets_2[0])