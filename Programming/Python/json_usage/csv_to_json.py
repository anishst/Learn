import csv
import json

with open(r"csv_to_json_input.csv.csv") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# convert
with open('csv_converted.json', 'w') as f:
    json.dump(rows, f)


# read new file
import re
# https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


with open('csv_converted.json') as f:
    posts_json = json.load(f)
    for post in posts_json:
        print(cleanhtml(post["title"]).strip())
        # clean html tagas and only get up to 120 chars
        post["title"] = cleanhtml(post["title"]).strip() [0:120]

        # convert date
        from datetime import  datetime
        date_obj = datetime.strptime(post["created_ts"], '%m/%d/%Y %H:%M')
        post["created_ts"] = str(date_obj)

        if post["last_updated_ts"]:
            date_obj = datetime.strptime(post["last_updated_ts"], '%m/%d/%Y %H:%M')
            post["last_updated_ts"] = str(date_obj)

with open('csv_converted.json', 'w') as jsonFile:
    json.dump(posts_json, jsonFile)
    print(posts_json)