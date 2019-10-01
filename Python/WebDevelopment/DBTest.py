#!C:/Python/python
print("Content-type: text/html")
import sqlite3

conn = sqlite3.connect('otcnet.db')

def Test():
	print("test")
	return ""

print("")
print("<html><head>")
print("")
print("</head><body>")
print("Opened database successfully")

print("<BR/>DB Records:<br />")
cursor = conn.execute("SELECT *  from log")
for row in cursor:
   print ("ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])
   print ("<br/>")

print ( "Operation done successfully")
print(Test())
print("</body></html>")