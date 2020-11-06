# https://towardsdatascience.com/use-python-to-automate-your-excel-work-c16b6e5ab58e
import pandas as pd
url = 'https://github.com/datagy/mediumdata/raw/master/exceltopandas.xlsx'
excel_file = pd.ExcelFile(url)

print(excel_file.sheet_names)

# for-loop to loop over each sheet in the Excel workbook, generated a temporary dataframe with its data
# (skipping the first three rows), and appended each item to the dataframe df.
# Finally, you printed the first five records, using the .head()method.

df = pd.DataFrame()

for sheet in excel_file.sheet_names:
    temp_df = pd.read_excel(url, skiprows=3)
    df = df.append(temp_df, ignore_index=True)

print(df.head())

# alt to for loop
# df = pd.concat(pd.read_excel(url, sheet_name=None, skiprows=3), ignore_index=True)
# print(df.head())


# total value of each sale by Type and Region, across the various months.
pivot = pd.pivot_table(df,
                       index=[df['Date'].dt.month, 'Type'],
                       columns='Region',
                       values='Amount',
                       aggfunc='sum',
                       fill_value=0)

print(pivot)


pivot.plot.bar(stacked=True)