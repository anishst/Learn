# http://pandas.pydata.org/pandas-docs/stable/tutorials.html
# https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PandasPythonForDataScience.pdf
# https://www.datacamp.com/community/tutorials/python-excel-tutorial#gs.bf7SWNQ
# http://queirozf.com/entries/pandas-dataframe-by-example

import pandas as pd
import xml.etree.ElementTree as ET
import xlrd, sys,os
import datetime
from lxml import objectify

# print('Python version ' + sys.version)
# print('Pandas version ' + pd.__version__)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#  read csv files
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
df = pd.io.parsers.read_csv("req.csv")
print(df.head(3)) # Select top N number of records (default = 5)
print(df.tail(3)) # Select bottom N number of records (default = 5)

# create output as a list
# reqID = df[['ID-NEW']].values

# print out list items
# print(len(reqID))
# for i in reqID:
# 	print(i)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# reading from text file
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# txtFile = pd.io.parsers.read_table("Test.txt")
# print(txtFile)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# reading from Excel
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#  http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_excel.html
xls = pd.ExcelFile("CIRAQuery.xlsx")
df =  xls.parse('Sheet1', index_col=None)
# df = xls.parse('Sheet1',skiprows=3, skip_footer=2) -skip rows
print(df.head(2))	# get first rows
print(df.tail(1))	#get last items
print(df.columns) # get column names
print(df.dtypes)	# get data types
print(df)	#get all
print(df['IRN'])	# get 1 specific column
print(df[['IRN','RTN']]) # get  more than 1 column

subset = df['IRN']
print(subset.head())
print(df[[1,3]]) # access columns by column numbers

print(type(df))	# finding type

lis = df.values	# covert to list
print(lis[0][0])


# remove rows
# df.drop(df.head(1).index, inplace=True)

#print(test)
# Get unique values from a column
# print(testdf['Module'].unique())

# If you actually want to print the unique values:
# for x in testdf['Module'].unique():
#     print(x)

# print(testdf['Module'].describe())


# Create a groupby object
# testGroupBy = testdf.groupby('RTN')
# print(testGroupBy)

# Apply the sum function to the groupby object
# df = testGroupBy.sum()
# # print(df)
# for i in df:
# 	print(i)


# convert to a list
# print(testdf['ID'].values)

# apply a filter
# mask = testdf['In Scope System Testing'] == 'Yes'
# testdf = testdf[mask]
# testdf['NewCol'] = datetime.datetime.now()
# print(testdf['ID'])
# print(testdf.duplicated()) #Identify which observations are duplicates #http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.duplicated.html
# testdf = testdf.drop_duplicates() #Drop duplicates  drop_duplicates(['ID'])

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#  EXPORT options 
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# testdf.to_csv("pand_export.csv", index=False)		#CSV  http://pandas.pydata.org/pandas-docs/version/0.15.1/generated/pandas.DataFrame.to_csv.html
# testdf.to_excel("panda_export.xlsx", columns=['ID','Name','NewCol'], index=False) 	#Excel   http://pandas.pydata.org/pandas-docs/version/0.15.1/generated/pandas.DataFrame.to_excel.html
# testdf.to_csv("panda_export.txt", index=False)	#TEXT

#Open excel
# os.system('start excel.exe "%s\\panda_export.xlsx"' % (sys.path[0], ))

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# read from XML and convert to Data Frame
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# Method 1 - any xml file will work 
# http://www.austintaylor.io/lxml/python/pandas/xml/dataframe/2016/07/08/convert-xml-to-pandas-dataframe/
# xml_data = 'XMLData.xml'
# def xml2df(xml_data):
#     tree = ET.parse(xml_data)
#     root = tree.getroot()
#     all_records = []
#     headers = []
#     for i, child in enumerate(root):
#         record = []
#         for subchild in child:
#             record.append(subchild.text)
#             if subchild.tag not in headers:
#                 headers.append(subchild.tag)
#         all_records.append(record)
#     return pd.DataFrame(all_records, columns=headers)
# print(xml2df(xml_data))

# Method 2 - need to adjust for source
# http://timhomelab.blogspot.com/2014/01/how-to-read-xml-file-into-dataframe.html
# path = 'XMLData.xml'
# xml = objectify.parse(open(path))
# root = xml.getroot()
# root.getchildren()[0].getchildren()
# df = pd.DataFrame(columns=('id', 'name'))

# for i in range(0,4):
#     obj = root.getchildren()[i].getchildren()
#     row = dict(zip(['id', 'name'], [obj[0].text, obj[1].text]))
#     row_s = pd.Series(row)
#     row_s.name = i
#     df = df.append(row_s)

# print(df)