
def isPalindrome(string):
    left = 0
    right = len(string) - 1
    while left <= right:
        if string[left] != string[right]:
            return False
        left+=1
        right-=1
    return True

def isPrime(N):
    for i in range(1,N//2):
        if i != 1 and int(N%i) == 0:
            return False
    return True

def primePalindrome(N):
    if N == 1:
        return 2
    if N <= 3:
        return N
    elif N <= 5:
        return 5
    elif N <= 7:
        return 7
    elif N <= 11:
        return 11

    while True:
        if isPrime(N):
            if len(str(N)) == 1:
                return N
            elif isPalindrome(str(N)):
                return N
            else:
                N+=1
        else:
            N+=1

print(primePalindrome(5))



