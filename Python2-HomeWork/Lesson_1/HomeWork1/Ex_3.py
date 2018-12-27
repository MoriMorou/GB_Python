#3. По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.

print("Input the coordinates of two points ")
print('')
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

if x1 == x2:
    print(f'x = {x1:.2f}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print("y = %.2f * x + %.2f" % (k, b))
