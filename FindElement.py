



#### Using Binary Search

def findElement(ls,lower,upper,target):

    mid = (upper + lower)//2

    if target < ls[mid]:
        upper = mid
        findElement(ls,lower,upper,target)

    if target > ls[mid]:
        lower = mid
        findElement(ls,lower,upper,target)

    if target == ls[mid]:
        index = ls.index(target)
        print(index)


ls = [2,5,6,8,9,23,33,39,43,55,65,78,877,986,1112]
target = int(input("Enter the number : "))
lower = 0
upper = len(ls)-1

if target not in ls:
    print("Not Found")
else:
    findElement(ls,lower,upper,target)

