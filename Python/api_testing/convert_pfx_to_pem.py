"""Script to convert a pfx/p12 file to PEM format

            .pem
Defined in RFCs 1421 through 1424, this is a container format that may include just the public certificate
(such as with Apache installs, and CA certificate files /etc/ssl/certs), or may include an entire certificate
chain including public key, private key, and root certificates. Confusingly, it may also encode a CSR
(e.g. as used here) as the PKCS10 format can be translated into PEM. The name is from Privacy Enhanced Mail (PEM),
a failed method for secure email but the container format it used lives on, and is a base64 translation of
the x509 ASN.1 keys.

            .pkcs12 .pfx .p12 -
Originally defined by RSA in the Public-Key Cryptography Standards (abbreviated PKCS),
the "12" variant was originally enhanced by Microsoft, and later submitted as RFC 7292.
This is a passworded container format that contains both public and private certificate pairs. Unlike .pem files,
this container is fully encrypted. Openssl can turn this into a .pem file with both
public and private keys: openssl pkcs12 -in file-to-convert.p12 -out converted-file.pem -nodes

https://serverfault.com/questions/9708/what-is-a-pem-file-and-how-does-it-differ-from-other-openssl-generated-key-file

"""

# https://gist.github.com/erikbern/756b1d8df2d1487497d29b90e81f8068
# https://github.com/mvantellingen/python-zeep/issues/824
# pip install pyOpenSSL


import contextlib
import OpenSSL.crypto
import requests


@contextlib.contextmanager
def pfx_to_pem(pfx_path, pfx_password):
    ''' Decrypts the .pfx file to be used with requests. '''
    # with tempfile.NamedTemporaryFile(suffix='.pem') as t_pem:
    filename = 'test.pem'

    f_pem = open(filename, 'wb')
    pfx = open(pfx_path, 'rb').read()
    p12 = OpenSSL.crypto.load_pkcs12(pfx, pfx_password)
    f_pem.write(OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, p12.get_privatekey()))
    f_pem.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, p12.get_certificate()))
    ca = p12.get_ca_certificates()
    if ca is not None:
        for cert in ca:
            f_pem.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, cert))
    f_pem.close()
    yield filename

# HOW TO USE:
p12file = 'filenmaem.p12'
p12pass = b'<passpharase>'
url = "<url of webservice>"

payload = """
<xml data goes here>
"""
with pfx_to_pem(p12file, p12pass) as cert:
    response = requests.post(url, cert=cert, data=payload)
    print(response)
    print(response.content)
    print(response.content.decode('utf-8'))


# using generated pem
response = requests.post(url, cert='test.pem', data=payload)
print(response.content)