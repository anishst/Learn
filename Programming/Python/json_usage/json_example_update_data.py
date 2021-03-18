# https://docs.python.org/3/library/json.html
# JSON - JavaScript Object Notation
# https://www.youtube.com/watch?v=9N6a-VLBa2I
# https://github.com/CoreyMSchafer/code_snippets/tree/master/Python-JSON

import json

# ================================================================================================
#  Using a string json 
# ================================================================================================

# json python string
people_string = '''
{
	"people": [
		{
			"name": "Anish Sebastian",
			"phone": "233-230-1238",
			"emails": ["test@yahhoo.com", "test1@gmail.com"],
			"has_license": false
		},
		{

			"name": "Ligy Sebastian",
			"phone": "490-230-1238",
			"emails": null,
			"has_license": true 
		}
	]
}
'''

#  load json string to python dictonary - for more info on converseion types: see https://docs.python.org/3/library/json.html#json.JSONDecoder 
data = json.loads(people_string)

print("updating names thru all people...")
for person in data['people']:
	print(person)
	person["name"] = person["name"] + "UPDATED"



new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)