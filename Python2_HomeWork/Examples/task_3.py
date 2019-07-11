import hashlib


print(hashlib.sha1(b'Hello World!').hexdigest())
print(hashlib.sha1(b'Hello World.').hexdigest())
print(hashlib.sha1(b'H').hexdigest())
print(hashlib.sha256(b'H').hexdigest())
print(hashlib.sha512(b'H').hexdigest())

print(hash(b'Hello World!'))
print(hash(b'Hello World!'))
print(hash(b'Hello World!'))