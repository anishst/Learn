import requests

url = 'https://httpbin.org/post'

# open in binary
files = [
    ('copy1', ( 'test.csv', open('test.csv', 'rb'), 'csv')),
    ('copy2', ( 'test.csv', open('test.csv', 'rb'), 'csv'))
    ]

r = requests.post(url, files=files, verify=False)
print(r.status_code)
print(r.text)