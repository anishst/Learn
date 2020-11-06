import xlsxwriter

sheets = ["query1", "query2", "query3"]
workbook = xlsxwriter.Workbook('myxlsx.xlsx')
for sh in sheets:
   worksheet = workbook.add_worksheet(sh)
   worksheet.write(1,1,"abcd")
workbook.close() # should be outside the for loop