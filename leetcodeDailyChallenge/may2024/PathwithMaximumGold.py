# https://leetcode.com/problems/path-with-maximum-gold/

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        LEN_ROWS = len(grid)
        LEN_COLS = len(grid[0])

        def dfs(r, c, visited):
            if (min(r, c) < 0 or r == LEN_ROWS or c == LEN_COLS or grid[r][c] == 0 or (r, c) in visited):
                return 0

            res = grid[r][c]
            visited.add((r, c))

            res = max(res , grid[r][c] + dfs(r + 1, c, visited))
            res = max(res , grid[r][c] + dfs(r - 1, c, visited))
            res = max(res , grid[r][c] + dfs(r, c + 1, visited))
            res = max(res , grid[r][c] + dfs(r, c - 1, visited))
            
            visited.remove((r, c))
            return res
        res = 0
        for r in range(LEN_ROWS):
            for c in range(LEN_COLS):
                res = max(res, dfs(r, c, set()))
        
        return res