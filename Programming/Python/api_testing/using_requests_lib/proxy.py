import requests

# get an ip from here: https://free-proxy-list.net/
proxies = { 'https': '34.91.135.38:80'}

# without proxy
r = requests.get('https://httpbin.org/ip', verify=False)
print(r.text)

# with proxy
r = requests.get('https://httpbin.org/ip', verify=False, proxies=proxies)
print(r.text)




