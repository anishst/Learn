import os
from sub2.sub2_func import readlogin

basedir = os.path.abspath(os.path.dirname(__file__))
loginFile = os.path.join(basedir, 'logindata/login.txt')
print(loginFile)
print(basedir)
print(os.getcwd())
# filename = r'logindata/login.txt'

filename = loginFile
with open(filename, 'r') as file:
	print(file.read())

readlogin()



