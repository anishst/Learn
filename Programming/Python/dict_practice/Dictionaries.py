#========================================
""" Dictionaries
A dictionary in Python is a collection of key-value pairs. Each key is connected 
to a value, and you can use a key to access the value associated with that key.
A key’s value can be a number, a string, a list, or even another dictionary.

unordered sets but fast since they use hash keys
also called assoc. array/hash tables
tuples can be used as key but not lists

methods:

keys()
items()
values()

pop() - remove key from dict
clear() - purge all items
"""
#========================================

months = {1: "jan", 2: "feb"}
print(months)

print(months.keys())
print(months.values())
print(months[2])

# add items
months[3] = "march"
print(months)
# redefine
months[3] = "mar"
print(months)

#conver to list
months2list = list(months)
print(months2list)

months2list2 = list(months.values())
print(months2list2)

# ad tuple
tup = ("some", "data", "here")
months[4] = tup
print(months)

# get length of dict
print(len(months))


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
print(alien_0['color'])
print(alien_0['points'])

# Adding New Key-Value Pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

# Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# A Dictionary of Similar Objects
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	'Anish': 'python',
}
print(favorite_languages)
print("Anish's fav lan is: " + 
	favorite_languages['Anish'].title() +
	".")

# Looping Through a Dictionary
for key, value in favorite_languages.items():
	print("\nKey: " + key)
	print("Value: " + value)

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")

# Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
	print(name.title())

if "Ligy" not in favorite_languages.keys():
	print("Ligy, please take our poll!")

# Looping Through a Dictionary’s Keys in Order
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

# Looping Through All Values in a Dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

# Looping Through All Values in a Dictionary - remove dups using set
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

# Nesting
# A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
# Show the first 5 aliens:
for alien in aliens[:5]:
	print(alien)
	print("...")
# Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

# A List in a Dictionary
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}
# Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping)

favorite_languages = {
	'jen': ['python','ruby'],
	'sarah': ['c'],
	'edward': ['ruby','Pascal'],
	'phil': ['python','Java'],
	'Anish': ['python','c#'],
}
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())


# A Dictionary in a Dictionary
users = {
	'aeinstein': {
	'first': 'albert',
	'last': 'einstein',
	'location': 'princeton',
	},
	'mcurie': {
	'first': 'marie',
	'last': 'curie',
	'location': 'paris',
	},
}
for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())


#  USING nested dict arrays
nested_dict = {
	"stability": {
		"non_csn":[
			"test1",
			"test2"
		],
		"full_stability": [
			"test1",
			"test2"
		]
	},
	"regression": {
		"non_csn": [
			"test1",
			"test2"
		]
	}
}

for key, val in nested_dict.items():
	print(key,val)

print("Stabily scripts")
print(nested_dict["stability"].items())
print(nested_dict["stability"]["full_stability"])
for k, va in nested_dict["stability"].items():
	print(k)