# https://lxml.de/tutorial.html#namespaces
# http://effbot.org/zone/element-namespaces.htm

from lxml import etree as xml
xml_file_name = 'xml_output_namespace.xml'

# xhtml = xml.Element("{urn:us:gov:treas:fms:ccmm:otcnet:CardPaymentUploadSchema:v1.0}ocps")
# body = xml.SubElement(xhtml, "{http://www.w3.org/1999/xhtml}body")
# body.text = "Hello World"

# print(xml.tostring(xhtml, pretty_print=True))



# # for entry in range(number_of_entries):
# # 	#  create child with attribute
# # 	xml.SubElement(entries, "entry", name="test").text  = 'entry 1'
# #
# # write tree to a file
# tree = xml.ElementTree(xhtml)
# tree.write(xml_file_name, pretty_print=True)


# TEST 2

# from lxml import etree

#
# attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
#
# root = etree.Element('ClinicalDocument',
#                      {attr_qname: 'urn:hl7-org:v3 CDA.xsd'},
#                      nsmap={None: 'urn:hl7-org:v3',
#                             'mif': 'urn:hl7-org:v3/mif',
#                             'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
#                             })
# print(etree.tostring(root))


# TEST 3 - efactory https://lxml.de/tutorial.html#the-e-factory
from lxml.builder import ElementMaker
# attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
E = ElementMaker(namespace="http://my.de/fault/namespace",
                  nsmap={'ocps' : "http://my.de/fault/namespace",
                         'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                         })

DOC = E.BatchTransmission
TITLE = E.title
SECTION = E.section
PAR = E.par

my_doc = DOC(
   TITLE("The dog and the hog"),
   SECTION(
     TITLE("The dog"),
     PAR("Once upon a time, "),
     PAR("And then ")
   ),
   SECTION(
     TITLE("The hog"),
     PAR("Sooner or later ")
   )
 )

print(xml.tostring(my_doc, pretty_print=True))
# write tree to a file
tree = xml.ElementTree(my_doc)
tree.write(xml_file_name, pretty_print=True, encoding='utf-8', xml_declaration=True, standalone=True)


# test 5 https://stackoverflow.com/questions/39619046/lxml-xsischemalocation-namespace-uri-validation-issue
from lxml import etree

attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")

root = etree.Element('ClinicalDocument',
                     {attr_qname: 'urn:hl7-org:v3 CDA.xsd'},
                     nsmap={None: 'urn:hl7-org:v3',
                            'mif': 'urn:hl7-org:v3/mif',
                            'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
                            })
print(xml.tostring(root, pretty_print=True))

# test 6 https://stackoverflow.com/questions/2850823/multiple-xml-namespaces-in-tag-with-lxml
xmlns = "http://www.topografix.com/GPX/1/1"
xsi = "http://www.w3.org/2001/XMLSchema-instance"
schemaLocation = "http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd"
version = "1.1"
ns = "{xsi}"

getXML = etree.Element("{" + xmlns + "}gpx", version=version,
                       attrib={"{" + xsi + "}schemaLocation" : schemaLocation},
                       creator='My Product', nsmap={'xsi': xsi, None: xmlns})

print(etree.tostring(getXML, xml_declaration=True,
                     standalone='Yes', encoding="UTF-8",
                     pretty_print=True))

# test 7 https://stackoverflow.com/questions/25132998/how-to-add-namespace-prefix-to-attribute-with-lxml-node-is-with-other-namespace

# from lxml.etree import Element, SubElement, QName, tostring, ElementTree
#
# class XMLNamespaces:
#    ocps = '<url>'
#    vc = 'http://www.w3.org/2007/XMLSchema-versioning'
#    otcn = '<url>'
#    xsi = 'http://www.w3.org/2001/XMLSchema-instance'
#
#
#
# attr_qname = QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
# root = Element(QName(XMLNamespaces.ocps, 'BatchTransmission'),
#                {attr_qname: 'urn:us:gov:treas:fms:ccmm:otcnet:CardPaymentUploadSchema:v1.0'},
#                nsmap={'ocps':XMLNamespaces.ocps, 'vc':XMLNamespaces.vc, 'otcn': XMLNamespaces.otcn, "xsi": XMLNamespaces.xsi})
#
# TransmissionHeader = SubElement(root, QName(XMLNamespaces.ocps, 'TransmissionHeader'))
# CardDataTransmissionID  = SubElement(TransmissionHeader, QName(XMLNamespaces.ocps, 'CardDataTransmissionID')).text = '{CARDFILE-3s7x-wRjK-AZuh-uWpmahthSUNB}'
# SourceSystem  = SubElement(TransmissionHeader, QName(XMLNamespaces.ocps, 'SourceSystem')).text = 'ats'
#
# BatchData = SubElement(root, QName(XMLNamespaces.ocps, 'BatchData'))
# Transactions  = SubElement(BatchData, QName(XMLNamespaces.ocps, 'Transactions'))
# for i in range(3):
#     Transaction  = SubElement(Transactions, QName(XMLNamespaces.ocps, 'Transaction'))
#
# print(tostring(root, pretty_print=True))
#
# tree = ElementTree(root)
# tree.write(xml_file_name, pretty_print=True, encoding='utf-8', xml_declaration=True, standalone=True)


