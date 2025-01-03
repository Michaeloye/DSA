# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        t = 0
        b = ROWS - 1
        m1 = 0

        while t <= b:
            m1 = t + (b - t) // 2

            firstNum = matrix[m1][0]
            lastNum = matrix[m1][-1]

            if target < firstNum:
                b = m1 - 1
            elif target > lastNum:
                t = m1 + 1
            else:
                break
        
        l = 0
        r = COLS - 1

        while l <= r:
            m2 = l + (r - l) // 2

            if matrix[m1][m2] < target:
                r = m2 - 1
            elif matrix[m1][m2] > target:
                l = m2 + 1
            else:
                return True

        return False