# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] < 0:
                    ans += 1

        return ans