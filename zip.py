print("Example 1:")
x = [1,2,3,4,5]
y = ['a','b','c','d']
xy = list(zip(x,y))
print(xy)
for a,b in zip(x,y):
    print(a)
    print(b)


print("Example 2:")
x = [1,2,3,4,5]
xx = zip(x)
print(xx)
for a in zip(x):
    print(a)
for a in zip(x):
    print(a[0])


print("Example 3:")
x = [[1,2,3,4],['a','b','c'],[7,8,9]]
y = list(zip(*x))
print(y)
for a in y:
    print(a)
for a,b,c in zip(*x):
    print(a)
    print(b)
    print(c)


print("Example 4:")
import numpy as np
a = [1,2,3,4,5]
b = (1,2,3,4,5)
c = np.arange(5)
d = "zhang"
z = list(zip(a,b,c,d))
print(z)


print("Example 4:")
a=[1,2,3]
b=[4,5,6,7]
c=[8,9,10,11,12]
zz=list(zip(a,b,c))
print(zz)

x,y,z=zip(*zz)
print(x)
print(y)
print(z)

