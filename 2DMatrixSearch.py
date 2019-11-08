
def searchInSortedMatrix(matrix, target):
    row, col = 0, len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if target < matrix[row][col]:
            col -= 1
        elif target > matrix[row][col]:
            row += 1
        else:
            return [row, col]
    return [-1, -1]

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]


target = 423



print(searchInSortedMatrix(matrix,target))












