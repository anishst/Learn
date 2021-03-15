import csv
import json

with open('csv_to_json_input.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# convert
with open('csv_converted.json', 'w') as f:
    json.dump(rows, f)


# read new file

with open('csv_converted.json') as f:
    posts_json = json.load(f)
    for post in posts_json:
        print(post["title"])