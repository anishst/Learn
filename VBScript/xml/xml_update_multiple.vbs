' this script updates a node in xml xml_file

xml_file = "input_checks_multiple.xml"
Set xmlDoc = CreateObject("Microsoft.XMLDOM")
xmlDoc.load xml_file

'Locate the desired nodes
Set check_type_nodes = xmlDoc.selectNodes("//checkdata/checktype")

For Each node in check_type_nodes:
    node.Text = "1"
Next

'Save the xml document with the new settings.
strResult = xmldoc.save(xml_file)