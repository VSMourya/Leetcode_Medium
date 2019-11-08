



def charCompressor(string):

    counterList = []

    left = 0
    right = 0

    while right < len(string):

        firstChar = string[left]
        secondChar = string[right]
        if firstChar == secondChar and right == len(string)-1:
            concat = string[left] + str(right - left+1)
            counterList.append(concat)
            break
        elif firstChar == secondChar:
            right+=1
        else:
            concat = string[left] + str(right-left)
            counterList.append(concat)
            left = right

    result = "".join(counterList)

    return result



string = "aaaabbccdcccdddddee"

print(charCompressor(string))