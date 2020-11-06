# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
import requests

url = 'https://httpbin.org/post'
headers = { 'content/type': 'mutlipart/form-data'}
r = requests.post(url, headers=headers, verify=False)
print(r.status_code)
print(r.text)
print(r.request.headers)
print(r.headers)
