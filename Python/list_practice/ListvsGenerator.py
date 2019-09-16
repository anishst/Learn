# https://medium.freecodecamp.org/python-list-comprehensions-vs-generator-expressions-cef70ccb49db

#  regular list
a = 12
b = "this is text"
my_list = [0, b, ['element', 'another element'], (1, 2, 3), a]
print(my_list)

# normal list
my_list = []
for x in range(10):
	my_list.append(x * 2)
print(my_list)

#  list comprehensions allow you to create lists with a for loop with less code
comp_list = [x * 2 for x in range(10)] 
print(comp_list)

# more conditional logic
comp_list = [x ** 2 for x in range(7) if x % 2 == 0] 
print(comp_list)

# create a list of lists by combining two existing lists
nums = [1, 2, 3, 4, 5]
letters = ['A', 'B', 'C', 'D', 'E']
nums_letters = [[n, l] for n in nums for l in letters]
#the comprehensions list combines two simple lists in a complex list of lists.
print(nums_letters)
print(nums_letters)

# dic comprehen
dict_comp = {x:chr(65+x) for x in range(1, 26)}
print(type(dict_comp))
print(dict_comp)

# set compre
set_comp = {x ** 3 for x in range(10) if x % 2 == 0}
print(type(set_comp))
print(set_comp)

simple_list = [1, 2, 3]
my_iterator = iter(simple_list)
# print(my_iterator)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
for x in my_iterator:
	print(x)


# Generator Expressions

gen_exp = (x ** 2 for x in range(10) if x % 2 == 0) 
for x in gen_exp:
	print(x)	

# get memory usage info
from sys import getsizeof
my_comp = [x * 5 for x in range(1000000)]
my_gen = (x * 5 for x in range(10000000))
print("showing memeory usage...")
print(getsizeof(my_comp))
print(getsizeof(my_gen))
