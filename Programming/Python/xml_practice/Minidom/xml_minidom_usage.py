# https://docs.python.org/2/library/xml.dom.minidom.html#module-xml.dom.minidom
import xml.etree.ElementTree as ET
import random,string


def RandomNumber(len):
	char_set = string.digits
	text = ''.join(random.sample(char_set*len, len))
	return text	

# ************** TEST DATA  - UPDATE BEFORE RUNNING ********************

CHECK_TYPE = '1'  #  TYPE OF CHECK: 1=Personal 2=Non-Personal 
RTN = "101108319" # Routing number
ACCOUNT_NUMBER = '80002' # account number
CHECK_NUMBER = str(random.randint(1,2000)) # random check number
# CHECK_NUMBER = RandomNumber(21)
# **********************************************************************


if CHECK_TYPE == '1': 
	MICR_Line = 'T'+ RTN + 'T    ' + ACCOUNT_NUMBER + 'O' + CHECK_NUMBER # personal
else: 
	MICR_Line = 'O' + CHECK_NUMBER + 'O T'+ RTN + 'T    ' + ACCOUNT_NUMBER + 'O' # non-personal

# dictionary with XML file elements
checkInfo = {
'scannerserialnumber':'5703523',
'make':'Panini',
'model':'Panini',
'firmwareversion':'16911104',
'checktype': CHECK_TYPE,
'micr':MICR_Line,
'micrlinestatus':'0',
'accountnumber': ACCOUNT_NUMBER,
'banknumber':RTN,
'checknumber':CHECK_NUMBER,
'transitnumber':RTN,
'imagesize':'1',
'imagequality':'1',
'countrycode':'1',
'serialnumber':'',
'checkamount':'',
'irn':'',
'datetime':'',
'capturetime':'',
'epc':'',
'imagequalityresult':'',
'imagequalityreport':'',
'base64checkimage':''
}

root = ET.Element("checkdata")

for key, value in checkInfo.items():
	child = ET.Element(key)
	child.text = value
	root.append(child)
#  save file
tree = ET.ElementTree(root)
print(tree)

from xml.dom import minidom
xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="\t",encoding=None)
print(xmlstr)
with open("xml_minidom.xml", "w") as f:
    f.write(xmlstr)

# delete first line from file to remove '<?xml version="1.0" ?>'
with open('xml_minidom.xml', 'r') as fin:
    data = fin.read().splitlines(True)
with open('xml_minidom.xml', 'w') as fout:
    fout.writelines(data[1:])

tree.write('mockscan.xml')
