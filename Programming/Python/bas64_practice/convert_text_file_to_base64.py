import base64

data = open("test.txt", "rb").read()
encoded = base64.b64encode(data)
print(data)


# decode
decoded_string = base64.b64decode(encoded).decode('utf-8')
print(decoded_string)

#  get size of string in bytes
string_len = (len(encoded) * 3 / 4) # length in bytes
print(string_len)

#  get file size using python os
import os
print(os.path.getsize('test.txt'))


