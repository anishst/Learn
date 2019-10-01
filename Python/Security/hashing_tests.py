import hashlib
BLOCKSIZE = 65536
hasher = hashlib.sha1()
with open('anotherfile.txt', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print(hasher.hexdigest())


# https://www.pythoncentral.io/hashing-strings-with-python/

print("md5")
print("=======================")
mystring = "test"
# Assumes the default UTF-8
hash_object = hashlib.md5(mystring.encode())
print(hash_object.hexdigest())

hash_object = hashlib.md5(b'Hello World')
print(hash_object.hexdigest())

print("sha512")
print("=======================")
hash_object = hashlib.sha512(b'Hello World')
hex_dig = hash_object.hexdigest()
print(hex_dig)