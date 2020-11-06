# Example of incremental XML parsing
# https://github.com/dabeaz/python-cookbook/blob/8a71861a81350e55bd77556996ac3b530a1ffe5e/src/6/incremental_parsing_of_huge_xml_files/example.py

# The file 'potholes.xml' is a greatly condensed version of a larger
# file available for download at
#
# https://data.cityofchicago.org/api/views/7as2-ds3y/rows.xml?accessType=DOWNLOAD

from xml.etree.ElementTree import iterparse

def parse_and_remove(filename, path):
    print("starting parse...")
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
            print(elem.tag)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass

# Find zip code with most potholes

from collections import Counter
potholes_by_zip = Counter()

data = parse_and_remove('rows.xml', 'row/row')
for pothole in data:
    potholes_by_zip[pothole.findtext('zip')] += 1

for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)