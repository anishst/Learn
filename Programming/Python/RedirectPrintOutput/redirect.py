import sys
sys.stdout = open("Redirectoutput.txt", "w")
print('Testing')
print ("test sys.stdout")
for i in range(3):
	print(i)
