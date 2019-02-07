import random


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    small = []
    medium = []
    large = []

    for item in array:
        if item < pivot:
            small.append(item)
        elif item == pivot:
            medium.append(item)
        elif item > pivot:
            large.append(item)

    print(small, medium, large)
    return quick_sort(small) + medium + quick_sort(large)


array = [9, 5, 0, 4, 8, 1, 6, 3, 2, 7]
new_array = quick_sort(array)
# print(array)
print(new_array)
