
def getHash(str):

    hsh = {}

    for char in str:
        if char not in hsh:
            hsh[char] = 1
        else:
            hsh[char] += 1

    return hsh


def groupAnagrams(strs):

    output = []

    for i in range(len(strs)):
        ls = []
        hsh = getHash(strs[i])
        for j in range(i,len(strs)):

            if strs[j][len(strs[j])-1] != "-":
                hsh2 = getHash(strs[j])

                if hsh == hsh2 :
                    ls.append(strs[j])
                    strs[j] = strs[j] + "-"


            else:
                continue
        if len(ls) >0:
            output.append(ls)
    return output

ls = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(ls))

