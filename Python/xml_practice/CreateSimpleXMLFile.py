# https://docs.python.org/3.6/library/xml.etree.elementtree.html
# #http://www.diveintopython3.net/xml.html

import xml.etree.ElementTree as ET

root = ET.Element("root")
doc = ET.SubElement(root,"doc")

ET.SubElement(doc,"field1", name="blah")
ET.SubElement(doc,"field2", name="tony").text = "Some value2"
print(root)

tree = ET.ElementTree(root)
tree.write('SimpleXMLOutput.xml')