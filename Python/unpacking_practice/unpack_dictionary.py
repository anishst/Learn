# example 1:  conn string for mysql db
import pymysql as db
conn_info = {
    'host': '192.168.1.50',
    'port': 3306,
    'user': 'newuser',
    'passwd': 'newpassword',
    'db': 'test_db',
    'read_timeout': 600, # 10 min timeout'
    'unicode_error': 'strict',
    'ssl': False
}

connection = db.Connection(**conn_info)
