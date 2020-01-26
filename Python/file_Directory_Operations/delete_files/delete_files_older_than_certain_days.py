# https://stackoverflow.com/questions/12485666/python-deleting-all-files-in-a-folder-older-than-x-days
# https://www.blog.pythonlibrary.org/2013/11/14/python-101-how-to-write-a-cleanup-script/
import os, time

path = r'logs/'
now = time.time()

for filename in os.listdir(path):
	if os.path.getmtime(os.path.join(path, filename)) < now - 4 * 86400:
	    if os.path.isfile(os.path.join(path, filename)):
	        print(f"Removing {filename}")
	        os.remove(os.path.join(path, filename))