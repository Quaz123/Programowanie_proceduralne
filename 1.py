import copy
import sys

x = [1, 2, 3]
y = x[:]
z = copy.copy(x)
print(y)
print(z)
print(x is y)
print(x is z)
print(y is z)

a = [1, 2]
b = [3, a]
c = a
print(sys.getrefcount(x))

def f():
    t = a
    print(sys.getrefcount(x))

f()
