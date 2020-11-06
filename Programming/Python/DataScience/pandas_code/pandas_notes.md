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



### Display settings
```python
import  pandas as pd
# setting how many rows/columsn to show
pd.set_option('display.max_columns', 3)
pd.set_option('display.max_rows', 10)
```

## Reading date/time columns

```python
# convert date time column to date object

# OPTION 1 - using to_datetime
df['script_time'] = pd.to_datetime(df['script_time'])

# OPTION 2 - using formatter string as data is loaded
d_parser = lambda x: pd.datetime.strptime(x, '%Y-%m-%d %I-%p')
df = pd.read_csv('ETH_1h.csv', parse_dates=['Date'], date_parser=d_parser)
```


```python
# get first date tiem
df.loc[0,'script_time']

# get day name
df.loc[0,'script_time'].day_name()

# view day names of entire date column
df['Date'].dt.day_name()

# create a new column to show day names
df['DayofWeek'] = df['Date'].dt.day_name()

# See earliest date
df['Date'].min()

# See recent date
df['Date'].max()

# get time delta; show # of days between 2 dates
df['Date'].max() - df['Date'].min()
```

### Date Filters

```python
# filter by date >= 2020
filt = (df['Date'] >= '2020')
df.loc[filt]

# filter by date >= 2019 and < 2020
filt = (df['Date'] >= '2019') & (df['Date'] < '2020')
df.loc[filt]

# filter by date >= 2019 and < 2020 using datetime func
filt = (df['Date'] >= pd.to_datetime('2019-01-01')) & (df['Date'] < pd.to_datetime('2020-01-01'))
df.loc[filt]

```

### Date slicing

```python
# set index as date
df.set_index('Date', inplace=True)

# get data for 2010
df['2019']

df['2020-01':'2020-02']

# get avg closing price
df['2020-01':'2020-02']['Close'].mean()

# get high for the entire day
df['2020-01-01']['High'].max()

# re-sample to see high values for each day
df['High'].resample('D').max() # D = day ; W = week

# re-sample to see high values for each day
highs = df['High'].resample('D').max()
highs['2020-01-01']

# resample entire df by week
df.resample('W').mean()

# using agg method
df.resample('W').agg({'Close':'mean', 'High':'max', 'Low':'min', 'Volume': 'sum'})

```

### Plot date dfs

```python
%matplotlib inline

# plot the highs
highs.plot()

```


### References
- Datetime Formatting Codes - http://bit.ly/python-dt-fmt
- Pandas Date Offset Codes - http://bit.ly/pandas-dt-fmt
- Video: https://www.youtube.com/watch?v=UFuo7EHI8zc

## Preview data

df.head()
df.tail()


## Code Snippets

```python
# simple read from url csv
import pandas as pd
movies = pd.read_csv('http://bit.ly/imdbratings')
```

###  Indexes
```python
# set index
import pandas as pd 
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")  

df.set_index('myindex', inplace=True)

# show index
df.index

# once index is set you acces items using that index
df.loc[''<index_name>']

# access specific col value for an index
df.loc[''<index_name>', '<colname>']

# you can still access using integer indexes using iloc
df.iloc[0]


# sort by index
df.sort_index(ascending=False)
```

### Sorting
Soure: https://github.com/CoreyMSchafer/code_snippets/blob/master/Python/Pandas/07-Sorting-Data/Snippets.ipynb
```python
people = {
    'first': ['Corey', 'Jane', 'John', 'Adam'], 
    'last': ['Schafer', 'Doe', 'Doe', 'Doe'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', 'A@email.com']
}
:
import pandas as pd
df = pd.DataFrame(people)
df.sort_values(by='last', ascending=False)

df.sort_values(by=['last', 'first'], ascending=False)
df.sort_values(by=['last', 'first'], ascending=[False, True], inplace=True)
df.sort_index()
# sort individual column values 
df['last'].sort_values()

```

## Min and Max Value

````python
# find largest salaries 
df['salary'].nlargest(10)
# get all data for high salaries
df.nlargest(10, 'salary')

# find low salaries 
df['salary'].nsmallest(10)
# get all data for low salaries
df.nsmallest(10, 'salary')
````

