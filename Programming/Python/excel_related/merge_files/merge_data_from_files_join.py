#https://medium.com/swlh/merging-spreadsheets-with-python-join-d53bc701e4ec

# where spreadsheet columns are joined horizontally based on the same values of your selected columns
import pandas as pd

# Read both Excel files
customers = pd.read_excel("Customers.xlsx")
calls = pd.read_excel("Calls.xlsx")

# Inner Join
inner_join_df = customers.merge(calls, how="inner", on="Name")
inner_join_df.to_excel("InnerJoin.xlsx")

# Left Join
left_join_df = customers.merge(calls, how="left", on="Name")
left_join_df.to_excel("LeftJoin.xlsx")

# Right Join
right_join_df = customers.merge(calls, how="right", on="Name")
right_join_df.to_excel("RightJoin.xlsx")

# Outer Join
outer_join_df = customers.merge(calls, how="outer", on="Name")
outer_join_df.to_excel("OuterJoin.xlsx")