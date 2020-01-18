
def buildGrid(queens, king):
    grid = [ [0 for i in range(8)] for j in range(8)]

    for (a ,b) in queens:
        grid[a][b] = 1

    return grid

def isInBounds(grid,i,j):
        return i >= 0 and i < 8 and j < 8 and j >= 0


def queensAttacktheKing(queens, king):

    grid = buildGrid(queens, king)
    result = []
    row,col = king[0],king[1]

    while isInBounds(grid, row, col):      #isInBoundsLeft
        if grid[row][col] == 1:
            result.append([row,col])
            break
        col -=1

    row,col = king[0],king[1]
    while isInBounds(grid, row, col):     #isInBoundsRight
        if grid[row][col] == 1:
            result.append([row, col])
            break
        col += 1

    row,col = king[0],king[1]
    while isInBounds(grid, row, col):     #isInBoundsTop
        if grid[row][col] == 1:
            result.append([row, col])
            break
        row-=1

    row,col = king[0],king[1]
    while isInBounds(grid, row, col):    #isInBoundsDown
        if grid[row][col] == 1:
            result.append([row, col])
            break
        row += 1

    row,col = king[0],king[1]
    while isInBounds(grid, row, col):  #isInBoundsLeftUp
        if grid[row][col] == 1:
            result.append([row, col])
            break
        row -= 1
        col -= 1

    row, col = king[0], king[1]
    while isInBounds(grid, row, col):   #isInBoundsLeftDown

        if grid[row][col] == 1:
            result.append([row, col])
            break
        row += 1
        col -= 1

    row,col = king[0],king[1]
    while isInBounds(grid, row, col):    #isInBoundsRightUp
        if grid[row][col] == 1:
            result.append([row, col])
            break
        row -= 1
        col += 1

    row, col = king[0], king[1]
    while isInBounds(grid, row, col):  #isInBoundsRightDown

        if grid[row][col] == 1:
            result.append([row, col])
            break
        row += 1
        col += 1

    return result

queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]]
king = [3,4]

print(queensAttacktheKing(queens,king))