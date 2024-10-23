# https://leetcode.com/problems/island-perimeter

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        LEN_ROW = len(grid)
        LEN_COL = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= LEN_ROW or c >= LEN_COL or grid[r][c] == 0:
                return 1
            
            if (r, c) in visited:
                return 0

            visited.add((r, c))
            perimeter = dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

            return perimeter

        for i in range(LEN_ROW):
            for j in range(LEN_ROW):
                if grid[i][j] == 1:
                    return dfs(i, j)
