# READ METHOD 1 - simple
# ===========================================================
# f = open("test.txt", 'r')
# print(f.name)
# print(f.mode)
# print(f.read())
# f.close()


# READ METHOD 2 - using context manager - recommeneded 
# ===========================================================
# with open("test.txt", 'r') as f:
# 	f_contents = f.read()
# 	print(f_contents)

# # produces a list
# with open("test.txt", 'r') as f:
# 	f_contents = f.readlines()
# 	print(f_contents)

# # one line at a time
# with open("test.txt", 'r') as f:
# 	f_contents = f.readline()
# 	print(f_contents)

# 	f_contents = f.readline()
# 	print(f_contents)	


# READ METHOD 3 - more memory efficient
# ===========================================================
# with open("test.txt", 'r') as f:

# 	for line in f:
# 		print(line, end='')


# READ METHOD 4 - Read in chunks
# ===========================================================

# with open("test.txt", 'r') as f:
	
# 	size_to_read = 15
# 	f_contents = f.read(size_to_read)

# 	while len(f_contents) > 0:
# 		print(f_contents, end='')
# 		f_contents = f.read(size_to_read)


# WRITE METHOD  - Read a text file and write to another
# ===========================================================

with open("Test.txt", 'r') as rf:
	with open("Test_Copy.txt", 'w') as wf:
		for line in rf:
			wf.write(line)

# WRITE METHOD  - Read a text file and write to another but only certain value
# ===========================================================

with open("Test.txt", 'r') as rf:
	with open("Test_Copy.txt", 'w') as wf:
		for line in rf:
			items = line.split(' ')
			print(items)
			wf.write(items[0] + "," + items[1])

# WRITE METHOD  - working with binary file
# ===========================================================

with open("google.png", 'rb') as rf:
	with open("google_Copy.png", 'wb') as wf:
		for line in rf:
			wf.write(line)