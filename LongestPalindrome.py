
def isPalindrome(num):

    left  = 0
    right = len(num ) -1

    for i in range(len(num)):
        if num[left] == num[right]:
            if left >= right:
                break
            left +=1
            right -=1
            print("left = " + str(left))
            print("right = " + str(right))
            continue
        else:
            return False

    return True

word = input()


if isPalindrome(word) == True:

    print(word)

elif isPalindrome(word) == False:
    print()
