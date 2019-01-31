import sys
# 1619884144
a = 42
print(id(a))
b = 43.0
print(id(b))
c = 'Ж'
print(id(c))

# a = b

print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
s = '123456789'
print(sys.getsizeof(s))

sum_ = 0
for i in s:
    sum_ += sys.getsizeof(i)
    print(sys.getsizeof(i))
print(sum_)

a = set([str(i) for i in range(1, 10)])
print(a)
print(sys.getsizeof(a))


def show_size(x):
    print(sys.getsizeof(x), type(x))
    if hasattr(x, '__iter__'):
        if not isinstance(x, str):
            for item in x:
                show_size(item)

show_size(a)

# size = 16
# allocated = (size >> 3) + (3 if size < 9 else 6)
# len(a) = size + allocated
