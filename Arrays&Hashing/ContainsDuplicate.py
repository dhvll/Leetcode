# https://leetcode.com/problems/contains-duplicate/

# Time : O(n)
# Space : O(n)

def containDuplicate(nums):

    # Create a set to store the numbers
    hashset = set()

    for num in nums:

        # check if duplicate number is in hashset or not
        if num in hashset:
            return True

        # add number to hashset
        hashset.add(num)
    return False

nums = [1,2,3,3,4,5,3]
print(containDuplicate(nums))