
def getUniqueYears(string):

    ls = string.split()
    ints = []
    result = []

    for char in ls:

        if not char.isalpha() and len(char) > 4:
            ints.append(char[:10])

    for char in ints:
        date,month,year = char.split("-")
        if int(year) not in result:
            result.append(int(year))

    return len(result)





string = "The UN found that world war 2 ended on 02-09-1945, the UN was established on 24-05-1947"

print(getUniqueYears(string))
