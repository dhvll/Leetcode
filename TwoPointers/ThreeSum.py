# https://leetcode.com/problems/3sum/

# Time = O(n^2)
# Space = O(n)


def threeSum(nums):

    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1

        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])k
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
    return res


nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))
