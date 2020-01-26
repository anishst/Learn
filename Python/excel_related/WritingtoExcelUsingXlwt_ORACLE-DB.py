import xlwt
import cx_Oracle

db = 'cbaxs01/Shaek400$@10.20.103.116:29085/OTCNIF'
connection = cx_Oracle.connect(db)
#SQL="SELECT * FROM OTCNET.AGENCY_SITE"
#SQL = "SELECT * FROM OTCNET.agency_site"
#SQL = "SELECT * FROM OTCNET.BATCH WHERE BATCH_STATUS_CODE='O' AND ACTIVE_FLG='N'  AND CURR_DOLLAR_AMT = '10'AND CREATED_TS > '12-AUG-13' AND CREATED_LOGONID IN ('batchloader')"
SQL = "SELECT A.*, B.*, C.*, D.* FROM (SELECT COUNT(*) AS CHECKS_SAVED FROM OTCNET.CHECK_PAYMENT WHERE SCANNER_SERIAL_NUM!='batchloader'AND CREATED_TS BETWEEN TO_DATE('01/09/2017 01:00:00 PM', 'MM/DD/YYYY HH:MI:SS PM') AND TO_DATE('01/13/2017 11:59:59 PM', 'MM/DD/YYYY HH:MI:SS PM')) A, /* Number of Deposits SUBMITTED in a given time period */ (SELECT COUNT(*) AS DEPOSITS_CREATED FROM OTCNET.DEPOSIT WHERE DEPOSIT.STATUS_CD in ('SUBMITTED','AWAP') AND CREATED_TS BETWEEN TO_DATE('01/09/2016 01:00:00 PM', 'MM/DD/YYYY HH:MI:SS PM') AND TO_DATE('01/09/2017 11:59:59 PM', 'MM/DD/YYYY HH:MI:SS PM')) B, /* Number of Deposits CONFIRMED in a given time period */ (SELECT COUNT(*) AS DEPOSITS_CONFIRMED FROM OTCNET.DEPOSIT WHERE DEPOSIT.STATUS_CD='CONFIRMED'AND CONFIRMED_TS BETWEEN TO_DATE('01/09/2017 01:00:00 PM', 'MM/DD/YYYY HH:MI:SS PM') AND TO_DATE('01/09/2017 11:59:59 PM', 'MM/DD/YYYY HH:MI:SS PM')) C, /* Number of Batches CLOSED in a given time period */ (SELECT COUNT(*) AS BATCHES_CLOSED FROM OTCNET.BATCH WHERE BATCH_STATUS_CODE = 'X'AND LAST_UPDATE_TS BETWEEN TO_DATE('01/09/2017 01:00:00 PM', 'MM/DD/YYYY HH:MI:SS PM') AND TO_DATE('01/09/2017 11:59:59 PM', 'MM/DD/YYYY HH:MI:SS PM')) D"

 
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