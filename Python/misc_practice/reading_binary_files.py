# http://codeigo.com/python/convert-bytes-to-string

str = 'PI'
str_utf8 = str.encode('utf8')
str_ascii = str.encode('ascii')
str_latin1 = str.encode('latin1')
str_utf16 = str.encode('utf16')
str_utf32 = str.encode('utf32')

print(str, len(str))
print(str_utf8, len(str_utf8))
print(str_ascii, len(str_ascii))
print(str_latin1, len(str_latin1))
print(str_utf16, len(str_utf16))
print(str_utf32, len(str_utf32))