

#This code can be made even shorter but the primary focus remains the same
#The code should be readable and be more simple to understand :)

def isOutOfBounds(matrix,row,col):

    return row < 0 or row > len(matrix)-1 or col < 0 or col > len(matrix)-1

def checkPossibility(matrix,row,col):

    possibilityDown = True
    possibilityRight = True

    while not isOutOfBounds(matrix,row,col):
        if matrix[row][col] == 1:
            possibilityRight = False
            break
        col += 1

    while not isOutOfBounds(matrix,row,col):
        if matrix[row][col] == 1:
            possibilityDown = False
            break
        row += 1


    if possibilityDown and possibilityRight:
        return True
    else:
        return False

def getCount(matrix):

    row,col = 0,len(matrix)-1
    count = 0

    while not isOutOfBounds(matrix,row,col):

        if col != 0:
            if matrix[row][col] == 0:
                if checkPossibility(matrix,row,col):
                    count+=1
                    col-=1
                else:
                    col-=1
            else:
                row+=1
                col = len(matrix)-1
        else:
            if matrix[row][col] == 1:
                row += 1
                col = len(matrix) - 1
            else:
                count+=1
                row += 1
                col = len(matrix) - 1

    return count

matrix = [[1,0,1],
          [1,0,0],
          [0,0,0]]

#matrix is an nxn matrix

print(getCount(matrix))


