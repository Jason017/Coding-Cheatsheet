given_list = [1, 2, [3], [4, [5, 6,[7,[8]]]]]
def flattenList(given_list, final_list=[]):
    for x in given_list:
        if isinstance(x,list):
            flattenList(x)
        else:
            final_list.append(x)
    return final_list

print(flattenList(given_list))



matrix = [[1,2,3,4],[4,5,6,8]]
def transposeMatrix(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    return transposed

print(transposeMatrix(matrix))

matrix = [[1,2],[3,4],[5,6],[7,8],[9,10]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)

