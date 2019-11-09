
# asked in a google interview

def minDominoRotations(A,B):

    for i in range(1,7):
        if all(a==i or b==i for a,b in zip(A,B)):
            return min(len(A)-A.count(i),len(B) - B.count(i))
    return -1

A = [2,2,4,2,5,2,2]
B = [1,3,2,3,2,3,5]

print(minDominoRotations(A,B))



