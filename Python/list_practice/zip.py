""" Use zip to process iterators in parallel 
used when you need to pair data together
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


