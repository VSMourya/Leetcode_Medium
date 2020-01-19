


def isInBounds(row,col,matrix):
    return row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0])


def numIslands(matrix):

    islands = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
             if matrix[i][j] == 1:
                length = explore(i,j,matrix)
                islands.append(length)

    return islands

def explore(i,j,matrix):

    directions = [[0,1],[0,-1],[1,0],[-1,0]]
    nodesToExplore = [[(i,j),1]]
    while nodesToExplore:

        (row,col),sm = nodesToExplore.pop(0)
        matrix[row][col] = "#"

        for dx,dy in directions:
            if isInBounds(row+dx,col+dy,matrix):
                if matrix[row+dx][col+dy] == 1:
                    nodesToExplore.append([(row+dx,col+dy),sm+1])

    return sm

matrix = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0]
]
print(numIslands(matrix))
