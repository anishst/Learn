import os

top = r'Y:\Automation 2.0\ALM\Stability'

for dirpath, dirnames, filenames in os.walk(top):
	print(dirpath)
	if 'Offline' in dirnames:
		dirnames.remove('Offline')

