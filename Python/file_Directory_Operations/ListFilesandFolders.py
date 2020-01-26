import os, sys
# provide folder
path = r"C:\Users\532975\Documents\Automation\SeleniumPythonFramework\tests\Stability"

# List all files and directories in current directory
print(os.listdir('.'))

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
print(cwd)

# Change directory 
# os.chdir(path)
# List all files and directories in current directory
os.listdir('.')


# ///////////////////////////////////////////////////////////////
# print files + folders
# ///////////////////////////////////////////////////////////////
dirs = os.listdir('.')
# Print files and directories
for file in dirs:
   print(file)
# ///////////////////////////////////////////////////////////////
# print only file names; skip folders
# ///////////////////////////////////////////////////////////////
def GetfilesOnly(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file
for file in GetfilesOnly(path):
	print(file)


# import os
# for dirpath, dirnames, filenames in os.walk('.'):
#     print("Current Path: {}".format(dirpath))
#     print("Current Directory: {}".format(dirnames))
#     print("Files: {}".format(filenames))



