# https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd
import sqlite3 as sl

con = sl.connect('my-test.db')

# create table
with con:
    con.execute("""
        CREATE TABLE USER (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        );
    """)

# insert records
sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
data = [
    (1, 'Alice', 21),
    (2, 'Bob', 22),
    (3, 'Chris', 23)
]
with con:
    con.executemany(sql, data)

# query data
with con:
    data = con.execute("SELECT * FROM USER WHERE age <= 22")
    for row in data:
        print(row)

con.execute('DROP TABLE USER')


