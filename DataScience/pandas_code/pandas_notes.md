# Pandas


[Matplotlib](#matplot)

## Display settings
```python
import  pandas as pd
# setting how many rows/columsn to show
pd.set_option('display.max_columns', 3)
pd.set_option('display.max_rows', 10)
```

## Commands
|Command | Description |
|--------|-------------|
| ```df.head()```| shows first values|
|```df.count()```|counts rows|
|```df.fillna(0)```|Replace null values| 
| ```df.dtypes```| shows data types|
| ```df.values.tolist()``` | convert df to list|
| ```df['Transaction Date']=pd.to_datetime(df['Transaction Date'])``` | convert date col into dattime type|
|```df['col'].sum()```| print sum of a column|
|```df.loc[df['col'].str.contains('text'), 'Transaction Amount'].sum()```| sum based on value of another column|
|```df[df['col'].str.contains('text')].sum()```| sum based on value of another column|
| **Group By**||
|```df.groupby(['column1', 'column2']).sum()```|get sum|
|```df.groupby(['column1', 'column2']).count()```|get count|
|```df.groupby(df['Transaction Date'].dt.strftime('%B'))['Transaction Amount'].sum().sort_values()```| group by month|
| **Data Slicing**||
|df[-1:]|get last row|
|df.iloc[-1]|get last row using iloc|
| df.iloc[0:10] | slice first 10 rows|
|df.loc["USA", "India"]| slice of rows  USA and India|
|df.loc["USA", "India"]["1929","1980"]| get subset values|
| **Data Filtering**||
|```df[df['column_name'] == 0]```|Filtering a particular column based on a particular value or string|
| df.filter(items=["1990"])| only column 1990|
| df[df.filter(items=["1990"] < 10)]| only column 1990 population density < 10 |
| df.filter(like="8", axis=1)| Years containing an 8|
| df.filter(regex="a$", axis=0)| countries ending with a|
| **Data Sorting**||
| df.sort_values(by=["1990"])| sort by   1990|
|```df.drop_duplicates()```| drop duplicates|
|```df.join(lookup_dataframe, on='column_name')```|join your main dataframe df with another dataframe, we’ll call this lookup_dataframe on the column 'column_name' which appears in both df and lookup_dataframe. The join method has the default parameter how='left'|
| **Plotting**||
|```data['Gender'].value_counts().plot.pie()```| plot pie char of gender|
|```data['Neighbourhood'].value_counts(sort=True).nlargest(10).plot.bar()```|bar chart|


## Basic operations

### iterate data frame
```python
for index, row in df.iterrows():
    print(index, row)
```

### Reading date/time columns

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

## Filter Data


### using loc
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

<a name="#matplot"></a>
## Matplotlib

Plotting library

https://matplotlib.org/

**pyplot** is an interface which allows users to create visualizations to plot the data without explicitly configuring the Figure and Axes. They are implicitly and automatically configured to achieve the desired output

https://matplotlib.org/3.3.2/api/_as_gen/matplotlib.pyplot.plot.html

**plt.figure()** is used to create a new Figure, which returns a Figure instance but it is also passed to the backend.

## Plot Examples

### simple plot

```python
plt.plot([1, 2, 4, 5], [1, 3, 4, 3], '-o')
plt.show()
```
 
### stock data

data sample format

```csv
date,open,high,low,close,volume,Name
2013-02-08,390.4551,393.7283,390.1698,393.0777,6031199,GOOGL
2013-02-11,389.5892,391.8915,387.2619,391.6012,4330781,GOOGL
2013-02-12,391.2659,394.344,390.0747,390.7403,3714176,GOOGL
```

```python

# Import statements
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

%matplotlib inline

# load datasets
google = pd.read_csv('./data/GOOGL_data.csv')
facebook = pd.read_csv('./data/FB_data.csv')
apple = pd.read_csv('./data/AAPL_data.csv')
amazon = pd.read_csv('./data/AMZN_data.csv')
microsoft = pd.read_csv('./data/MSFT_data.csv')

# Create figure
plt.figure(figsize=(16, 8), dpi=300)
# Plot data
plt.plot('date', 'close', data=google, label='Google')
plt.plot('date', 'close', data=facebook, label='Facebook')
plt.plot('date', 'close', data=apple, label='Apple')
plt.plot('date', 'close', data=amazon, label='Amazon')
plt.plot('date', 'close', data=microsoft, label='Microsoft')
# Specify ticks for x- and y-axis
plt.xticks(np.arange(0, 1260, 40), rotation=70)
plt.yticks(np.arange(0, 1450, 100))
# Add title and label for y-axis
plt.title('Stock trend', fontsize=16)
plt.ylabel('Closing price in $', fontsize=14)
# Add grid
plt.grid()
# Add legend
plt.legend()
# Show plot
plt.show()
```

### Movie ratings

Data
```csv
,MovieTitle,Tomatometer,AudienceScore
0,The Shape of Water,91,73
1,Black Panther,97,79
2,Dunkirk,92,81
3,The Martian,91,91
4,The Hobbit: An Unexpected Journey,64,83
```
Plot
```python
# Create figure
plt.figure(figsize=(10, 5), dpi=300)
# Create bar plot
pos = np.arange(len(movie_scores['MovieTitle']))
width = 0.3
plt.bar(pos - width / 2, movie_scores['Tomatometer'], width, label='Tomatometer')
plt.bar(pos + width / 2, movie_scores['AudienceScore'], width, label='Audience Score')
# Specify ticks
plt.xticks(pos, rotation=10)
plt.yticks(np.arange(0, 101, 20))
# Get current Axes for setting tick labels and horizontal grid
ax = plt.gca()
# Set tick labels
ax.set_xticklabels(movie_scores['MovieTitle'])
ax.set_yticklabels(['0%', '20%', '40%', '60%', '80%', '100%'])
# Add minor ticks for y-axis in the interval of 5
ax.set_yticks(np.arange(0, 100, 5), minor=True)
# Add major horizontal grid with solid lines
ax.yaxis.grid(which='major')
# Add minor horizontal grid with dashed lines
ax.yaxis.grid(which='minor', linestyle='--')
# Add title
plt.title('Movie comparison')
# Add legend
plt.legend()
# Show plot
plt.show()
```
- plot multiple data pairs : ```plt.plot([2, 4, 6, 8], 'o', [1, 5, 9, 13], 's')```
- pandas df: ```plt.plot('x_key', 'y_key', data=df)```
- show supported formats: ```plt.gcf().canvas.get_supported_filetypes()```

## Types of Charts

### Bar
- plt.bar(x, height, [width]) creates a vertical bar plot
    - x - x cordinates
    - ex. ```plt.bar(['A','B', 'C'], [10, 30,23], color='green')```
    - ex. ```plt.bar(['A','B', 'C'], [10, 30,23], color=['green', 'blue', 'red'])```
    - control width between ```plt.bar(['A','B', 'C'], [10, 30,23], color=['green', 'blue', 'red'], width=.5)```
    - alpha ```plt.bar(['A','B', 'C'], [10, 30,23], color=['green', 'blue', 'red'], alpha=.7)```
    
- plt.barh() creates a horizontal bars plot

### Pie Chart
- plt.pie(x, [explode], [labels], [autopct]) 

data
```csv
,Usage,Percentage
0,Leak,12
1,Clothes Washer,17
2,Faucet,19
3,Shower,20
4,Toilet,24
5,Other,8

```
plot
```python
data = pd.read_csv('./data/water_usage.csv')
# Create figure
plt.figure(figsize=(8, 8), dpi=300)
# Create pie plot
plt.pie('Percentage', explode=(0, 0, 0.1, 0, 0, 0), labels='Usage', data=data, autopct='%.0f%%')
# Add title
plt.title('Water usage')
# Show plot
plt.show()
```

### Stacked Area Chart

- plt.stackplot(x, y) creates a stacked area plot.

data
```csv
,Quarter,Apple,Samsung,Huawei,Xiaomi,OPPO
0,3Q16,43001,71734,32490,14926,24591
1,4Q16,77039,76783,40804,15751,26705
2,1Q17,51993,78776,34181,12707,30922
3,2Q17,44315,82855,35964,21179,26093
4,3Q17,45442,85605,36502,26853,29449
5,4Q17,73175,74027,43887,28188,25660
6,1Q18,54059,78565,40426,28498,28173
7,2Q18,44715,72336,49847,32826,28511

```
plot
```python
sales = pd.read_csv('./data/smartphone_sales.csv')
# Create figure
plt.figure(figsize=(10, 6), dpi=300)
# Create stacked area chart
labels = sales.columns[1:]
plt.stackplot('Quarter', 'Apple', 'Samsung', 'Huawei', 'Xiaomi', 'OPPO', data=sales, labels=labels)
# Add legend
plt.legend()
# Add labels and title
plt.xlabel('Quarters')
plt.ylabel('Sales units in thousands')
plt.title('Smartphone sales units')
# Show plot
plt.show()
```
### Histogram

plt.hist(x) creates a histogram.

```python
# IQ samples
iq_scores = [126,  89,  90, 101, 102,  74,  93, 101,  66, 120, 108,  97,  98,
            105, 119,  92, 113,  81, 104, 108,  83, 102, 105, 111, 102, 107,
            103,  89,  89, 110,  71, 110, 120,  85, 111,  83, 122, 120, 102,
            84, 118, 100, 100, 114,  81, 109,  69,  97,  95, 106, 116, 109,
            114,  98,  90,  92,  98,  91,  81,  85,  86, 102,  93, 112,  76,
            89, 110,  75, 100,  90,  96,  94, 107, 108,  95,  96,  96, 114,
            93,  95, 117, 141, 115,  95,  86, 100, 121, 103,  66,  99,  96,
            111, 110, 105, 110,  91, 112, 102, 112,  75]

# Create figure
plt.figure(figsize=(6, 4), dpi=150)
# Create histogram
plt.hist(iq_scores, bins=10)
plt.axvline(x=100, color='r')
plt.axvline(x=115, color='r', linestyle= '--')
plt.axvline(x=85, color='r', linestyle= '--')
# Add labels and title
plt.xlabel('IQ score')
plt.ylabel('Frequency')
plt.title('IQ scores for a test group of a hundred adults')
# Show plot
plt.show()
```

### Box Plot
- plt.boxplot(x) creates a box plot.

### Scatter Plot

- plt.scatter(x, y) creates a scatter plot of y versus x, varying in marker size and/or color

### Bubble Plot

-plt.scatter creates a bubble plot. The parameters c (color) and s (scale) are used to visualize the third and fourth parameter.


### Layouts

- Subplots are multiple Axes within a figure.
    - plt.subplots(nrows, ncols) – creates a Figure and a set of subplots.
    - plt.subplot(nrows, ncols, index) - adds a subplot to the current Figure.
    - Figure.subplots(nrows, ncols) adds a set of subplots to the specified Figure.
    - Figure.add_subplot(nrows, ncols, index) adds a subplot to the specified Figure.
    - examples: https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/subplots_demo.html



    
## Resources
- Officila Guide: https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html
- Code snippets: https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Pandas

## Python Packages

## Seaborn

Seaborn is a Python data visualization library based on matplotlib. 

https://seaborn.pydata.org/

### Examples

water usage example:

data: water_usage.csv

```csv
,Usage,Percentage
0,Leak,12
1,Clothes Washer,17
2,Faucet,19
3,Shower,20
4,Toilet,24
5,Other,8
```

Graph:
```python
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

mydata = pd.read_csv("water_usage.csv")
# Create figure
plt.figure(dpi=200)
# Create tree map
labels = mydata['Usage'] + ' (' + mydata['Percentage'].astype('str') + '%)'
squarify.plot(sizes=mydata['Percentage'], label=labels, color=sns.light_palette('green', mydata.shape[0]))
plt.axis('off')
# Add title
plt.title('Water usage')
# Show plot
plt.show()

```

## Bokeh

```python
# importing the necessary dependencies
import pandas as pd
from bokeh.plotting import figure, show

# make bokeh display figures inside the notebook
from bokeh.io import output_notebook
output_notebook()

# loading the Dataset with geoplotlib
dataset = pd.read_csv('./data/world_population.csv', index_col=0)

# preparing our data for Germany
years = [year for year in dataset.columns if not year[0].isalpha()]
de_vals = [dataset.loc[['Germany']][year] for year in years]

# plotting the population density change in Germany in the given years
plot = figure(title='Population Density of Germany', x_axis_label='Year', y_axis_label='Population Density')

plot.line(years, de_vals, line_width=2, legend='Germany')

show(plot)


# preparing the data for the second country
ch_vals = [dataset.loc[['Switzerland']][year] for year in years]

# plotting the data for Germany and Switzerland in one visualization, 
# adding circles for each data point for Switzerland
plot = figure(title='Population Density of Germany and Switzerland', x_axis_label='Year', y_axis_label='Population Density')

plot.line(years, de_vals, line_width=2, legend='Germany')
plot.line(years, ch_vals, line_width=2, color='orange', legend='Switzerland')
plot.circle(years, ch_vals, size=4, line_color='orange', fill_color='white', legend='Switzerland')

show(plot)

# display the plots next to each other instead if having them stacked.
# plotting the Germany and Switzerland plot in two different visualizations
# that are interconnected in terms of view port
from bokeh.layouts import gridplot

plot_de = figure(
    title='Population Density of Germany', 
    x_axis_label='Year', 
    y_axis_label='Population Density',
    plot_height=300)

plot_ch = figure(
    title='Population Density of Switzerland', 
    x_axis_label='Year', 
    y_axis_label='Population Density',
    plot_height=300,
    x_range=plot_de.x_range, 
    y_range=plot_de.y_range)

plot_de.line(years, de_vals, line_width=2)
plot_ch.line(years, ch_vals, line_width=2)

plot = gridplot([[plot_de, plot_ch]])

show(plot)

# plotting the above declared figures in a vertical manner
plot_v = gridplot([[plot_de], [plot_ch]])

show(plot_v)

```

### pandassql

pandasql allows you to query pandas DataFrames using SQL syntax. 

https://pypi.org/project/pandasql/


### Geopandas

GeoPandas is an open source project to make working with geospatial data in python easier.

https://geopandas.org/index.html


## Geoplotlib

Geoplotlib is an open-source Python library for geospatial data visualizations which contains a wide range of geographical visualizations. It has a simple interface.

```pip install geoplotlib```

you may also need: ```python -m pip install pyglet```

### Examples

data
```csv
id_report,date_report,description,created_date,lat,lon
138,01/01/2005 12:00:00 AM,Poaching incident,2005/01/01 12:00:00 AM,-7.049359, 34.84144
4,01/20/2005 12:00:00 AM,Poaching incident,2005/01/20 12:00:00 AM,-7.65084, 34.48001
43,01/20/2005 12:00:00 AM,Poaching incident,2005/02/20 12:00:00 AM,-7.843201803, 34.00570378
98,01/20/2005 12:00:00 AM,Poaching incident,2005/02/21 12:00:00 AM,-7.745846318, 33.94852605
```

graph:

```python
# importing the necessary dependencies
import geoplotlib
from geoplotlib.utils import read_csv

# loading the Dataset with geoplotlib
dataset = read_csv('./data/poaching_points_cleaned.csv')
# plotting our dataset with points
geoplotlib.dot(dataset)
geoplotlib.show()

# plotting our dataset as a histogram
geoplotlib.hist(dataset, binsize=20)
geoplotlib.show()

# plotting a voronoi map
geoplotlib.voronoi(dataset, cmap='Blues_r', max_area=1e5, alpha=255)
geoplotlib.show()
```

population data

```csv
Country,City,AccentCity,Region,Population,Latitude,Longitude
ad,aixas,Aixàs,6,,42.4833333,1.4666667
ad,aixirivali,Aixirivali,6,,42.4666667,1.5
ad,aixirivall,Aixirivall,6,,42.4666667,1.5
ad,aixirvall,Aixirvall,6,,42.4666667,1.5
ad,aixovall,Aixovall,6,,42.4666667,1.4833333
ad,andorra,Andorra,7,,42.5,1.5166667
ad,andorra la vella,Andorra la Vella,7,20430,42.5,1.5166667
```

graph

```python
import numpy as np
import pandas as pd
import geoplotlib

# loading the Dataset (make sure to have the dataset downloaded)
dataset = pd.read_csv('./data/world_cities_pop.csv', dtype={'Region': np.str})

# mapping Latitude to lat and Longitude to lon
dataset['lat'] = dataset['Latitude']
dataset['lon'] = dataset['Longitude']

# plotting the whole dataset with dots
geoplotlib.dot(dataset)
geoplotlib.show()

# filter for countries with a population entry (Population > 0)
dataset_with_pop = dataset[(dataset['Population'] > 0)]

print('Full dataset:', len(dataset))
print('Cities with population information:', len(dataset_with_pop))


# showing all cities with a defined population with a dot density plot
geoplotlib.dot(dataset_with_pop)
geoplotlib.show()

# dataset with cities with population of >= 100k
dataset_100k = dataset_with_pop[(dataset_with_pop['Population'] >= 100_000)]

print('Cities with a population of 100k or more:', len(dataset_100k))

# displaying all cities >= 100k population with a fixed bounding box (WORLD) in a dot density plot
from geoplotlib.utils import BoundingBox

geoplotlib.dot(dataset_100k)
geoplotlib.set_bbox(BoundingBox.WORLD)
geoplotlib.show()

#  show only US; use BoundingBox to show certain areas
geoplotlib.dot(dataset_100k)
geoplotlib.set_bbox(BoundingBox.USA)
geoplotlib.show()

```

```python
# https://catalog.data.gov/dataset/national-obesity-by-state-b181b

# importing the necessary dependencies
import json
import geoplotlib
from geoplotlib.colors import ColorMap
from geoplotlib.utils import BoundingBox

# plotting the information from the geojson file
geoplotlib.geojson('data/National_Obesity_By_State.geojson')
geoplotlib.show()

# converting the obesity into a color
cmap = ColorMap('Reds', alpha=255, levels=40)

def get_color(properties):
    return cmap.to_color(properties['Obesity'], maxvalue=40,scale='lin')

# plotting the shaded states and adding another layer which plots the state outlines in white
# our BoundingBox should focus the USA
geoplotlib.geojson('data/National_Obesity_By_State.geojson', fill=True, color=get_color)
geoplotlib.geojson('data/National_Obesity_By_State.geojson', fill=False, color=[255, 255, 255, 255])

geoplotlib.set_bbox(BoundingBox.USA)
geoplotlib.show()
```

**Visually comparing different tile providers¶**

Geoplotlib offers the possibility to switch between several providers of map tiles.
This means we can try out different map tile styles that fit our visualization

Other examples of popular free tile providers are:

- Stamen Watercolor => watercolor
- Stamen Toner => toner
- Stamen Toner Lite => toner-lite
- DarkMatter => darkmatter

More free tile providers for OpenStreetMap can be found here:
https://wiki.openstreetmap.org/wiki/Tile_servers

```python

# importing the necessary dependencies
import geoplotlib

# displaying the map with the default tile provider
geoplotlib.show()

# using map tiles from the dark matter tile provider
geoplotlib.tiles_provider('darkmatter')
geoplotlib.show()

# using custom object to set up tile provider
geoplotlib.tiles_provider({
    'url': lambda zoom, xtile, ytile: 'http://a.tile.openstreetmap.fr/hot/%d/%d/%d.png' % (zoom, xtile, ytile),
    'tiles_dir': 'custom_tiles',
    'attribution': 'Custom Tiles Provider - Humanitarian map style | Packt Courseware'
})
geoplotlib.show()

```

foucs on USA using co-ordinates

```python
# displaying the map with the default tile provider
import geoplotlib
from geoplotlib.utils import BoundingBox
geoplotlib.tiles_provider('watercolor')
bb = BoundingBox(45, -125, 22, -65)
geoplotlib.set_bbox(bb)
geoplotlib.show()

# to save
geoplotlib.savefig(r'c:/temp/filename.png')

help(geoplotlib)
```

