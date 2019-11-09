


def wateringFlowers(arr,capacity1,capacity2):

    n = len(arr)//2

    cap1 = capacity1
    cap2 = capacity2

    refills = 2


    for i in range(0,n):

        if arr[i] < cap1:
            cap1 = cap1 - arr[i]
        else:
            refills +=1
            cap1 = capacity1
            cap1 = cap1 - arr[i]

    if len(arr)%2 == 0:
        n = n - 1

    for j in range(len(arr)-1,n,-1):

        if arr[j] < cap2:
            cap2 = cap2 - arr[j]
        else:
            refills+=1
            cap2 = capacity2
            cap2 = cap2 - arr[j]

    if len(arr)%2 == 1:
        if cap1+cap2 < arr[n]:
            refills+=1


    return refills

array = [2,4,5,1,2]

print(wateringFlowers(array,5,7))

