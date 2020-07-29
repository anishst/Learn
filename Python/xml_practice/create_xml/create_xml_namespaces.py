# https://lxml.de/tutorial.html#namespaces
# http://effbot.org/zone/element-namespaces.htm

from lxml import etree as xml

xhtml = xml.Element("{urn:us:gov:treas:fms:ccmm:otcnet:CardPaymentUploadSchema:v1.0}ocps")
body = xml.SubElement(xhtml, "{http://www.w3.org/1999/xhtml}body")
body.text = "Hello World"

print(xml.tostring(xhtml, pretty_print=True))


xml_file_name = 'xml_output_namespace.xml'

# for entry in range(number_of_entries):
# 	#  create child with attribute
# 	xml.SubElement(entries, "entry", name="test").text  = 'entry 1'
#
# write tree to a file
tree = xml.ElementTree(xhtml)
tree.write(xml_file_name, pretty_print=True)

