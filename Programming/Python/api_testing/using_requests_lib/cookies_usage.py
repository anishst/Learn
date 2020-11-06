# https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
import requests

url = 'https://httpbin.org/cookies'

cookies = { 'location': 'Virginia'}
r = requests.get(url, cookies=cookies, verify=False)

print(r.status_code)
print(r.text)
print(r.request.headers)
print(r.headers)

r2 = requests.get('https://www.google.com', verify=False)
print(r2.cookies['1P_JAR'])

