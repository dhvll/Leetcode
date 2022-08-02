# https://leetcode.com/problems/search-insert-position/


def searchInsert(nums, target):

    left, right = 0, len(nums)

    while left < right:

        mid = left + (right - left) // 2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left


nums = [1, 3, 5, 6]
target = 5

print(searchInsert(nums, target))
