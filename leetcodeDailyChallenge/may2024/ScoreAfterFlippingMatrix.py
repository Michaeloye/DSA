# https://leetcode.com/problems/score-after-flipping-matrix/

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        LEN_ROWS = len(grid)
        LEN_COLS = len(grid[0])

        for r in range(LEN_ROWS):
            if grid[r][0] == 0:
                for c in range(LEN_COLS):
                    grid[r][c] = 1 if grid[r][c] == 0 else 0

        for c in range(LEN_COLS):
            oneCount = 0
            for r in range(LEN_ROWS):
                oneCount += grid[r][c]
            if oneCount < LEN_ROWS - oneCount:
                for r in range(LEN_ROWS):
                    grid[r][c] = 1 if grid[r][c] == 0 else 0

        maxNum = 0
        for r in range(LEN_ROWS):
            for c in range(LEN_COLS):
                maxNum += grid[r][c] << (LEN_COLS - 1 - c)

        return maxNum