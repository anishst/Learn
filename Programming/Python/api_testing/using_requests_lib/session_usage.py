import requests

# new session object
s = requests.Session()

userName = {'username': 'anish'}
location = {'location': 'ny'}

setCookieUrl = 'https://httpbin.org/cookies/set'
getCookieUrl = 'https://httpbin.org/cookies'

s.get(setCookieUrl, params=userName, verify=False)
s.get(setCookieUrl, params=location, verify=False)

r = s.get(getCookieUrl, verify=False)
print(r.text)





