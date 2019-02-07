array = [9, 5, 0, 4, 8, 1, 6, 3, 2, 7]

n = 1
while n < len(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]

    n += 1

    print(array)
