
def mostCommonWord(paragraph ,banned):

    para = paragraph.split()
    purePara = []
    hsh = {}
    result = []

    for i in para:
        string = ""
        for j in i:
            if j.isalpha():
                string += j.lower()
        purePara.append(string)


    for i in purePara:
        if i not in hsh:
            hsh[i] = 1
        else:
            hsh[i] += 1


    for a, b in zip(hsh.keys(), hsh.values()):
        result.append([a, b])

    result.sort(key=lambda x: x[1])

    for i in range(len(result) - 1, 0, -1):
        popped = result.pop()
        if popped[0] not in banned:
            return popped[0]

    return result[-1][0]

if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(mostCommonWord(paragraph ,banned))