### Filter Data
```python
import  pandas as pd
df = pd.read_csv('survey_results_public.csv', index_col='Respondent')
# set filter
high_salary = (df['salary'] > 100000)
#  get all matching filter
df.loc[high_salary]
# get specifics
df.loc[high_salary, ['Country','LanguageWorkedWith']]

# using contry filter
countries = ['US', 'INDIA']
filt = df['Country'].isin(countries)
df.loc[filt, 'Country']

```

### Grouping/Aggregating Data

show values counts
- df['social_media'].value_counts()

show values as % 
- df['social_media'].value_counts(normalize=True)

```python
# set a variable
country_grp = df.groupby(['Country'])
country_grp.get('United States')

filt = df['Country'] == 'India'
df.loc[filt]['SocialMedia'].value_counts()

country_grp['SocialMedia'].value_counts()
country_grp['SocialMedia'].value_counts().loc['United States']

country_grp['Salary'].median()
country_grp['Salary'].median().loc['Germany']
# using agg
country_grp['Salary'].agg(['median','mean']).loc['Cananda']

filt = df['country'] == 'India'
df.loc[filt]["languageworkedwith"].str.contains('Python').sum()

country_grp["languageworkedwith"].apply(lambda x: x.str.contains('Python').sum())
```    


### Add a new column

```python
df['full_name'] = df['first'] + ' ' + df['last']
```

### Delete columns

```python
df.drop(columns=['first','last'], inplace=True)
```

### Split a column value to 2 columns

```python
df['full_name'].str.split('', expand=True)
```

### Unique Value

df['colname'].unique()

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

### Handle Missing Data

- df.dropna()
- default values: ```df.dropna(axis='index', how='any') ```
    - axis of index is for rows
    - axis of columns is for cols
- drop only if all rows are missing: ```df.dropna(axis='index', how='all') ```
- drop only if all columns are missing: ```df.dropna(axis='columns', how='all') ```
- drop only specific columns: ```df.dropna(axis='index', how='all', subset=['last', 'email'])```
- use inplace=True to make permanent

- use replace to replace na values: ```df.replace('NA', "new_value", inplace=True)```

```
df = pd.DataFrame(people)
df.replace('NA', np.nan, inplace=True)
df.replace('Missing', np.nan, inplace=True)
```
```
na_vals = ['NA', 'Missing']
df = pd.read_csv('yourcsv.csv', index_col='age', na_values=na_vals)
```

- find na is df: ```df.isna()```
- fill all missing with text: ```df.fillna('MISSING')```

https://www.youtube.com/watch?v=KdmPHEnPJPs&t=214s

### Read/Write to Different sources

```python

import pandas as pd
df = pd.read_csv('dataset_nba.csv', index_col='Respondent')

# write to csv
df.to_csv('data/modified.csv')

# write to csv with tab separator
df.to_csv('data/modified.csv' , sep='\t')

# write to excel
# install req. libs: pip install xlwt openpyxl xlrd
df.to_excel('data/modified.xlsx')

# write to json
df.to_json('data.json')

# write to json - as records on separate lines
df.to_json('data.json', orient='records', lines=True)

# sql - read postgress db and write
from sqlalchemy import create_engine
import psycopg2
engine = create_engine('postgresql://dbuser:dbpass@localhost:5432/sample_db')
df.to_sql('sample_table', engine, if_exists='replace')
df = pd.read_sql('sample_table', engine, index_col='Respondent')

# read sql
sql_df = pd.read_sql_query('SELECT * FROM sample_table', engine, index_col='Respondent')

# read from url
posts_df = pd.read_json('https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Flask_Blog/snippets/posts.json')
```

https://www.youtube.com/watch?v=N6hyN6BW6ao&list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS&index=11

### Casting Data

- show df types: ```df.dtypes```
- cast data to int: ```df['age'] = df['age'].astype(int)```
- cast data to float: ```df['age'] = df['age'].astype(float)```

## Pandas stat
- df1.hist() - histogram of all columns
- df1.corr() correlation

## Resources
- Tutorial: 
- Code snippets: https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Pandas
