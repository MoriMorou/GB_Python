
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.


import memory_calculation as mc

if __name__ == '__main__':
    length = int(input("Input n: "))
    row = [1, ]
    summ = row[0]

    for i in range(1, length):
        row.append(row[i - 1] / -2)
        summ = summ + row[i]

    print(f'Sum {length} elements in line {row} \n = {summ}')
    print(mc.memory_size(locals()))

# Sum 10 elements in line [1, -0.5, 0.25, -0.125, 0.0625, -0.03125, 0.015625, -0.0078125, 0.00390625, -0.001953125]
#  = 0.666015625
#  <class 'int'> 28 10
#  <class 'list'> 200 [1, -0.5, 0.25, -0.125, 0.0625, -0.03125, 0.015625, -0.0078125, 0.00390625, -0.001953125]
# 	 <class 'int'> 28 1
# 	 <class 'float'> 24 -0.5
# 	 <class 'float'> 24 0.25
# 	 <class 'float'> 24 -0.125
# 	 <class 'float'> 24 0.0625
# 	 <class 'float'> 24 -0.03125
# 	 <class 'float'> 24 0.015625
# 	 <class 'float'> 24 -0.0078125
# 	 <class 'float'> 24 0.00390625
# 	 <class 'float'> 24 -0.001953125
#  <class 'float'> 24 0.666015625
#  <class 'int'> 28 9
# The total sum of memory is: 524 byte

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