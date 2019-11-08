
def largestSumRange(arr,target):

    longestRange = [-1,-1]

    left = 0
    right = 1

    temp = arr[left]

    while right != left:
        if temp < target:
            temp += arr[right]
            right += 1
        elif temp > target:
            temp -= arr[left]
            left += 1
        else:
            range = [left,right-1]
            mx = max(longestRange,range,key=lambda x:x[1]-x[0])
            longestRange = mx
            break
    return longestRange


arr = [1,1,2,3,5,6,7,98]

target = 10
print(largestSumRange(arr,target))