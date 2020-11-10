# Import pandas
import pandas as pd

# EXAMPLE 1
df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
print("first DataFrame")
print(df)

df2 = pd.DataFrame([[5, 6], [7, 8]],columns=list('AB'))
df2 = df.append(df2, ignore_index=False)
print("with appeneded DataFrame")
print(df2)




