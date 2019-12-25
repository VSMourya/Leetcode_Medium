#
# Input: "the sky is blue"
# Output: "blue is sky the"


def reverseWords(str):
    return " ".join(str.split()[::-1])


string = "the sky is blue"
print(reverseWords(string))
