# https://leetcode.com/problems/top-k-frequent-elements


# Time = O(n)
# Space = O(n)

def topKFrequent(nums, k):

    count = {}

    # index will count of elements , numbers will be size of array +1
    freq = [[] for i in range(len(nums) + 1)]

    # count every value in num and how many times it occurs
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    # n occurs c times       
    for n,c in count.items():
        freq[c].append(n)

    res = []
    #  iterate from last to first because we want to get less frequent elements first
    for i in range(len(freq) -1, 0,-1):
        # if there are enough elements in the list then add them to the result.
        for n in freq[i]:
            # n is value which appears most frequently
            res.append(n)
            # check length of res and k if equal then return res
            if len(res) == k:
                return res


nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))