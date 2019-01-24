from collections import defaultdict

a = defaultdict()
print(a)

s = 'abrakadabra'
b = defaultdict(int)
for char in s:
    b[char] += 1
print(b)

lst = [('cat', 1), ('dog', 2), ('cat', 6), ('dog', 1), ('cat', 5), ('cat', 2), ('dog', 9)]
c = defaultdict(list)
for key, value in lst:
    c[key].append(value)
print(c)

d = defaultdict(lambda: 'unknown')
d.update(rex='dog', boris='cat')
print(d)
print(d['felix'])
