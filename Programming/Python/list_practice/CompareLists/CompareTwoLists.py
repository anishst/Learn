def read_file(filename):
	items = []
	with open(filename) as f:
		for item in f:
			items.append(item.strip())
	return items

list1 = read_file('list1.txt')
list2 = read_file('list2.txt')

# list1 = [1,2,3]
# list2 = [8, 4,2,2]


# Union: set of all elements from both sets
print(f"\nCombined Unique Items from List 1 and List 2: {len(set(list1) | set(list2))}")
print('*' * 60)
for item in set(list1) | set(list2):
	# print(item)
	pass


# Intersection: a set of elements that are common in both sets
print(f"\nUnique Items that are in both List 1 and List 2: {len(set(list1) & set(list2))}")
print('*' * 60)
for item in set(list1) & set(list2):
	# print(item)
	pass


# Difference: set of elements that are only in list1 but not in list2
print(f"\nItems that are only in list1 but not in list2: {len(set(list1) - set(list2))}")
print('*' * 60)
for item in set(list1) - set(list2):
	# print(item)
	pass


# Difference: set of elements that are only in list2 but not in list1
print(f"\nItems that are only in list2 but not in list1: {len(set(list2) - set(list1))}")
print('*' * 60)
for item in set(list2) - set(list1):
	# print(item)
	pass

print('{:-^60}'.format('') )
print('{:^60}'.format("LIST COMPARE STATS"))
print('{:-^60}'.format('') )
print(f"{'List1:'} Total Items: {len(list1)} Unique Items: {len(set(list1))}")
print(f"List2: Total Items: {len(list2)} Unique Items: {len(set(list2))}")

mergedlist = list1 + list2
seen = set()
uniq = []
dups = []
for x in mergedlist:
    if x not in seen:
        uniq.append(x)
        seen.add(x)
    else:
    	dups.append(x)

print('{:-^60}'.format('') )
print('{:^60}'.format("COMBINED LIST STATS"))
print('{:-^60}'.format('') )
print(f"Total Items: {len(mergedlist)} \nUnique Items: {len(set(mergedlist))} \nDuplicate Items: {len(dups)}")
print(f"Here are the unique duplicates between list1 and list2: {len(set(dups))}")
# for item in set(dups):
# 	print(item)