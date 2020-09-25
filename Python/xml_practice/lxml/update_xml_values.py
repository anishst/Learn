# http://lxml.de/tutorial.html

from lxml.etree import Element, SubElement, ElementTree, tostring

# create base xml
from lxml import etree
root = etree.Element("root")
etree.SubElement(root, "a").text = "aval"
etree.SubElement(root, "b").text = "bval"
etree.dump(root)
print("*"*100)

# access one item
print(root[0].text)
print(root.findtext('a')) # Directly retrieve the the title tag's text
# access using iterfind
myval = root.iterfind("a")
print([item.text for item in myval])
etree.dump(root)
print("*"*100)

# update using xpath
a_elm = root.xpath("//a")
print(f"a_elm value is {a_elm[0].text}")
a_elm[0].text = "New Value"
etree.dump(root)
print("*"*100)

# update using a loop
for child in root.iter('a'):
    print(child.tag, child.text)
    # update
    child.text = "Anish"
    print(f"{child.tag} updated to {child.text}")
etree.dump(root)
print("*"*100)


tree = ElementTree(root)
tree.write('xml_update_test.xml', pretty_print=True)