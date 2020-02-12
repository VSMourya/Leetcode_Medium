
def maximalSquare(grid):
    if not grid or not grid[0]:
        return 0

    r = len(grid) + 1
    c = len(grid[0]) + 1
    m = [[0 for j in range(c)] for i in range(r)]

    mxIdx = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                m[i + 1][j + 1] = min(m[i][j], m[i][j + 1], m[i + 1][j]) + 1
                if m[i + 1][j + 1] > mxIdx:
                    mxIdx = m[i + 1][j + 1]

    return mxIdx**2


grid = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximalSquare(grid))