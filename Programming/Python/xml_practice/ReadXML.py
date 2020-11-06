import xml.etree.ElementTree as ET
tree = ET.parse('input_checks.xml')
root = tree.getroot()

#print root tag
print(root.tag)

# print element names
for child in root:
	print(child.tag)

# print element values
for child in root:
	print(child.text)

