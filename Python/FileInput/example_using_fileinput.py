import fileinput
import re
import os

filelist = []

# define folder location with form packages
start_path = r"C:\Users\532975\Downloads"

# Get a list FormCfg.xml files
for (path,dirs,files) in os.walk(start_path):
	for file in files:
		if file == 'FormCfg.xml':
			filelist.append(os.path.join(path,file))

print("{} 'FormCfg.xml' files identified for processing".format(len(filelist)))

for fileToSearch in filelist:
	print("Processsing {}".format(fileToSearch))

	currentVersion = ""
	newVersion = ""
	
	# Find existing version number and set new number
	with open(fileToSearch, "r") as f:
		for line in f:
			regex = r'Package version="(.+?)"'
			try:
				found = re.search(regex, line).group(1)
				currentVersion = found
				newVersion = int(found) + 1
			except AttributeError:
				found = ''

	# Update file
	
	# with fileinput.FileInput(fileToSearch, inplace=True, backup='.bak') as file: # use this if backup is needed
	with fileinput.FileInput(fileToSearch, inplace=True) as file:
	    for line in file:
	        print(line.replace(currentVersion, str(newVersion)), end='')
	
	print("Processsing complete. Old Version# {} New Version# {}".format(currentVersion, newVersion))	        
