import string

# print (string.printable)

ascii_char_list = [chr(i) for i in range(128)]
for i, char in enumerate(ascii_char_list):
	print(i, "\t", char)


new_string = ""
for char in ascii_char_list:
	new_string += char
print(new_string)

# print([chr(i) for i in range(127)])


# for c in (chr(i) for i in range(14,126)):
# 	print (c)



