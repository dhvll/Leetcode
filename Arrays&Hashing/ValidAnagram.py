# https://leetcode.com/problems/valid-anagram/

# Time = O(n)
# Space = O(n)

def isAnalgram(s, t):

    if len((s)) != len((t)):
        return False

    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countS[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c,0):
            return False
    return True

s = "anagram"
t = "nagaram"

print(isAnagram(s, t))