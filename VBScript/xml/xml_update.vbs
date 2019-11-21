' this script updates a node in xml xml_file

xml_file = "input_checks.xml"
Set xmlDoc = CreateObject("Microsoft.XMLDOM")
xmlDoc.load xml_file

'Locate the desired node
'Note the use of XPATH instead of looping over all the child nodes
Set nNode = xmlDoc.selectsinglenode("//checkdata/checktype")

'Set the node text with the new value
nNode.text = "1"

'Save the xml document with the new settings.
strResult = xmldoc.save(xml_file)