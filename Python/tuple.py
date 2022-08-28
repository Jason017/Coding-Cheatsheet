a = [(1,2), (3,4)]
for i, j in a:
    print(i, j)


# Following code is going to run into type error:
#     for (i,j) in item:
# TypeError: cannot unpack non-iterable int object

# a = [(1,2), (3,4)]
# for item in a:
#     for i,j in item: 
#         print(i, j)