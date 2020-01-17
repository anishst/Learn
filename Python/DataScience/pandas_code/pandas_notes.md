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




## Code Snippet

### Concat example

```python
csv_file = 'prices1.csv'
df = pd.read_csv(csv_file)
csv_file2 = 'prices2.csv'
df2 = pd.read_csv(csv_file2)
all_prices = pd.concat([df,df2])
```