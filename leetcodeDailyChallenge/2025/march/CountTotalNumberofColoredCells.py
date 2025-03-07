# https://leetcode.com/problems/count-total-number-of-colored-cells/

class Solution:
    def coloredCells(self, n: int) -> int:
        res = 1

        for i in range(n):
            res += 4 * i
        return res
