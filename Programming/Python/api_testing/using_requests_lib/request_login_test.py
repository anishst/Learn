import requests

payload = {'username': 'otcnqe88', 'PASSWORD': 'value2'}
r = requests.get('https://login.gov/', verify=False, params=payload)
print(r.text)
print(r.url)