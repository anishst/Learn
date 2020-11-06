import json

with open('config.json') as json_data_file:
    data = json.load(json_data_file)
print(data)


# write to json
import json
with open('config_output.json', 'w') as outfile:
    json.dump(data, outfile)