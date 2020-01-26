import csv

# Read and print out csv file contents - FINAL
with open("Login.csv", "r") as LoginFile:    
	LoginFileReader = csv.reader(LoginFile)
	UserList = []
	for row in LoginFileReader:
		if len(row) != 0:
			UserList = UserList + [row]
LoginFile.close()
print(UserList)

# Append to text or csv file; same code applies to both format - FINAL
with open("Test.txt", "a",newline="") as LoginFile:    
	LoginFileWriter  = csv.writer(LoginFile)
	LoginFileWriter.writerow(["NEWROLE","NEWROLEID","NEWROLEPWD"])
	LoginFileWriter.writerow(["NEWROLE2","NEWROLEID2","NEWROLEPWD2"])
LoginFile.close()

# Query each row in the file for a certain value and if found print out line containing item - FINAL
query = "HLAS"
with open("Login.csv", "r") as LoginFile:    
	LoginFileReader = csv.reader(LoginFile)
	for row in LoginFileReader:
		for field in row:
			if field == query:
				print(row) # print full row
				print("Password for " + query + " is " + row[2]) # print specific column
LoginFile.close()


txtFile = open(r"DataFiles/PasswordReset.csv",'r') 
txtFileContents = txtFile.readlines()
txtFile.close()	
for i in txtFileContents:
	users.append(i.rstrip('\n'))

users = []
with open(r"DataFiles/PasswordReset.csv") as f:
    users = f.read().splitlines()		