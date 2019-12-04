import os
import sqlite3

print(os.getcwd())

con = sqlite3.connect('data.sqlite3')
print(type(con))
cur = con.cursor()
cur.execute('''CREATE TABLE 
		emp (id integer primary key, 
		fn varchar(20), 
		ln varchar(20))''')

cur.execute('''INSERT INTO emp VALUES(1,'Anish','sebastian')''')

con.commit()

cur.execute('SELECT * FROM emp')
print(cur.fetchall())
cur.execute('''DROP TABLE emp''')

con.close()