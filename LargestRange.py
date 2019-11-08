
def largestRange(array):

    bestRange = [0 ,0]
    longestLength = float("-inf")
    hsh = {}

    for i in array:
        if i not in hsh:
            hsh[i] = True

    for i in array:
        if hsh[i] == False:
            continue
        hsh[i] = True
        currentLongest = 1
        left = i- 1
        right = i + 1

        while left in hsh:
            hsh[left] = False
            left -= 1
            currentLongest += 1

        while right in hsh:
            hsh[right] = False
            right += 1
            currentLongest += 1

        if currentLongest > longestLength:
            longestLength = currentLongest
            bestRange = [left + 1, right - 1]

    return bestRange


array = [1,11,0,3,10,15,5,2,4,7,12,6]

print(largestRange(array))