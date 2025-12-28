# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] < 0:
                    ans += 1

        return ans

# STAIR CASE METHOD
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        m = len(grid[0])

        i = 0
        j = m - 1

        while i < n and j >= 0:
            if grid[i][j] < 0:
                ans += n - i
                j -= 1
            else:
                i += 1

        return ans