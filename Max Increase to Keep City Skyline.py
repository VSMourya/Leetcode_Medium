def maxIncreaseKeepingSkyline(grid):
    rowMaxs = []
    colMaxs = []

    # below while loop counts the maximums in the each column

    row, col = 0, 0
    mx = float("-inf")
    while row <= len(grid) - 1 and col <= len(grid[0]) - 1:
        if grid[row][col] > mx:
            mx = grid[row][col]

        if row == len(grid) - 1:
            colMaxs.append(mx)
            row = 0
            col += 1
            mx = float("-inf")
            continue
        row += 1

    # below while loop counts the maximums in the each row

    row, col = 0, 0
    mx = float("-inf")
    while row <= len(grid) - 1 and col <= len(grid[0]) - 1:
        if grid[row][col] > mx:
            mx = grid[row][col]

        if col == len(grid[0]) - 1:
            rowMaxs.append(mx)
            row += 1
            col = 0
            mx = float("-inf")
            continue
        col += 1

    resultSum = 0
    row, col = 0, 0

    # your number in the grid should be bounded to the min of the [ (left,right)values
    # and the (top,bottom)values ] in the grid

    while row <= len(grid) - 1 and col <= len(grid[0]) - 1:

        mn = min(rowMaxs[row], colMaxs[col])  # calculate the bounds
        resultSum += mn - grid[row][col]  # add it to the summation value

        if col == len(grid[0]) - 1:
            row += 1
            col = 0
            continue
        col += 1

    return resultSum

if __name__ == '__main__':
    grid = [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]
    print(maxIncreaseKeepingSkyline(grid))