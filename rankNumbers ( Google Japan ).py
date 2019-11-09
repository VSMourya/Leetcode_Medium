# Question
# You are given an array A of distinct integers, you have to return another array B
# which transforms the first array such that the minimum element in the new array is 1
# and all the other elements maintain their relative ordering i.e.
# if A[i] > A[j] then it should also be that B[i] > B[j] and similarly for other elements.
# Also, the maximum number in B should be minimized.

# Input: [4, 2, 3, 7]
# Output: [3, 1, 2, 4]

# Input: [-4, -2, -3, -7]
# Output: [2, 4, 3, 1]
#-----------------------------------------------------------------------------------------------------------------------

# time - O(nlogn)
# space - O(n)

def getArray(inp):

    hsh = {}
    ls = []
    result = []

    arr = inp[:]
    print("original arr = ",arr)
    arr.sort()
    print("sorted arr = ",arr)
    tempNum = float("-inf")

    count = 0

    for i in range(len(arr)):
        if arr[i] > tempNum:
            tempNum = arr[i]
            count+=1
            ls.append(count)
        else:
            ls.append(count)

    print("required numbering =",ls)

    for a,b in zip(arr,ls):
        hsh[a] = b

    for a in inp:
        result.append(hsh[a])

    return "result = " + str(result)


if __name__ == '__main__':

    inp = [4, 2, 3, 7]
    print(getArray(inp))



