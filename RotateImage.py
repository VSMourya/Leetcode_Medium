


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


for i in range(0, len(matrix)):
    temp = []
    for j in range(0, len(matrix)):
        temp.append(matrix[j][i])
    matrix.append(temp[::-1])

    matrix.remove(matrix[0])


print(matrix)

