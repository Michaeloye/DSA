# https://leetcode.com/problems/range-sum-query-2d-immutable

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rowLen = len(matrix)
        colLen = len(matrix[0])
        self.prefixSum = [[0 for i in range(colLen + 1)]
                          for j in range(rowLen + 1)]

        for i in range(rowLen):
            sumUp = 0
            for j in range(colLen):
                sumUp += matrix[i][j]
                above = self.prefixSum[i][j + 1]
                self.prefixSum[i + 1][j + 1] = sumUp + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 = row1 + 1
        col1 = col1 + 1
        row2 = row2 + 1
        col2 = col2 + 1

        curr = self.prefixSum[row2][col2]
        above = self.prefixSum[row1 - 1][col2]
        left = self.prefixSum[row2][col1 - 1]
        topLeft = self.prefixSum[row1 - 1][col1 - 1]

        return curr - above - left + topLeft
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# THIS
# [
# [3,0,1,4,2],
# [5,6,3,2,1],
# [1,2,0,1,5],
# [4,1,0,1,7],
# [1,0,3,0,5]
# ]

# adding left prefix sum to sum of index above
# RESULT IN THIS PREFIX SUM
# [
# [0, 0, 0, 0, 0, 0],
# [0, 3, 3, 4, 8, 10],
# [0, 8, 14, 18, 24, 27],
# [0, 9, 17, 21, 28, 36],
# [0, 13, 22, 26, 34, 49],
# [0, 14, 23, 30, 38, 58]
# ]
