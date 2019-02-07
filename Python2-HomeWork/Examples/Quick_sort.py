import random


def quick_sort(array, first, last):
    print(array)
    if first >= last:
        return

    pivot = array[random.randint(first, last)]
    i, j = first, last

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    quick_sort(array, first, j)
    quick_sort(array, i, last)


array = [9, 5, 0, 4, 8, 1, 6, 3, 2, 7]
quick_sort(array, 0, len(array) - 1)
print(array)

