# https://towardsdatascience.com/manage-files-and-database-connections-in-python-like-a-pro-73e8fc0b7967

# write data
with open('data.txt', 'w') as myfile:
    myfile.write('Hello from context manager!')

# read data

with open('data.txt', 'r') as myfile:
    data = myfile.read()

print(data)

# ------------------------------------------------------------------------------
#                       Custom context managers - dir chage
# ------------------------------------------------------------------------------
import os
import contextlib
import boto3

s3 = boto3.client('s3', aws_access_key_id='my_aws_access_key',
                  aws_secret_access_key='my_aws_secret_key',
                  region_name='eu-central-1')


@contextlib.contextmanager
def this_directory(path):
    """
    Change the working dir to the path specified. Then, change back to the original one.
    """
    original_workdir = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(original_workdir)


# Usage:
with this_directory(path='../data'):
    file = 'my_s3_file.csv'
    s3.download_file(bucket='s3_bucket', key=file, filename=file)
# ------------------------------------------------------------------------------
#                       Custom context managers - db query
# ------------------------------------------------------------------------------
import os
import contextlib
import mysql.connector

@contextlib.contextmanager
def get_mysql_conn(db):
    """
    Context manager to automatically close DB connection.
    We retrieve credentials from Environment variables
    """
    conn = mysql.connector.connect(host=os.environ.get('MYSQL_HOST'),
                                   user=os.environ.get('MYSQL_USER'),
                                   password=os.environ.get('MYSQL_PWD'),
                                   database=db)
    try:
        yield conn
    finally:
        conn.close()

#    using custom manager
import pandas as pd
from mysql_conn import get_mysql_conn

with get_mysql_conn(db='mytestdb') as conn:
    df = pd.read_sql('SELECT * FROM mytable', conn)