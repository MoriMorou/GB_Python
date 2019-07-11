from collections import deque

# очередь (простой двухсвязный список)
a = deque()
b = deque('abrakadabra')
# maxlen ограничивает размер очереди, если его убрать, то очередь будет бесконечная (очень интересный эффек при
# добалениее значений)
c = deque([1, 2, 3], maxlen=5)
print(a, b, c, sep='\n')

print('*' * 50)
c.append(4)
print(c)
c.appendleft(5)
print(c)
c.extend([6, 7])
print(c)
c.extendleft([8, 9, 10])
print(c)
print(c.pop())
print(c)
print(c.popleft())  # list.pop(0)
print(c)

c.rotate(-2)
print(c)
c.insert(2, 555)
print(c[2])
