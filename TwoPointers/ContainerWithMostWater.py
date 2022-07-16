# https://leetcode.com/problems/container-with-most-water/

# Time = O(n)
# Space = O(1)
def maxArea(height):
    res = 0

    l, r = 0, len(height) - 1

    while l < r:
        area = (r - 1) * min(height[l], height[r])
        res = max(res, area)
        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        else:
            r -= 1
    return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
