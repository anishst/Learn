#https://docs.python.org/2/library/xml.etree.elementtree.html
#http://www.diveintopython3.net/xml.html

import xml.etree.ElementTree as etree

tree = etree.parse('feed.xml')
root = tree.getroot()

print(len(root))

print(root.tag)
# elements are lists; see element
for child in root:
	print(child)

print(root.attrib)

# Searching For Nodes Within An XML Document
print(root.findall('{http://www.w3.org/2005/Atom}entry') )

entries = tree.findall('{http://www.w3.org/2005/Atom}entry')

title_element = entries[0].find('{http://www.w3.org/2005/Atom}title')
print(title_element.text)

for i in range(0,len(entries)):
	title_element = entries[i].find('{http://www.w3.org/2005/Atom}title')
	print(title_element.text)
