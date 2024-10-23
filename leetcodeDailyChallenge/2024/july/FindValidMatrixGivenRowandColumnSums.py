# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ROWS = len(rowSum)
        COLS = len(colSum)

        res = [[0] * COLS for _ in range(ROWS)]
        
        # put all row sums in first column on each row
        for r in range(ROWS):
            res[r][0] = rowSum[r]
        
        # check if col sum requirement is met
        for c in range(COLS):
            curColSum = 0
            for r in range(ROWS):
                curColSum += res[r][c]
            
            # shift extra to next column
            r = 0
            while curColSum > colSum[c]:
                diff = curColSum - colSum[c]
                maxShift = min(diff, res[r][c])

                res[r][c] -= maxShift
                res[r][c + 1] += maxShift
                curColSum -= maxShift

                r += 1

        return res