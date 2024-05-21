# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        l = 0
        r = 1
        maxProfit = 0

        while r < n:
            if prices[r] < prices[l]:
                l = r
            else:
                currProfit = prices[r] - prices[l]
                maxProfit = max(maxProfit, currProfit)
            r += 1

        return maxProfit