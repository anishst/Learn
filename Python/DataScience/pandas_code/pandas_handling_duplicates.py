# http://pandas.pydata.org/pandas-docs/stable/tutorials.html
import pandas as pd
import os, sys


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# reading from Excel
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#  http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_excel.html
xls = pd.ExcelFile(r"CIRAQuery.xlsx")
df =  xls.parse('Sheet1', columns=['BATCHID','IRN'],index_col=None)
print(df.head())
print(df['BATCHID'].describe())

# print(testdf.duplicated()) #Identify which observations are duplicates #http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.duplicated.html
testdf = df.drop_duplicates() #Drop duplicates  drop_duplicates(['ID'])
print(df.duplicated())
print(testdf)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#  EXPORT options 
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# df.to_excel("TestSetValidation.xlsx", columns=['ID','Manual Test Script'], index=False) 	#Excel   http://pandas.pydata.org/pandas-docs/version/0.15.1/generated/pandas.DataFrame.to_excel.html
#Open excel
os.system('start excel.exe "%s\\CIRAQuery.xlsx"' % (sys.path[0], ))

