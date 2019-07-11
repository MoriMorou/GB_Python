
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.


import memory_calculation as mc

if __name__ == '__main__':
    count_elements = int(input("Input n: "))
    element = 1
    sequence_sum = element
    for counter in range(1, count_elements):
        element /= -2
        sequence_sum += element
    print("For {0} elements, the total sum is {1}.".format(count_elements, sequence_sum))
    print(mc.memory_size(locals()))


# For 10 elements, the total sum is 0.666015625.
#  <class 'int'> 28 10
#  <class 'float'> 24 -0.001953125
#  <class 'float'> 24 0.666015625
#  <class 'int'> 28 9
# The total sum of memory is: 104 byte

# python 3.7.2

# Аппаратные средства:
#
#   Название модели:	iMac
#   Идентификатор модели:	iMac14,2
#   Имя процессора:	Intel Core i7
#   Скорость процессора:	3,5 GHz
#   Количество процессоров:	1
#   Общее количество ядер:	4
#   Кэш 2-го уровня (в каждом ядре):	256 КБ
#   Кэш 3-го уровня:	8 МБ
#   Память:	32 ГБ
#   Версия Boot ROM:	133.0.0.0.0
#   Версия SMC (система):	2.15f7
#   Серийный номер (система):	DGKMM0PSF8JC
#   UUID аппаратного обеспечения:	CE4682D2-7707-5882-B3C5-15281E12D2BB