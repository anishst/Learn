import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")


def CreateTable():

	conn.execute('''CREATE TABLE COMPANY
	       (ID    NOT NULL,
	       NAME           TEXT    NOT NULL,
	       AGE            INT     NOT NULL,
	       ADDRESS        CHAR(50),
	       SALARY         REAL);''')
	print ("Table created successfully")

def dataCreation():
	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")
	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)  VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");	
	conn.commit()

	print("Records created successfully")


def searchDB():
	cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
	for row in cursor:
	   print ("ID = ", row[0])
	   print ("NAME = ", row[1])
	   print ("ADDRESS = ", row[2])
	   print ("SALARY = ", row[3], "\n")

	print ( "Operation done successfully")

def DeleteRecords():
	conn.execute("DELETE from COMPANY")
	# conn.execute("DELETE from COMPANY where ID=2;")
	conn.commit()
	print("Total number of rows deleted :", conn.total_changes)

def DropTable():
	conn.execute("DROP TABLE COMPANY")
	print("Table dropped")

CreateTable()
dataCreation()
searchDB()
DeleteRecords()
DropTable()

conn.close()
