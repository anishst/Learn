import os
basedir = os.path.abspath(os.path.dirname(__file__))
loginFile = os.path.join(basedir, '../logindata/login.txt')

print("i am in sub2_func file")
print(basedir)
print(loginFile)
def readlogin():
	with open(loginFile, 'r') as file:
		print(file.read())