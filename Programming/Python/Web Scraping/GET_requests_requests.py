# https://code.tutsplus.com/tutorials/using-the-requests-module-in-python--cms-28204
import requests

url = "http://www.python4forbeginners.com"
req = requests.get(url)

text = req.text # returns html as string
print(text)
# print(req.encoding)
# print(req.status_code)
# print(req.elapsed)
# print(req.url)

# print(req.history)

# print(req.headers)
# print(req.headers['Content-Type'])

# print(req.encoding)
# print(req.text)

# print(req.cookies)

#  Session objects
# reqOne = requests.get("https://www.google.com")
# print(reqOne.cookies['_tuts_session'])
