# https://docs.python.org/3.6/library/xml.etree.elementtree.html
# #http://www.diveintopython3.net/xml.html


import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
print(root)

# root has a tag and a dictionary of attributes
print(root.tag)
print(root.attrib)

# children nodes over which we can iterate
for child in root:
	print(child.tag, child.attrib)

# access specific child nodes by index
print(root[0][2].text)

# iterate recursively over all the sub-tree below
for neighbor in root.iter('neighbor'):
	print(neighbor.attrib)


# Element.findall() finds only elements with a tag which are direct children of the current element. 
# Element.find() finds the first child with a particular tag, and 
# Element.text accesses the element’s text content. 
# Element.get() accesses the element’s attributes:
for country in root.findall('country'):
	rank = country.find('rank').text
	name = country.get('name')
	print(name,rank)

# Modifying an XML File
for rank in root.iter('rank'):
	new_rank = int(rank.text) + 1
	rank.text = str(new_rank)
	rank.set('updated','yes')
tree.write('output.xml')