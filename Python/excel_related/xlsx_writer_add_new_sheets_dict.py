import xlsxwriter

sql_queries = {

   'query1': 'sql query1',
   'query2': 'sql quer2'
}
workbook = xlsxwriter.Workbook('myxlsx.xlsx')
for queryname, sql in sql_queries.items():
   worksheet = workbook.add_worksheet(queryname)
   worksheet.write(0,0,queryname)
   worksheet.write(0, 1, sql)
workbook.close() # should be outside the for loop