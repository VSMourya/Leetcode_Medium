

#time - O(n)
#space - O(d) depth of the sub Lists


def productSum(arr,multiplier = 1):

    summation = 0

    for i in arr:
        if type(i) is list:
            summation += productSum(i,multiplier+1)
        else:
            summation += i

    return summation*multiplier

arr = [5,2,[7,-1],3,[6,[-13,8],4]]
print(productSum(arr))
