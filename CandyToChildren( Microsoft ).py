

def getCandiesToChildren(N,K):

    ls = [0]*K

    summation = K*(K+2)//2
    dummyNumber = N
    i = 0

    if N <= summation:
        while dummyNumber > i+1:
            ls[i] += i+1
            dummyNumber -= i+1
            i+=1
    else:
        while dummyNumber > (i+1)%K:
            ls[i%K] += i + 1
            dummyNumber -= (i+1)
            i+=1

    ls[i%K] += dummyNumber

    return ls

N = 12
K = 3

print(getCandiesToChildren(N,K))
