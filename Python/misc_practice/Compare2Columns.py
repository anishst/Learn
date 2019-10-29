import csv,os


Col1 = []
with open('reqs.csv','r') as csvFile:
	csvReader = csv.reader(csvFile)
	for row in csvReader:
		Col1.append(row[0])
# print("First Column values:",Col1)

Col2 = []
with open('reqs.csv','r') as csvFile:
	csvReader = csv.reader(csvFile)
	for row in csvReader:
		Col2.append(row[1])
# print("2nd Column values:",Col2)


#  Create 2 sets and load lists into them
Col1Set = set()
for i in Col1:
	Col1Set.add(i)


Col2Set = set()
for i in Col2:
	Col2Set.add(i)


# Do comparison
newSet = Col1Set - Col2Set


for i in newSet:
	print (i)
print(len(Col1))
print(len(Col2))
print("Total Items: ", len(newSet))
