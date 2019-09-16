# fstring usage
# need python 3.6 or higher

first_name = 'Anish'
last_name = 'sebastian'

sentence = f'My name is {first_name} {last_name}'
print(sentence)
#  using functions 
sentence = f'My name is {first_name.upper()} {last_name.upper()}'
print(sentence)
# print dic values
person = {'name': 'Anish', 'age': 28}

print(f'2*5 is eual to {2*5}')


# apply padding
for n in range(1,5):
	sentence = f'the value is {n:02}'
	print(sentence)