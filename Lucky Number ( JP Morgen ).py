
# a lucky number is a number those sum of its individual digits should be equal to one
# Question : Find if a num is a lucky number


def getSquareSum(ls):

    op = [x*x for x in ls]                          # gets the sum of the individual digits of the number
    return sum(op)

def luckyNumber(num,hsh=[]):

    hsh = {}                                        # adds the number into the list
    intLs = [int(i) for i in str(num)]              # converts the number into a list form with an int data type

    summedValue = getSquareSum(intLs)

    if summedValue == 1:
        return "lucky number",hsh
    else:
        if summedValue in ls:
            return "not a lucky number",hsh
        return luckyNumber(summedValue,hsh)

num = 86
print(luckyNumber(num))









