


def getCountSet(str):

    ls = list(str)

    hsh = {}
    for i in ls:
        if i not in hsh:
            hsh[i] = 1
        else:
            hsh[i] += 1

    return hsh

def ransomNote(ransomNote,magazine):

        setA = getCountSet(ransomNote)
        setB = getCountSet(magazine)

        for i in ransomNote:
            if i in setB:
                if setB[i] < setA[i]:
                    return False
            else:
                return False
        return True

if __name__ == '__main__':
    a = "aa"
    b = "ab"
    print(ransomNote(a,b))