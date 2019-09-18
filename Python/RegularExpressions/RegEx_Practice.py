# https://www.youtube.com/watch?v=kWyoYtvJpe4
import re

# searches for email

search_string = "anish in a string anish again anish"

if re.search("anish", search_string):
    print("there is anish in string")

#  using find all - returns a list
all_anish = re.findall('anish', search_string)
for i in all_anish:
    print(i)

#  get iterator for all matching objects
for i in re.finditer("an.", search_string):
    loc_tuple = i.span()
    print(loc_tuple)
    # slice match
    print(search_string[loc_tuple[0]:loc_tuple[1]])


m = re.search(r'[\w.]+@[\w.]+', "blah nick.p@gmail.com")
print(m.group())


m = re.search(r'([\w.]+)@([\w.]+)', "blah nick.p@gmail.com")
print(m.group(0))
print(m.group(1))  # get username; 1 refers to 1st paranetheses
print(m.group(2))  # get domain

m = re.search(r'anish', "ANISH anish Ligy", flags=re.IGNORECASE)
print(m.group())
