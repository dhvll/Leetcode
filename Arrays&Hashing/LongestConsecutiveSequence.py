# https://leetcode.com/problems/longest-consecutive-sequence/


# Time = O(n)
# Space = O(n)


def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0

    for n in nums:
        # check if prefix of that element exist in set
        if (n - 1) not in numSet:
            length = 0
            # add element with length and increment length
            while (length + n) in numSet:
                length += 1
            # take max of longest and length
            longest = max(longest, length)
    return longest


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))
