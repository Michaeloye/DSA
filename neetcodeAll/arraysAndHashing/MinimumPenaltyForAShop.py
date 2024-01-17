# https://leetcode.com/problems/minimum-penalty-for-a-shop/

# NON-OPTIMIZED SOLUTION
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # counting the number of Ns from the left
        # counting the number of Ys from the right
        # adding the two lists together
        # finding the index of the minimum value in the list
        # return the index

        length = len(customers)
        prefixN = [0] * (length + 1)
        postfixY = [0] * (length + 1)
        penalty = [0] * (length + 1)

        sumN = 0
        for i in range(1, length):
            if customers[i - 1] == "N":
                sumN += 1

            prefixN[i] = sumN
        prefixN[-1] = sumN

        sumY = 0
        for i in range(length - 1, -1, -1):
            if customers[i] == "Y":
                sumY += 1
            postfixY[i] = sumY

        for i in range(length + 1):
            penalty[i] = prefixN[i] + postfixY[i]

        return penalty.index(min(penalty))


# OPTIMIZED SOLUTION
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Instead of computing the minimum penalty, we can compute the maximum profit.
        ans = 0
        profit = 0
        maxProfit = 0

        for i, customer in enumerate(customers):
            profit += 1 if customer == 'Y' else -1
            if profit > maxProfit:
                maxProfit = profit
                ans = i + 1

        return ans
