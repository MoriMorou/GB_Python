def insertion_sort(array):
    for i in range(1, len(array)):
        spam = array[i]
        j = i
        while array[j - 1] > spam and j > 0:
            array[j] = array[j - 1]
            j -= 1
        array[j] = spam
        print(array)
        

array = [9, 5, 0, 4, 8, 1, 6, 3, 2, 7]
insertion_sort(array)
print(array)
