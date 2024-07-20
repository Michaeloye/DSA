# https://leetcode.com/problems/lucky-numbers-in-a-matrix/

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        LEN_ROWS = len(matrix)
        LEN_COLS = len(matrix[0])
        colsMap = defaultdict(int)
        rowsMap = defaultdict(int)

        for r in range(LEN_ROWS):
            rowsMap[r] = float("inf")
            for c in range(LEN_COLS):
                rowsMap[r] = min(rowsMap[r], matrix[r][c])
                colsMap[c] = max(colsMap[c], matrix[r][c])
        
        minRows = set(rowsMap.values())
        maxCols = set(colsMap.values())

        intersection = minRows.intersection(maxCols)

        return list(intersection)
