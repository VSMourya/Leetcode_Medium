

#This code can be made even shorter but the primary focus remains the same
#The code should be readable and be more simple to understand :)


def isOutOfBounds(row,col,matrix):

    return row<0 or row>len(matrix)-1 or col<0 or col>len(matrix[row])-1


def checkPossibility(row,col,matrix):

    down = True
    right = True

    i = row
    while i < len(matrix):
        if matrix[i][col] == 1:
            down = False
        i+=1

    j = col
    while j < len(matrix[row]):
        if matrix[row][j] == 1:
            right = False
        j+=1

    return down and right


def getCount(matrix):

    count = 0
    row,col = 0,len(matrix)-1

    while not isOutOfBounds(row,col,matrix):

        if col != 0:
            if matrix[row][col] == 0:
                if checkPossibility(row,col,matrix):
                    count +=1
                    col-=1
                else:
                    col-=1
            else:
                row += 1
                col = len(matrix) - 1
        else:
            if matrix[row][col] == 0:
                if checkPossibility(row,col,matrix):
                    count += 1
                    row += 1
                    col = len(matrix) - 1
                else:
                    row += 1
                    col = len(matrix) - 1
            else:
                row += 1
                col = len(matrix) - 1

    return count


matrix = [[1,0,1],
          [1,0,0],
          [0,0,0]]

print(getCount(matrix))


