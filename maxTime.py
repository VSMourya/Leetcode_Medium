

def getAnswer(s):

    hrs,mins = s.split(":")
    minutes,hours = [],[]

    for i,ints in enumerate(mins):
        if ints == "?":
            if i == 0:
                minutes.append("5")
                continue
            if i == 1:
                minutes.append("9")
                continue
        minutes.append(ints)

    for i in range(len(hrs)):
        if hrs[0] == "?" and hrs[1] == "?":
            hours.append("2")
            hours.append("3")
            break
        elif i==0:
            if hrs[i] == "?":
                if int(hrs[i+1]) < 4:
                    hours.append("2")
                    hours.append(hrs[i+1])
                    break
                else:
                    hours.append("1")
                    hours.append(hrs[i + 1])
                    break
            else:
                hours.append(hrs[i])
        elif i==1:
            if hrs[i] == "?":
                if hrs[i-1] =="0" or hrs[i-1] == "1":
                    hours.append("9")
                else:
                    hours.append("3")

    return ":".join(["".join(hours),"".join(minutes)])


    # OR
    #
    # r = list(s)
    # for i, c in enumerate(s):
    #     if c == '?':
    #         if i == 0:
    #             r[i] = '2' if s[1] == '?' or int(s[1]) <= 3 else '1'
    #         elif i == 1:
    #             r[i] = '3' if r[0] == '2' else '9'
    #         elif i == 3:
    #             r[i] = '5'
    #         elif i == 4:
    #             r[i] = '9'
    # return ''.join(r)

print(getAnswer("0?:??"))

