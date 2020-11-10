# Import pandas
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_html.html
import pandas as pd

csv_file = 'req.csv'

df = pd.read_csv(csv_file)
print(df)

print(df.to_html())