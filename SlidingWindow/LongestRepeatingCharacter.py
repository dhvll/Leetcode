# https://leetcode.com/problems/longest-repeating-character-replacement/


def characterReplacement(s, k):

    # To store frequency of character
    count = {}
    res = 0
    l = 0

    for r in range(len(s)):

        count[s[r]] = 1 + count.get(s[r], 0)

        # check if valid or not
        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)
    return res


s = "ABAB"
k = 2
print(characterReplacement(s, k))
