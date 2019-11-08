

def getAnswer(ls):

    hsh = {}
    sortedValues = []
    result = []

    for i in range(len(ls)):                                            #created hash
        if ls[i][0] not in hsh:
            hsh[ls[i][0]] = [ls[i][1]]
        else:
            hsh[ls[i][0]] += [ls[i][1]]

    for i in hsh.values():
        sortedValues.append([min(i),max(i),(min(i) + max(i))//2])       #min max avg

    for a,b in zip(hsh.keys(),sortedValues):                            #joined keys-values
        result.append((a,b))

    result.sort(key=lambda x: x[0])                                     #sorted by fruit name
    return result


ls = [["banana",150],["banana",250],["apple",120]]


print(getAnswer(ls))


