# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Time = O(n)
# Space = O(1)


def maxProfit(prices):

    # prices[0] and prices[1] are the first two prices
    l, r = 0, 1

    # initial profit count
    maxP = 0

    while r < len(prices):
        # if right is greater than left, then we can buy or left and right are the same and increment right
        if prices[r] > prices[l]:
            profit = prices[r] - prices[l]
            # max of previous profit i.e 4 and current profit i.e 5
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))
