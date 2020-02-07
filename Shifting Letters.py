def shiftingLetters(S,shifts):
    for i in range(len(shifts) - 1)[::-1]:
        shifts[i] += shifts[i + 1]

    newStr = ""

    for i, value in enumerate(S):
        newStr += chr((ord(value) + shifts[i] - 97) % 26 + 97)

    return newStr

if __name__ == '__main__':
    S = "abc"
    shifts = [3, 5, 9]
    print(shiftingLetters(S,shifts))