# https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd
import sqlite3 as sl
import pandas as pd

con = sl.connect('my-test.db')

#  create a df
df_skill = pd.DataFrame({
    'user_id': [1,1,2,2,3,3,3],
    'skill': ['Network Security', 'Algorithm Development', 'Network Security', 'Java', 'Python', 'Data Science', 'Machine Learning']
})


df_skill.to_sql('SKILL', con)

df = pd.read_sql('''SELECT * from SKILL''', con)
print(df)


con.execute('DROP TABLE SKILL')