# https://docs.python.org/3/library/json.html
# JSON - JavaScript Object Notation
# https://www.youtube.com/watch?v=9N6a-VLBa2I
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-JSON

import json

# ================================================================================================
#  Using a json file 
# ================================================================================================
with open('questions.json') as file:
	data = json.load(file)

print(data)

for question in data['questions']:
	print(question['question'])
	print(question['category'])
	for answer in question['answers']:
		print(answer)
	print(question['type'])



