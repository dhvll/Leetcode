# https://leetcode.com/problems/trapping-rain-water/


def trap(height):

    if not height:
        return 0

    l, r = 0, len(height) - 1

    max_left, max_right = height[l], height[r]
    res = 0
    while l < r:
        if max_left < max_right:
            l += 1
            max_left = max(max_left, height[l])
            res += max_left - height[l]
        else:
            r -= 1
            max_right = max(max_right, height[r])
            res += max_right - height[r]
    return res


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height))
