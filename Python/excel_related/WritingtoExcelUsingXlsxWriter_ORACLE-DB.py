#http://xlsxwriter.readthedocs.io/tutorial01.html

import xlsxwriter
import cx_Oracle
from xlsxwriter.workbook import Workbook

connectionString = '<constring>'
SQL = "<query"

connection = cx_Oracle.connect(connectionString)
cursor = connection.cursor()
cursor.execute(SQL)

# Create a workbook and add a worksheet.
workbook = Workbook('outfile.xlsx')
sheet = workbook.add_worksheet()
for r, row in enumerate(cursor.fetchall()):
    for c, col in enumerate(row):
        sheet.write(r, c, col)
workbook.close()