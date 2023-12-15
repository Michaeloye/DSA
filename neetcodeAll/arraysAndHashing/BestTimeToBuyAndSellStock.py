# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for i in prices[1:]:
            if i < buy:
                buy = i
            else:
                profit += i - buy
                buy = i
        return profit
