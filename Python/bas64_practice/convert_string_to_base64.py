import base64

my_string_value = """my_string
"""
base64_string = base64.b64encode(my_string_value.encode())
print(base64_string)
# print without b
print(base64_string.decode())


# decode
decoded_string = base64.b64decode(base64_string).decode('utf-8')
print(decoded_string)

#  get size of string in bytes
string_len = 3 * (len(base64_string) / 4) # length in bytes
print(string_len)




