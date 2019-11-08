

def hasSingleCycle(array):

    hsh = {}
    i = 0
    while i < len(array):
        if i not in hsh:
            hsh[i] = 0
        i+=1

    i = 0
    while i < len(array):
        if all(hsh.values()):
            break
        elif hsh[(i+array[i])%len(array)] > 1:
            return False
        else:
            hsh[(i+array[i])%len(array)] +=1
            i = (i+array[i])%len(array)

    return True


array = [2,2,-1]
print(hasSingleCycle(array))
