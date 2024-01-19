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

# DP SOLUTION


def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    N = len(matrix)

    for r in range(1, N):
        for c in range(N):
            left = matrix[r - 1][c - 1] if c > 0 else float("inf")
            mid = matrix[r - 1][c]
            right = matrix[r - 1][c + 1] if c < N - 1 else float("inf")

            matrix[r][c] = matrix[r][c] + min(left, mid, right)

    return min(matrix[-1])
