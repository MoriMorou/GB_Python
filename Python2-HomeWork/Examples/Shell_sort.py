def shell_sort(array):
    assert len(array) < 4000, 'Массив слишком большой'

    def new_increment(array):
        inc = [1, 4, 10, 23, 57, 132, 301, 701, 1750]
        while len(array) <= inc[-1]:
            inc.pop()
        while len(inc) > 0:
            yield inc.pop()

    for increment in new_increment(array):
        for i in range(increment, len(array)):
            for j in range(i, increment - 1, -increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
            print(array)


array = [9, 5, 0, 4, 8, 1, 6, 3, 2, 7]
shell_sort(array)
print(array)
