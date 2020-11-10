# Import pandas
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_html.html
import pandas as pd

# Assign spreadsheet filename to `file`
file = 'CIRAQuery.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Load a sheet into a DataFrame by name: df1
df = xl.parse('Sheet1')

# print column names
print(df.columns)
print(df)

# convert to html code
print(df.to_html())

# customize class
print(df.to_html(classes='my_class'))

# mutliple classes
print(df.to_html(classes=['my_class', 'my_other_class']))



