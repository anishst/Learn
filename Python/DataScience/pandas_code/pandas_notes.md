# Pandas


|Command | Description |
|--------|-------------|
| df.values.tolist() | convert df to list|



## Code Snippet

### Concat example

```
csv_file = 'prices1.csv'
df = pd.read_csv(csv_file)
csv_file2 = 'prices2.csv'
df2 = pd.read_csv(csv_file2)
all_prices = pd.concat([df,df2])
```