# USING DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        # using DFS
        def dfs(r, c):
            if grid[r][c] == '0' or grid[r][c] == '2':
                return

            grid[r][c] = '2'
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            # check 4 corners of current pos
            for dr, dc in dirs:
                newRow = r + dr
                newCol = c + dc

                if newRow in range(ROWS) and newCol in range(COLS) and grid[newRow][newCol] == '1':
                    dfs(newRow, newCol)

        ans = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    dfs(r, c)
                    ans += 1

        return ans