# https://docs.python.org/3.6/library/xml.etree.elementtree.html
# #http://www.diveintopython3.net/xml.html

from lxml import etree as xml

xml_file_name = 'xml_output_loop.xml'
#  create root
root = xml.Element("addressbook")
entries = xml.Element("items")
root.append(entries)

number_of_entries = 3

for entry in range(number_of_entries):
	#  create child with attribute
	xml.SubElement(entries, "entry", name="test").text  = 'entry' + str(entry+1)

# write tree to a file
tree = xml.ElementTree(root)
tree.write(xml_file_name, pretty_print=True)

#  find count of entries
record_count = entries.xpath('//entry')
for item in record_count:
	print(item.text)
print(len(record_count))




