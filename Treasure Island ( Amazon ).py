


def isInBounds(i,j,matrix):

    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])


def treasureIsland(m):

    matrix = [row[:] for row in m]


    directions = [[0,1],[0,-1],[1,0],[-1,0]]

    q = [((0, 0), 0)]

    matrix[0][0] = "D"        #since we have already included/initialized the node in the queue

    while q:

        (x,y),distance = q.pop(0)    # pop the first element of the array

        for dx,dy in directions:
            if isInBounds(x+dx,y+dy,matrix):
                if matrix[x+dx][y+dy] == "X":
                    return distance+1
                elif matrix[x + dx][y + dy] == "O":
                    matrix[x + dx][y + dy] = "D"                    # turn the visited nodes == "D"
                    q.append(((x + dx, y + dy), distance + 1))

    return -1



m = [['O', 'O', 'O', 'O'],
    ['D', 'O', 'D', 'O'],
    ['O', 'O', 'O', 'O'],
    ['O', 'D', 'D', 'X']]

print(treasureIsland(m))

