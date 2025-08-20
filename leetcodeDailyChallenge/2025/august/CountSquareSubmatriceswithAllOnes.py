# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}
        def dfs(r, c):
            if r == ROWS or c == COLS or matrix[r][c] == 0:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]

            length = 1 + min(
                dfs(r + 1, c),
                dfs(r + 1, c + 1),
                dfs(r, c + 1)
            )

            cache[(r, c)] = length
            return length
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res += dfs(r, c)
        return res