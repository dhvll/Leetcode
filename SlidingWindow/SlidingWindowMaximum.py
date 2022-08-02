# https://leetcode.com/problems/sliding-window-maximum/


def maxSlidingWindow(nums, k):

    res = []
    l = r = 0
    q = collections.deque()

    while r < len(nums):

        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popLeft()

        if (1 + r) >= k:
            res.append(nums[q[0]])
            l += 1j
        r += 1
    return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(maxSlidingWindow(nums, k))
