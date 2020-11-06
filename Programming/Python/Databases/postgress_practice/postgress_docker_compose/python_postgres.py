# import the connect library from psycopg2
#https://kb.objectrocket.com/postgresql/python-and-postgresql-docker-container-part-2-1063
from psycopg2 import connect

table_name = "test"

# declare connection instance
conn = connect(
    dbname = "root",
    user = "root",
    host = "192.168.1.35",
    password = "changeme"
)

# declare a cursor object from the connection
cursor = conn.cursor()

# execute an SQL statement using the psycopg2 cursor object
cursor.execute(f"SELECT * FROM {table_name};")

# enumerate() over the PostgreSQL records
for i, record in enumerate(cursor):
    print ("\n", type(record))
    print ( record )

# close the cursor object to avoid memory leaks
cursor.close()

# close the connection as well
conn.close()