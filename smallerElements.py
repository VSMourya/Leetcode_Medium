
def countNums(array):

    ls = []

    for i in range(0,len(array)):

        count = 0
        pointer = len(array)-1

        while ( pointer > i):

            if array[i] > array[pointer]:
                count+=1
                pointer-=1
            elif array[i] < array[pointer]:
                pointer -=1
            elif array[i] == array[pointer]:
                pointer-=1
        ls.append(count)

    return ls

nums = [5,2,6,1,1,5]
print(countNums(nums))
