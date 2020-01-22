def printVertically(s):

    s = s.split()
    l = len(max(s, key=len))

    for i in range(len(s)):
        if len(s[i]) != l:
            s[i] +=" "*(l - len(s[i]))

    ls = list(zip(*s))

    newLs = []
    for i in ls:
        s = ""
        for j in reversed(i):
            if j == " " and not s:
                continue
            s += str(j)
        newLs.append("".join(reversed(s)))

    return newLs



