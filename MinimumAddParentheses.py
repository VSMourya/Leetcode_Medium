

#Minimum Add to Make Parentheses Valid
#
# hint : the minimum add to make the parentheses valid is the number of elements left in the stack un-popped.



def minAddToMakeValid(string):
    stack = []
    openBrackets = ["("]

    for i in string:
        if i in openBrackets:
            stack.append(i)
        else:
            if stack and stack[-1] in openBrackets:
                stack.pop()
            else:
                stack.append(i)

    return len(stack)


string = "()))(("
print(minAddToMakeValid(string))