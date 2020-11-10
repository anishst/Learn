import pandas as pd 


datafile = 'https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv'

neededData = []

chunksize = 50 # number of lines to read at a time


for chunk in pd.read_csv(datafile, chunksize=chunksize):

	print(f"Reading {chunksize} lines at a time")
	print(chunk.info(memory_usage='deep'))
	print(type(chunk))
	# print(chunk.describe)
	print(chunk.head(2))
	print(chunk['continent'].unique())
	# print(chunk.info())
	print("*" * 40)


