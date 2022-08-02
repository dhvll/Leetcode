# https://leetcode.com/problems/first-bad-version/


def firstBadVersion(n):

    left, right = 0, n

    while left < right:

        mid = left + (right - left) // 2

        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1
    return left


# isBadVersion is inbuilt API in leetcode

n = 5
print(firstBadVersion(n))
