# https://github.com/m-click/requests_pkcs12

"""Shows how to use p12 file and password along with python requests lib"""
p12pass = b'<sslpassword>'
url = f"<apiurl>>"
from requests import Session
from requests_pkcs12 import Pkcs12Adapter

with Session() as s:
    s.mount(url,Pkcs12Adapter(pkcs12_filename='<p12_keystore_filename>.p12', pkcs12_password=p12pass))
    # r = s.get(url)

    payload = """
     xml request
     """
    r = s.post(url, data=payload)
    print(r.text)