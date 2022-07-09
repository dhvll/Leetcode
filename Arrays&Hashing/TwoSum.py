# https://leetcode.com/problems/two-sum/

# Time Complexity: O(n)
# Space Complexity: O(n)

def twoSum(nums, target):

    prevMap = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i

sums = [2,7,11,15]
target = 9
print(twoSum(sums, target))