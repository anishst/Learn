products = [
    ("Product1", 300),
    ("Product2", 3.98),
    ("Product3", 10),
    ("Product4", 57.09),
]

# option 1 using a helper function


def sort_item(item):
    # sorty by price
    return[item[1]]


products.sort(key=sort_item)
print(products)

# option 2 - using lamda function - recommended way

# sort by product
products.sort(key=lambda item: item[0])
print(products)
for item in products:
    print(item[0], item[1])

# sort by price
products.sort(key=lambda item: item[1])
print(products)
for item in products:
    print(item[0], item[1])
