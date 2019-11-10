
# Q.Find number of islands

# code walkthrough :

# traverse through the whole matrix ( 2 for loops )
# if we find 1,
#    1. increment count value by 1 and replace its (matrix[i][j]) value with 0.
#    2. see if its (left,right,up,down) values are also 1
#       if yes, repeat the same on those values too ( recursive dfs)
# else:
#      ignore the value and move on to traverse the other values in the matrix


def callDFS(i,j,matrix):

    if i<0 or i>len(matrix)-1 or j < 0 or j > len(matrix[i])-1 or matrix[i][j] == 0:
        return

    matrix[i][j] = 0

    callDFS(i-1,j,matrix)
    callDFS(i+1,j,matrix)
    callDFS(i,j+1,matrix)
    callDFS(i,j-1,matrix)


def findIslands(matrix):

    numOfIslands = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                numOfIslands +=1
                callDFS(i,j,matrix)

    return numOfIslands



matrix = [[1 ,0 ,0 ,1 ,1],
         [1 ,0 ,0 ,1 ,1],
         [0 ,0 ,0 ,1 ,0],
         [1 ,1 ,1 ,0 ,0],
         [1 ,0 ,0 ,1 ,1]]


print(findIslands(matrix))