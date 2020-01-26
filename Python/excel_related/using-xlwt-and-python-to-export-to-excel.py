# 12/7/2009 - Ryan Robitaille [ryrobes.com]
# http://ryrobes.com/featured-articles/using-xlwt-and-python-to-export-an-oracle-dataset-to-excel-python-simple-etl-part-2/

import cx_Oracle, time, string
from xlwt import *  #formerly "pyExcelerator"


# set oracle login variables
OraUid="scott"          	#Oracle User  
OraPwd="tiger"       		#Oracle password
OraService="TNS_EETFUK"      	#Oracle Service name From Tnsnames.ora file

# do a timestamp for being able to track execution time (if you want)
startscript = time.time()  # we will use this later
 
db = cx_Oracle.connect(OraUid + "/" + OraPwd + "@" + OraService)   #Connect to database
dev_cursor_select = db.cursor()                                    #Allocate a cursor

dev_cursor_select.execute("""SELECT DBMS_RANDOM.STRING('P',40) field1, 
		DBMS_RANDOM.STRING('X',30) field2, ROUND(DBMS_RANDOM.VALUE(1000, 9999)) field3, 
		DBMS_RANDOM.STRING('A',20) field4  FROM DUAL CONNECT BY LEVEL<=3000""")
# 3,000 rows of random garbage seems good

result_set = dev_cursor_select.fetchall()


# Start some Excel magic
wb = Workbook()
ws0 = wb.add_sheet('My New Worksheet')

# Grey background for the header row
BkgPat = Pattern()
BkgPat.pattern = Pattern.SOLID_PATTERN
BkgPat.pattern_fore_colour = 22

# Bold Fonts for the header row
font = Font()
font.name = 'Calibri'
font.bold = True

# Non-Bold fonts for the body
font0 = Font()
font0.name = 'Calibri'
font0.bold = False

# style and write field labels
style = XFStyle()
style.font = font
style.pattern = BkgPat

style0 = XFStyle()
style0.font = font0


col_width_dict = dict() # create a dictionary var

for i in range(4): # fill it up with 0s first so Python doesn't complain
	col_width_dict[i] = 0

row_number=1

for row in result_set:
	column_num=0
	for item in row:
		ws0.write(row_number,column_num,str(item),style0)
		# write the excel row from the cursor - starting at row 1 (literal row 2)
		if len(str(item)) > col_width_dict[column_num]:
			# only redefine the column width if we need it to be bigger
			col_width_dict[column_num] = len(str(item))
		ws0.col(column_num).width = len(str(item))*256
		# set the width of the column depending on incoming string
		column_num=column_num+1

	row_number=row_number+1


ws0.write(0,0,'Field 1',style)
ws0.write(0,1,'Field 2',style)
ws0.write(0,2,'Field 3',style)
ws0.write(0,3,'Field 4',style)

wb.save('sample_output.xls')

endscript = time.time()
endtime = endscript - startscript
print 'script run in ' + str(endscript - startscript) + ' seconds or ' + str((endscript - startscript)/60) + ' minutes'

# Peace!