# map() loops over the items of an input iterable (or iterables) and returns an iterator that
# results from applying a transformation function to every item in the original input iterable.
# https://realpython.com/python-map-function/

# without map
numbers = [1, 2, 3, 4, 5]
squared = []
for num in numbers:
    squared.append(num ** 2)
print(squared)

#  using map
def square(number):
    return number ** 2
numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)
print(list(squared))

# Processing Multiple Input Iterables With map()#
first_it = [1, 2, 3]
second_it = [4, 5, 6, 7]
print(list(map(pow, first_it, second_it)))

# clean up data
with_dots = ["processing..", "...strings", "with....", "..map.."]
print(list(map(lambda s: s.strip("."), with_dots)))

import re
def remove_punctuation(word):
    return re.sub(r'[!?.:;,"()-]', "", word)

print(remove_punctuation("...Python!"))

