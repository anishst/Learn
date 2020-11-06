# https://medium.com/@lovespreadsheets/merging-spreadsheets-with-python-append-591d599d49da
# spreadsheets are concatenated on top of each other
import pandas as pd

# Read all three files into pandas dataframes
file1_names = pd.read_excel("file1.xlsx")
file2_names = pd.read_excel("file2.xlsx")
file3_names = pd.read_excel("file3.xlsx")

# Create a list of the files in order you want them appended
all_df_list = [file1_names,file2_names, file3_names]

# Merge all the dataframes in all_df_list
# Pandas will automatically append based on similar column names
appended_df = pd.concat(all_df_list)

# Write the appended dataframe to an excel file
# Add index=False parameter to not include row numbers
appended_df.to_excel("AllNames.xlsx", index=False)