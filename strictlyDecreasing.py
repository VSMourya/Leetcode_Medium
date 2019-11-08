

# Compare strings

def getAnswer(A,B):

    if not A or not B:
        return -1

    outputList = []
    lsA = []
    lsB = []

    for string in B:
        sortedString = "".join(sorted(string))
        countB = sortedString.count(sortedString[0])
        lsB.append(countB)


    for string in A:
        sortedString = "".join(sorted(string))
        countA = sortedString.count(sortedString[0])
        lsA.append(countA)

    for b in lsB:
        count=0
        for a in lsA:
            if a < b:
                count+=1
        outputList.append(count)

    return outputList


A = ["abcd","aabc","bd"]
B = ["aaa","aa"]

print(getAnswer(A,B))
