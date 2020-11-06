# http://books.goalkicker.com/PythonBook/PythonNotesForProfessionals.pdf
import fileinput
replacements = {'Search1': 'Replace1',
			'Search2': 'Replace2'}

for line in fileinput.input(r'filename.txt', inplace=True):
	for search_for in replacements:
		replace_with = replacements[search_for]
		line = line.replace(search_for, replace_with)
	print(line, end='')