
# time - O(logn)
# space - O(1)

def missingNumberBinarySearch(arr):

    left = 0
    right = len(arr ) -1
    mid = 0

    while left +1 < right:

        mid = (left +right )//2

        if arr[right ] -arr[mid] != right -mid:
            left = mid
        elif arr[mid ] -arr[left] != mid -left:
            right = mid

    return arr[mid] + 1



arr = [1, 2, 3, 4, 5, 6, 8]
print(missingNumberBinarySearch(arr))


# OR


# time - O(n)
# space - O(1)

# for i in range(1,len(arr)):
#     if arr[i-1] != arr[i]-1:
#         print(arr[i]-1)

