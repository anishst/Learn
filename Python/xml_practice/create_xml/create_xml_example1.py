# https://docs.python.org/3.6/library/xml.etree.elementtree.html
# #http://www.diveintopython3.net/xml.html

from lxml import etree as xml

xml_file_name = 'xml_output.xml'
#  create root
root = xml.Element("addressbook")
entries = xml.Element("items")
root.append(entries)

#  create child
entryElement = xml.Element("entry")
entryElement.text = "test entry"
entries.append(entryElement)

#  create child
entryElement = xml.Element("entry")
entryElement.text = "test entry 2"
entries.append(entryElement)

#  create child with attribute
xml.SubElement(entries, "entry", name="test").text  = 'entry 3'

# write tree to a file
tree = xml.ElementTree(root)
tree.write(xml_file_name, pretty_print=True)


# print element names
for child in entries:
	print(child.tag)

# print element values
for child in entries:
	print(child.text)


