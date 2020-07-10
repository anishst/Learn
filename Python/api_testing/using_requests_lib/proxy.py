import requests

# get an ip from here: https://free-proxy-list.net/
proxies = { 'https://': '198.211.101.99:3128'}

# without proxy
r = requests.get('https://httpbin.org/ip', verify=False)
print(r.text)

# with proxy
r = requests.get('https://httpbin.org/ip', verify=False, proxies=proxies)
print(r.text)




