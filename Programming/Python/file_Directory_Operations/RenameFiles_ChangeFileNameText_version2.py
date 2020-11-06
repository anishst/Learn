import os

os.chdir(r'Y:\HP ALM Migration\Test Cases\Split Test Cases\USER STORY BASED - INDIVIDUAL TCs\Renamed_Version')

import glob, re, os

pattern = r'_.'
for filename in glob.glob('*.xlsx'):
	print(filename)
	new_name = filename[5:]
	print(new_name)
	os.rename(filename, new_name)