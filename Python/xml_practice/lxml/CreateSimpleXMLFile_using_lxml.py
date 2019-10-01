# http://lxml.de/tutorial.html

from lxml import etree as ET

# create XML
root = ET.Element("root")
# add child
root.append(ET.Element('field1'))
# another child
child = ET.Element("field2")
child.text = ""
root.append(child)


s = ET.tostring(root, pretty_print=True)
print(s)

tree = ET.ElementTree(root)
tree.write('SimpleXMLOutput_lxml.xml', pretty_print=True)