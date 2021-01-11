""" Use zip to process iterators in parallel 
used when you need to pair data together
https://medium.com/techtofreedom/7-levels-of-using-the-zip-function-in-python-a4bd22ee8bcd
"""

names = ["anish", "ligy", "tony", "Leah", "sebastian"]
letters = [len(n) for n in names]

print(names)
print(letters)

longest_name = None
max_letters  = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count
print(longest_name)

for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)


# using zip
for name, count in zip(names,letters):
    if count > max_letters:
        longest_name = name
        max_letters = count    
print(count, longest_name)        


from itertools import zip_longest

a = [1,2,3]
b = ["w", "y", "p", "l", "m"]

for i in zip_longest(a,b):
    print(i)

for i in zip_longest(a,b, fillvalue=0):
    print(i)

# Create and Update Dictionaries by the Zip Function
id = [1, 2, 3, 4]
leaders = ['Elon Mask', 'Tim Cook', 'Bill Gates', 'Yang Zhou']

# create dict by dict comprehension
leader_dict = {i: name for i, name in zip(id, leaders)}
print(leader_dict)
# {1: 'Elon Mask', 2: 'Tim Cook', 3: 'Bill Gates', 4: 'Yang Zhou'}

# create dict by dict function
leader_dict_2 = dict(zip(id, leaders))
print(leader_dict_2)
# {1: 'Elon Mask', 2: 'Tim Cook', 3: 'Bill Gates', 4: 'Yang Zhou'}

# update
other_id = [5, 6]
other_leaders = ['Larry Page', 'Sergey Brin']
leader_dict.update(zip(other_id, other_leaders))
print(leader_dict)


# Get the Transpose of a Matrix
matrix = [[1, 2, 3], [1, 2, 3]]
matrix_T = [list(i) for i in zip(*matrix)]
print(matrix_T)