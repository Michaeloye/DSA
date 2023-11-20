# https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def combination(n, r):
            nFactorial = 1
            rFactorial = 1
            n_rFactorial = 1

            for i in range(1, n + 1):
                nFactorial *= i

            for i in range(1, r + 1):
                rFactorial *= i
            
            for i in range(1, (n-r) + 1):
                n_rFactorial *= i

            return  nFactorial//(rFactorial * n_rFactorial)
        
        result = []
        column = 0

        for i in range(numRows):
            rowRes = []
            column += 1
            for j in range(column):
                rowRes.append(combination(i,j))
            result.append(rowRes)
        
        return result
