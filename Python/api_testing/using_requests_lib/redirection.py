# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
import requests


url = 'http://github.com'
r = requests.get(url)
# r = requests.get(url, allow_redirects=False)
print(r.status_code)
# github automatically uses https url
print(r.url)
print(r.history)


