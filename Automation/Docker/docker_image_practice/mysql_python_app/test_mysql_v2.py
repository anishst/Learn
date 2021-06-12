import pymysql as db

conn_info = {
    'host': '192.168.1.50',
    'port': 3306,
    'user': 'newuser',
    'passwd': 'newpassword',
    'db': 'test_db'
}

# HOST = '192.168.1.50'
# PORT = 3306
# USER = "newuser"
# PASSWORD = 'newpassword'
# DB = "test_db"

try:
    # connection = db.Connection(host=HOST, port=PORT,user=USER,
    # passwd=PASSWORD, db=DB)

    # use dict unpacking
    connection = db.Connection(**conn_info)

    dbhandler = connection.cursor()
    dbhandler.execute("SELECT * from UserVitals")
    result = dbhandler.fetchall()
    for item in result:
        print (item)
except Exception as e:
    print(e)
finally:
    connection.close()