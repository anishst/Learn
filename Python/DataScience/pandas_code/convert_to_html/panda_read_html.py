import pandas as pd

test = pd.read_html('https://www.w3schools.com/tags/tag_table.asp')

#  print all table
print(test)

# print 1st table
print(test[1])
