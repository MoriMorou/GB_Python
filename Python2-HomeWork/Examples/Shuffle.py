import random

# Перемешивание массива

array = [i for i in range(10)]
print("Old array", array)
random.shuffle(array)
print("New array", array)
