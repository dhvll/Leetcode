# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Time = O(n)
# Space = O(n)


def lengthOfLongestSubstring(s):

    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        # Check if r is in set if yes remove and incr
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        # else add unique char to set
        charSet.add(s[r])
        # calculate the length
        res = max(res, r - l + 1)

    return res


s = ["abcabcbb", "bbbbb", "pwwkew", "aab", "dvdf"]
for i in s:
    print(lengthOfLongestSubstring(i))
