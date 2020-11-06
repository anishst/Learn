'Source: https://stackoverflow.com/questions/23766435/replace-all-text-in-text-file-using-regular-expression

xml_file = "input_checks_no_root_tag.xml"
check_type_value = "1"

' read xml file and store value in string
Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objTxtFile = objFSO.OpenTextFile(xml_file, 1)
strText = objTxtFile.ReadAll
objTxtFile.Close
Set objTxtFile = Nothing

' find pattern and replace
b = ""
Set objRegEx = CreateObject("VBScript.RegExp")
With objRegEx
    .Global = True
    .MultiLine = True
    'find pattern
    .Pattern = "<checktype>(.+)</checktype>"
    'Indicate new value
    b = objRegEx.Replace(strText, "<checktype>"& check_type_value & "</checktype>")
End With
Set objRegEx = Nothing

' overwrite xml file with new string
Set objTxtFile = objFSO.OpenTextFile(xml_file, 2)
objTxtFile.Write b
objTxtFile.Close
Set objTxtFile = Nothing