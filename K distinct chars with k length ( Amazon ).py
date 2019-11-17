




# Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

# Example 1:
#
# Input: s = "abcabc", k = 3
# Output: ["abc", "bca", "cab"]
# Example 2:
#
# Input: s = "abacab", k = 3
# Output: ["bac", "cab"]
# Example 3:
#
# Input: s = "awaglknagawunagwkwagl", k = 4
# Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
# Explanation:
# Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl"
# "wagl" is repeated twice, but is included in the output once.


def subStrings(string,k):

    ls = []

    for i in range(0,len(string)):
        if len(string[i:i+k]) == k and len(set(string[i:i+k])) == k:
            ls.append(string[i:i+k])

    return list(set(ls))


s = "awaglknagawunagwkwagl"
k = 4
print(subStrings(s,k))

