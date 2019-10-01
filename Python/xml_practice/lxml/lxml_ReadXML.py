# http://lxml.de/tutorial.html

from lxml import etree as ET

file = 'input_checks.xml'

xmlDoc = ET.parse(file)

for record in xmlDoc.xpath('//checkdata'):
	for sf in record.getchildren():
		print(sf.text)
