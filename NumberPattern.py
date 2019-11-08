
def getMinNumberForPattern(string):
    n = len(string)
    if (n > 8):
        return "-1"
    result = [None] * (n + 1)
    counter = 1

    for i in range(n + 1):
        if (i == n or string[i] == 'I'):
            for j in range(i - 1, -2, -1):
                result[j + 1] = int('0' + str(counter))
                counter += 1
                if(j >= 0 and string[j] == 'I'):
                    break


            break
    return result

inp = ["IDD"]

for Input in inp:
    print(*(getMinNumberForPattern(Input)))



