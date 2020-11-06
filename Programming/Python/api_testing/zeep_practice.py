# https://docs.python-zeep.org/en/master/
# https://www.techcoil.com/blog/how-to-send-a-http-request-with-client-certificate-private-key-password-secret-in-python-3/

import zeep

# Example 1
# wsdl = 'http://www.soapclient.com/xml/soapresponder.wsdl'
# client = zeep.Client(wsdl=wsdl)
# print(client.service.Method1("This", "is cool!"))
# print(client.service.Method1('Zeep', 'is cool'))

# example 2
wsdl2 = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'
client = zeep.Client(wsdl=wsdl2)
print(client.service.CapitalCity('IND'))
print(client.service.CountryFlag('IND'))

request_data = {  "sCountryISOCode": "IND"}
print(client.service.CapitalCity(**request_data))


# get xml back
from zeep import Client
client = Client('http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL')
node = client.create_message(client.service, 'CapitalCity', sCountryISOCode='IND')
print(node)
