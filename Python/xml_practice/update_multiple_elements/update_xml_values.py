# https://docs.python.org/3.3/library/xml.etree.elementtree.html#modifying-an-xml-file

import xml.etree.ElementTree as ET
tree = ET.parse('input_checks.xml')
root = tree.getroot()

# update element based on name using for loop - option 2 - best way
for child in root.iter('checktype'):
    print(child.tag, child.text)
    # update
    child.text = "Anish"
    print(f"{child.tag} updated to {child.text}")

tree.write('input_checks.xml')
