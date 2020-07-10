import requests

url = 'https://httpbin.org/post'
data = { 'firstName': 'Anish'}
r = requests.post(url, json=data, verify=False)
print(r.status_code)
print(r.text)