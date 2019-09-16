mylist = (x*x for x in range(3))
print(type(mylist))
for i in mylist:
	print(i)

print("/" *50)
anotherlist = [x+1 for x in range(10)]

for i in anotherlist:
	print(i)