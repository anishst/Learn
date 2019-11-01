import pandas as pd
import os
import csv

path = r"Y:\Testing\Release 2.7\DataPurge\Data to be updated for Purge"
def GetfilesOnly(path):
	for file in os.listdir(path):
		if os.path.isfile(os.path.join(path, file)):
			yield os.path.join(path, file)

for file in GetfilesOnly(path):
	print(file)
	# Load spreadsheet
	xls = pd.ExcelFile(file)
	sheet1 = xls.parse(0)

	# grab first column values only from ss
	df = sheet1[sheet1.columns[0]]
	
	print(df.to_csv(index=False))

	with open("ExcelData.txt", 'a') as textFile:
			textFile.write(sheet1.columns[0] + "\t" +  os.path.basename(file) + "\n")
			textFile.write(df.to_csv(index=False))



	





