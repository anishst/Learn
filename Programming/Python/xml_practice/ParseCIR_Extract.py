# script assumes xml data was created using urn:us:gov:treas:fms:BusinessTransaction:v4.6.1

import xml.etree.ElementTree as etree

tree = etree.parse('CIR_Extract.xml')
root = tree.getroot()
# print(root)

SummaryEntries = tree.findall('{urn:us:gov:treas:fms:BusinessTransaction:v4.6.1}Summary')
# total summary elements
print("**********************************************************************")
print("Total Summary Elements: {}".format(len(SummaryEntries)))
print("**********************************************************************")
# print(len(SummaryEntries[0].attrib))

# loop thru all attributes of Summary element
for i in range(0, len(SummaryEntries)):
	for key, value in SummaryEntries[i].attrib.items():
		print(key  + ":" + value)
	print("======================================================================")	
# loop thru each Batch elements
for BT in tree.findall('{urn:us:gov:treas:fms:BusinessTransaction:v4.6.1}Batch'):
	print("**********************************************************************")
	print("Total Business Transaction Elements: {}".format(len(BT)))	
	print("**********************************************************************")	
	for i in range(0,len(BT)):
		print("=================================================================")
		for key, value in BT[i].attrib.items():
			print(key  + ":" + value)


