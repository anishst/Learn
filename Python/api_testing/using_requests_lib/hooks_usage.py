import requests

setCookieUrl = 'https://httpbin.org/cookies/set'
getCookieUrl = 'https://httpbin.org/cookies'

# callback function

def response_info(r, *args, **kwargs):
    print(r.status_code, r.url)
    print(r.text)

def response_headers(r, *args, **kwargs):
    print(r.headers)


hooks = {'response': (response_info, response_headers)}

r = requests.get('https://httpbin.org/get', hooks=hooks, verify=False)





