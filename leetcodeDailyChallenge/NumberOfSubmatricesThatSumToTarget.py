# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rowLen = len(matrix)
        colLen = len(matrix[0])

        ans = 0

        submatrixSum = [[0] * colLen for _ in range(rowLen)]
        
        for i in range(rowLen):
            for j in range(colLen):
                leftSum = submatrixSum[i][j - 1] if j > 0 else 0
                topSum = submatrixSum[i - 1][j] if i > 0 else 0
                topLeftSum = submatrixSum[i - 1][j - 1] if i > 0 and j > 0 else 0

                submatrixSum[i][j] = matrix[i][j] + topSum + leftSum - topLeftSum


        for r1 in range(rowLen):
            for r2 in range(r1, rowLen):
                count = defaultdict(int)
                count[0] = 1
                for c in range(colLen):
                    curSum = submatrixSum[r2][c] - (
                    submatrixSum[r1 - 1][c] if r1 > 0 else 0
                    )
                    diff = curSum - target
                    ans += count[diff]
                    
                    count[curSum] += 1
        
        return ans