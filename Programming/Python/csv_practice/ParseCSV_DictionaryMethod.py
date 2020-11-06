import csv

# Read and print out csv file contents - FINAL
with open("reqs.csv", "r") as ReqFile:    
	ReqFileReader = csv.DictReader(ReqFile)
	ReqList = []
	for row in ReqFileReader:
		if len(row) != 0:
			ReqList = ReqList + [row]
			print(ReqList)
ReqFile.close()
#