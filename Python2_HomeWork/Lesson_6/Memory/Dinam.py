import sys
a = "Hello world"
b = a
print(sys.getrefcount(a))
print(sys.getrefcount(b))
del(a)
print(sys.getrefcount(b))

