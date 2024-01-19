# https://leetcode.com/problems/minimum-falling-path-sum

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        cache = {}

        def dfs(row, col):
            if row >= len(matrix):
                return 0
            if col < 0 or col == len(matrix):
                return float("inf")
            if (row, col) in cache:
                return cache[(row, col)]

            res = matrix[row][col] + min(
                dfs(row + 1, col - 1),
                dfs(row + 1, col),
                dfs(row + 1, col + 1)
            )

            cache[(row, col)] = res
            return res

        minVal = float('inf')
        for i in range(len(matrix)):
            minVal = min(minVal, dfs(0, i))

        return minVal
