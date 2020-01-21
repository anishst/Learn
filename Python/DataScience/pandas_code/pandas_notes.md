# Pandas


|Command | Description |
|--------|-------------|
| ```df.head()```| shows first values|
| ```df.dtypes```| shows data types|
| ```df.values.tolist()``` | convert df to list|
| ```df['Transaction Date']=pd.to_datetime(df['Transaction Date'])``` | convert date col into dattime type|
|```df['col'].sum()```| print sum of a column|
|```df.loc[df['col'].str.contains('text'), 'Transaction Amount'].sum()```| sum based on value of another column|
|```df[df['col'].str.contains('text')].sum()```| sum based on value of another column|
|```df.groupby(df['Transaction Date'].dt.strftime('%B'))['Transaction Amount'].sum().sort_values()```| group by month|




## Code Snippets


### Filter Data
```python
import  pandas as pd

people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}
```

### Drop duplicates

```python
# http://pandas.pydata.org/pandas-docs/stable/tutorials.html
import pandas as pd
import os, sys
#  read file
xls = pd.ExcelFile(r"duplicates.xlsx")
df =  xls.parse('Sheet1', columns=['IRN','BATCHID','ACCOUNT_NUMBER', 'RTN'],index_col=None)
# Remove dupes
df  = df.drop_duplicates() #Drop duplicates  drop_duplicates(['ID'])
#  save to new file
df.to_excel("duplicates_removed.xlsx", columns=['IRN','BATCHID','ACCOUNT_NUMBER', 'RTN'], index=False) 
#Open excel
os.system('start excel.exe "%s\\duplicates_removed.xlsx"' % (sys.path[0], ))

```
### Concat example

```python
import  pandas as pd
csv_file = 'prices1.csv'
df = pd.read_csv(csv_file)
csv_file2 = 'prices2.csv'
df2 = pd.read_csv(csv_file2)
all_prices = pd.concat([df,df2])
```

## Resources
- Tutorial: 
- Code snippets: https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Pandas
