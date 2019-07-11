import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

POS = 2
NUM = 555

array.append(None)
print(array)
i = len(array) - 1

while i > POS:
    array[i], array[i - 1] = array[i - 1], array[i]
    i -= 1
    print(array)

array[POS] = NUM

# array.insert(POS, NUM)        # array.index()
print(array)