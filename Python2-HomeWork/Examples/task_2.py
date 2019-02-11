h_list = [None] * 26

def my_append(value):
    index = ord(value[0]) - ord('a')
    h_list[index] = value
    print(h_list)

a = 'apricot'
my_append(a)

b = 'banana'
my_append(b)

c = 'apple'
my_append(c)

print(5476 == 5*10**3 + 4*10**2 + 7*10**1 + 6*10**0)

def my_index(value):
    letter = 26
    index = 0
    size = 10000
    for i, char in enumerate(value):
        index += (ord(char) - ord('a') + 1) * letter ** i
    return index % size

print(my_index(a))
print(my_index(b))
print(my_index(c))