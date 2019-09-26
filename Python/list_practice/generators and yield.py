# Generators are iterators, but you can only iterate over them once. 
# It’s because they do not store all the values in memory, 
# they generate the values on the fly

#  resources:
# CBT nuggest video: https://www.youtube.com/watch?v=uJ-kwDo5b_c&t=504s

print("Creating generator using gen comprehension")
mygenerator = (x*x for x in range(3))
for i in mygenerator:
	print(i)

# Yield is a keyword that is used like return, 
# except the function will return a generator.
def createGenerator():
	mylist = range(3)
	for i in mylist:
		yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!

# next keyword returns one value at a time from iterator; 
# when reaches last item it will generate 'StopIteration' error
print(next(mygenerator))
print(next(mygenerator))
print(next(mygenerator))
# print(next(mygenerator))

# for i in mygenerator:
# 	print(i)		

# generator expression
# gx = (i *2 for i in range(4,7))
# print(gx)
# print(next(gx))

print("Example: Using generator to read value from a list")
ml = [1,0,12,2,3,4,5]
genxp = (i for i in ml if i > 2)
for i in genxp:
	print(i)