



def check(word,string):

    i = 0
    j = 0
    while i < len(word) and j < len(string)-1:
        if i == len(word)-1 and word[i] == string[j]:
            return True
        if word[i] == string[j]:
            i+=1
            j+=1
        else:
            j+=1
    return False


def longestWord(string,ls):

    longest = ""

    for word in ls:
        condition = check(word,string)
        if condition:
            if len(word) > len(longest):
                longest = word

    return longest

S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo"}

print(longestWord(S,D))

