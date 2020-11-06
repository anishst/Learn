# min max

print(max(3,45,33))

print(max('z', 'b','a'))

nums = [1,3,3,6]
print(max(nums))

print(min(nums))

names = ['anish', 'ligy', 'tony', 'leah', '3232', 'ab']
#  show shortest name len
print(min(len(name) for name in names))

#  show longest name len
print(max(len(name) for name in names))

# show longest name
print(max(names, key=lambda n:len(n)))
print(min(names, key=lambda n:len(n)))

# from list
songs = [

		{"title": "urvasi", "playcount": 3},
		{"title": "mukala", "playcount": 2},
		{"title": "kilukkam", "playcount": 7},
		{"title": "kannam", "playcount": 0}
]

# show song with least paycount
print(min(songs, key=lambda s: s['playcount']))

# show song with most paycount
print(max(songs, key=lambda s: s['playcount']))