# https://docs.python.org/3/library/json.html
# JSON - JavaScript Object Notation
# https://www.youtube.com/watch?v=9N6a-VLBa2I
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-JSON

import json

# ================================================================================================
#  Using a json file 
# ================================================================================================
with open('states.json') as file:
	data = json.load(file)

# print all data
for state in data['states']:
	print(state['name'],",",state['abbreviation'])

#  print the state names
for state in data['states']:
	print(state['name'])


# delete area codes
for state in data['states']:
  del state['area_codes']

# write to new file; 
# indent formats the json output
with open('new_states.json', 'w') as f:
  json.dump(data, f, indent=2)

