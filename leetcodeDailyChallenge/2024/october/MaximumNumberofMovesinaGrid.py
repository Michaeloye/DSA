# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [(-1, 1), (0, 1), (1, 1)]
        memo = {}

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]

            maxCount = 0
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if nr >= 0 and nr < ROWS and nc >= 0 and nc < COLS and grid[nr][nc] > grid[r][c]:
                    maxCount = max(maxCount, dfs(nr, nc) + 1)

            memo[(r, c)] = maxCount
            return maxCount

        ans = 0
        for r in range(ROWS):
            ans = max(ans, dfs(r, 0))
        
        return ans