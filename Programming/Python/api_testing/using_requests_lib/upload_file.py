import requests

url = 'https://httpbin.org/post'

# open in binary
file = { 'file': open('test.csv', 'rb')}

r = requests.post(url, files=file, verify=False)
print(r.status_code)
print(r.text)