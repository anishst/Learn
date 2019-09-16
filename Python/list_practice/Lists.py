# Lists
# A list is a collection of items in a particular order. In Python, square
# brackets ([]) indicate a list, and individual elements in the list are
# separated by commas.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing Elements in a List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])

# access last time
print("last item:", bicycles[-1])
# access 2nd to last
print("2nd to last item:",bicycles[-2])
# Using Individual Values from a List
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# Modifying Elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)

# Appending Elements to the End of a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

# Inserting Elements into a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing an Item Using the del Statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# Removing an Item Using the pop() Method
# The pop() method removes the last item in a list, but it lets you work
# with that item after removing it.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


# Sorting a List Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# Finding the Length of a List
print(len(cars))


# Looping Through an Entire List
# when writing your own for loops that you can choose any name you want
# for the temporary variable that holds each value in the list
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
for magician in magicians:
    print(magician.title() + ", that was a great trick!")

# Using range() to Make a List of Numbers
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
    print(squares)

# List Comprehensions
# A list comprehension allows you to generate this same list in just one
# line of code.
squares = [value**2 for value in range(1, 11)]
print(squares)


# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))



requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")


#========================================
# Lists
#========================================
sampleList = [1,2,3,4,5,6,7,8,10,9]
print (sampleList[1])
print(sampleList)
for a in sampleList: # looping thru the list
    print(a)
    pass

sampleList.append(13) # appends element to end of the list
print(sampleList)
sampleList.count('2') # counts the number of occurrences of 'x' in the list
print(sampleList)
sampleList.index(1) # returns the index of 'x' in the list
print(sampleList)
sampleList.insert(2,'100') # inserts 'x' at location 'y'
print(sampleList)
sampleList.pop() # returns last element then removes it from the list
print(sampleList)
sampleList.remove(1) # finds and removes first 'x' from list
print(sampleList)
sampleList.reverse() # reverses the elements in the list
print(sampleList)
#sampleList.sort() # sorts the list alphabetically in ascending order, or numerical in ascending order

# Moving Items from One List to Another
#   Start with users that need to be verified,
#   and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
#   Verify each user until there are no more unconfirmed users.
#   Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("\nVerifying user: " + current_user.title())
    confirmed_users.append(current_user)
# Display all confirmed users.
    print("\nThe following users have been confirmed:")
    for confirmed_user in confirmed_users:
        print(confirmed_user.title())


#   Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)


"""Enumerate list items - when u need to iterate overa list 
and also needs to know the index of the current item """
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

for i, pet in enumerate(pets):
    # print('%d: %s' % (i+1,pet))
    print("{}: {}".format(i+1,pet))

# supply a second paramter to specifiy the number from which to start counting
for i, pet in enumerate(pets, 1):
    # print('%d: %s' % (i+1,pet))
    print("{}: {}".format(i,pet))