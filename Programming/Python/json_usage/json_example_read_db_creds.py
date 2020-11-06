import json

# ================================================================================================
#  Using a json file 
# ================================================================================================
with open('db_pwds.json') as file:
	data = json.load(file)

print(data['QAECH'])

for key, value in data.items():
	print(key,value)
