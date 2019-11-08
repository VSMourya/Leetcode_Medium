



def ThreeSum(array,targetSum):
    array.sort()

    a = []
    for i in range(0,len(array)):
        left = i+1
        right = len(array) - 1

        while (left<right):

            currentSum = array[i] + array[left] + array[right]

            if currentSum == targetSum:
                a.append([array[i],array[left],array[right]])
                left +=1
                right-=1
            elif currentSum < targetSum:
                left+=1
            elif currentSum > targetSum:
                right-=1

    return a




nums = [2,34,5,6,4,0,1]
targetSum = 9
print(ThreeSum(nums,targetSum))