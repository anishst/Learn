import random
import string

# print random integer number between 1 and 10
print(random.randint(1,100))

# print random floating number between 1 and 100
print(random.random() * 100)

# print with 2 decimals
amount = random.random() * 1000
amount = "%.2f"%amount
print(amount)

# sample items
# ex.1 
char_set = string.ascii_letters
print(''.join(random.sample(char_set*10, 10)))

# ex.2
listofitems = ["apple","orange","manago","peach"]
print(random.sample(listofitems,2))


print(random.randrange(0,11))

# print random items from a list using choice method
items = [1,2,3]
print(random.choice(items))

