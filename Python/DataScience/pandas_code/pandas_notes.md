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

### Casting Data

- show df types: ```df.dtypes```
- cast data to int: ```df['age'] = df['age'].astype(int)```
- cast data to float: ```df['age'] = df['age'].astype(float)```

## Resources
- Tutorial: 
- Code snippets: https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Pandas
