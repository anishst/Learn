import xlwt
import cx_Oracle

db = '<connstring>'
connection = cx_Oracle.connect(db)
SQL = "<query"

 #Instantiates a workbook and sheet to write the query results to
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("anish's Sheet") # name of the worksheet

#Database connection
cursor = connection.cursor()
# you must create a Cursor object. It will let
# you execute all the queries you need

# Use all the SQL you like
cursor.execute(SQL)
rowNum = 0 #keep track of rows
colNum = 0 #keep track of columns
# print all the cells of the row to excel sheet
for row in cursor.fetchall() :
	sheet.write(rowNum, colNum, row) # row, column, value
	rowNum = rowNum + 1
	colNum = colNum + 1