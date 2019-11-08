



def getNonDecreasing(nonDecreasing,A,hsh,mid):

    left = 0
    right = len(nonDecreasing) -1

    while len(nonDecreasing) < mid :
        if A[left] < A[right] and hsh[A[left]] > 0:
            nonDecreasing.append(A[left])
            hsh[A[left]] -=1
            left+=1
        else:
            nonDecreasing.append(A[right])
            hsh[A[left]] -=1

    return nonDecreasing



def getstrictlyIncreasing(strictlyIncreasing,A,mid,hsh):


    for i in range(1,N-1):
        if A[i] > strictlyIncreasing[-1]:
            strictlyIncreasing.append(A[i])
            hsh[A[i]] -=1
        else:
            continue


    if len(strictlyIncreasing) < mid  :
        strictlyIncreasing.append( strictlyIncreasing[-1] +1 )


    return strictlyIncreasing


def getAnswer(A,N):

    hsh = {}
    strictlyIncreasing = [A[0]]
    mid = N//2
    nonDecreasing = []

    for i in A :
        if i not in hsh:
            hsh[i] = 1
        else:
            hsh[i] += 1

    hsh[A[0]] -=1


    strictlyIncreasing = getstrictlyIncreasing(strictlyIncreasing,A,mid,hsh)

    nonDecreasing = getNonDecreasing(nonDecreasing,A,hsh,mid)


    output = strictlyIncreasing + nonDecreasing

    return output


A = [0,0,0,1,1,1,4,6,7,8,9]
N = len(A)


print(getAnswer(A,N))