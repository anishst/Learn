# https://docs.github.com/en/rest/overview/resources-in-the-rest-api

import requests

url = 'https://api.github.com/events'

r = requests.get(url, verify=False)
print(r.status_code)
print(r.text)
events = r.json()
# get id from 1st event
print(events[0]['id'])