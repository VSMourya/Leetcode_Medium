
# time - O(n)
# space - O(n)

# create a nxn bool matrix ( visited ) and assign False to each place
# traverse through each node in the matrix ( 2 for loops )
# for each node check if it is 1 and check if it is unvisited ( if visited = false )
#       if yes:
#            find its neighbour
#             explore neighbours
#       else:
#            move to another node

def getUnvisitedNeighborNodes(i,j,matrix,visited):

    unvisitedNeighborNodes = []

    if i > 0 and not visited[i-1][j]:
        unvisitedNeighborNodes.append([i-1,j])

    if i < len(matrix)-1 and not visited[i+1][j]:
        unvisitedNeighborNodes.append([i+1,j])

    if j >0 and not visited[i][j-1]:
        unvisitedNeighborNodes.append([i,j-1])

    if j < len(matrix)-1 and not visited[i][j+1]:
        unvisitedNeighborNodes.append([i,j+1])

    return unvisitedNeighborNodes

def checkForOtherNodes(i, j, matrix, visited, riverSizes):

    riverLength = 0
    discoverableNodes = [[i,j]]

    while discoverableNodes:

        currentNode = discoverableNodes.pop()
        i = currentNode[0]
        j = currentNode[1]

        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        riverLength+=1
        unvisitedNeighborNodes = getUnvisitedNeighborNodes(i,j,matrix,visited)
        for neighbor in unvisitedNeighborNodes:
            discoverableNodes.append(neighbor)

    if riverLength > 0:
        riverSizes.append(riverLength)

def riverSize(matrix):
    riverSizes = []

    visited = [[False for i in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j] or matrix[i][j]==0:
                continue
            checkForOtherNodes(i,j,matrix,visited,riverSizes)

    return riverSizes


matrix = [[1,0,0,1,1],
          [1,0,0,1,1],
          [0,0,0,1,0],
          [1,0,0,1,0],
          [1,0,0,1,1]]

print(riverSize(matrix))
