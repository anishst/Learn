# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
import requests

# url = 'https://httpbin.org/status/200'
# cause 200 to timeout
# r = requests.get(url, verify=False, timeout=0.1)
# r.raise_for_status()

url = 'https://httpbin.org/status/404'
r = requests.get(url, verify=False)
print(r.status_code)
r.raise_for_status()


