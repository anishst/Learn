text = "yeah,, but no, but yea"

# exact match
print(text == 'yeah')

# match at start or end
print(text.startswith('yeah'))
print(text.endswith('yea'))

# search for the location of the first occurence

print(text.find('but'))
