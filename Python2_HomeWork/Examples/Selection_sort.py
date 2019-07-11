# сортировка выбором (On^^2)

def selection_sort(array):
    for i in range(len(array)):
        idx_min = i
        for j in range(i + 1, len(array)):
            if array[j] < array[idx_min]:
                idx_min = j
        array[idx_min], array[i] = array[i], array[idx_min]
        print(array)


array = [9, 5, 0, 4, 8, 1, 6, 3, 2, 7]
selection_sort(array)
print(array)
