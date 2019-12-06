import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")


import sqlite3, os

print(os.getcwd())
conn = sqlite3.connect('test.sqlite')
cur = conn.cursor()
print(cur.execute('''select * from Posts'''))
print (cur.fetchone())

items = cur.fetchall()
for item in items:
    print(item)

