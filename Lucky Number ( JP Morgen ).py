
# a lucky number is a number those sum of its individual digits should be equal to one
# Question : Find if a num is a lucky number


def getSquareSum(ls):

    op = [x*x for x in ls]                          # gets the sum of the individual digits of the number
    return sum(op)

def luckyNumber(num,ls=[]):

    ls.append(num)                                  # adds the number into the list
    intLs = [int(i) for i in str(num)]              # converts the number into a list form with an int data type

    summedValue = getSquareSum(intLs)

    if summedValue == 1:
        return "lucky number",ls,ls[-1]
    else:
        if summedValue in ls:
            return "not a lucky number",ls
        return luckyNumber(summedValue,ls)

num = 86
print(luckyNumber(num))









