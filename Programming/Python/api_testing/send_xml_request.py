# -*- coding: utf-8 -*-
import requests

# xml = """<?xml version='1.0' encoding='utf-8'?>
# <a>б</a>"""
# headers = {'Content-Type': 'application/xml'} # set what your server accepts
# print(requests.post('http://httpbin.org/post', data=xml, headers=headers).text)


# Set the name of the XML file.
# xml_file = "xxx.xml"
# xml_file = """<?xml version='1.0' encoding='utf-8'?><a>б</a>"""
# headers = {'Content-Type':'text/xml'}
#
# # Open the XML file.
# with open(xml_file) as xml:
#     # Give the object representing the XML file to requests.post.
#     r = requests.post('https://example.com/serverxml.asp', data=xml)
#
# print (r.content);


url = "https://httpbin.org/post"

headers = {"content-type" : "application/soap+xml"}
body = """
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:req="https://httpbin.org/post">
   <soapenv:Header/>
   <soapenv:Body/>
</soapenv:Envelope>
"""

response = requests.post(url, data = body, headers = headers, verify=False)
print(response.content)

