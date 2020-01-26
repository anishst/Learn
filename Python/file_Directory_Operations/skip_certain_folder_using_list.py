import os

ROOT = r'C:\Users\532975\Downloads'

folders_to_skip = ['TEST']

for dirpath, dirnames, filenames in os.walk(ROOT):
	print(dirpath)
	for folder in folders_to_skip:
		if folder in dirnames:
			dirnames.remove(folder)
	print(filenames)


