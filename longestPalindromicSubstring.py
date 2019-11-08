
def getLongestSubstring(left,right,string):

    while left >= 0 and right < len(string):
        if string[left] != string[right]:
            break
        left-=1
        right+=1

    return [left+1,right]


def longestPalindromicSubstring(string):

    currentLongest = [0,1]

    for i in range(1,len(string)):
        odd = getLongestSubstring(i-1,i+1,string)
        even = getLongestSubstring(i-1,i,string)

        longest = max(odd,even,key=lambda x:x[1]-x[0])
        currentLongest = max(currentLongest,longest,key=lambda x:x[1]-x[0])

    return string[currentLongest[0]:currentLongest[1]]


string = "09896"

print(longestPalindromicSubstring(string))