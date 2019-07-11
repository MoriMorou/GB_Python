import sys
class Parent(object):
     def __init__(self):
         self.children = []
     def add(self, ch):
         self.children.append(ch)
         ch.parent = self

class Child(object):
     def __init__(self):
         self.parent = None

p = Parent()
p.add(Child())
print(p)
p.children
print(sys.getrefcount(p))
print(sys.getrefcount(p.children[0]))
