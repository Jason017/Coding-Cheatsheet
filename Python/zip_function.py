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
xx = list(zip(x))
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


print("Example 5:")
a=[1,2,3]
b=[4,5,6,7]
c=[8,9,10,11,12]
zz=list(zip(a,b,c))
print(zz)
x,y,z=zip(*zz)
print(x)
print(y)
print(z)


print("Example 6:")
data1 = [450, 500, 300, 100]
data2 = [6,2,3,4]
zp = sorted(list(zip(data1, data2)), key = lambda x: x[0], reverse = True)
for k,v in enumerate(zp):
    print(k,v)

print("Output second value: ", min(zp, key = lambda x: x[0])[1])
print("Output value: ", min(zp, key = max))

print()
zp2 = list(zip(data1, data2))
print(zp2)
print(min(zp2, key=min))


print("Example 7:")
x = range(4)
nums = [-1, 2, 1, -4]
dct = dict(zip(x,nums))

print("Convert a list to a dictionary", dct)
