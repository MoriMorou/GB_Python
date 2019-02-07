from random import random
from array import array

M = 10
N = 5
a = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(int(random() * 11))
        print("%3d" % b[j], end='')
    a.append(b)
    print('   ')

