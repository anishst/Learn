# https://pythontic.com/pandas/serialization/mysql
from sqlalchemy import create_engine
import pymysql

import pandas as pd

userVitals = {"UserId": ["xxxxx", "yyyyy", "zzzzz", "aaaaa", "bbbbb", "ccccc", "ddddd"],

              "UserFavourite": ["Greek Salad", "Philly Cheese Steak", "Turkey Burger", "Crispy Orange Chicken",
                                "Atlantic Salmon", "Pot roast", "Banana split"],

              "MonthlyOrderFrequency": [5, 1, 2, 2, 7, 6, 1],

              "HighestOrderAmount": [30, 20, 16, 23, 20, 26, 9],

              "LastOrderAmount": [21, 20, 4, 11, 7, 7, 7],

              "LastOrderRating": [3, 3, 3, 2, 3, 2, 4],

              "AverageOrderRating": [3, 4, 2, 1, 3, 4, 3],

              "OrderMode": ["Web", "App", "App", "App", "Web", "Web", "App"],

              "InMedicalCare": ["No", "No", "No", "No", "Yes", "No", "No"]};

tableName = "UserVitals"

config = {
    'host': '192.168.1.50',
    'port': 3306,
    'user': 'newuser',
    'password': 'newpassword',
    'database': 'test_db'
}
db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')
dataFrame = pd.DataFrame(data=userVitals)
connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
sqlEngine = create_engine(connection_str, pool_recycle=3600)

dbConnection = sqlEngine.connect()

try:

    frame = dataFrame.to_sql(tableName, dbConnection, if_exists='replace');

except ValueError as vx:

    print(vx)

except Exception as ex:

    print(ex)

else:

    print("Table %s created successfully." % tableName);

finally:
    # dbConnection.execute("DROP TABLE UserVitals")
    dbConnection.close()