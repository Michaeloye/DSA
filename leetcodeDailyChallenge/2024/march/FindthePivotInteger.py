# https://leetcode.com/problems/find-the-pivot-integer/description/

class Solution:
    def pivotInteger(self, n: int) -> int:
        totalSum = (n // 2) * (1 + n)
        currSum = 0
        if n == 1:
            return 1
        for i in range(n):
            currSum += i

            if currSum == sum(range(i, n + 1)):
                return i
        return -1