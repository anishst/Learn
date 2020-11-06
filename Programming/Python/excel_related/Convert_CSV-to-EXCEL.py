#http://pandas.pydata.org/pandas-docs/stable/

import pandas as pd
import xlsxwriter

path = 'C:\\Python\\MyScripts\\'
#read the csv into a pandas dataframe
data = pd.read_csv(path + 'DBQuery.csv')    
#setup the writer
writer = pd.ExcelWriter(path + 'output.xlsx', engine='xlsxwriter')
#write the dataframe to an xlsx file
data.to_excel(writer, sheet_name='mysheet', index=False)
writer.save()