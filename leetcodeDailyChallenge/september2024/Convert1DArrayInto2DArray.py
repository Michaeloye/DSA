# https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) > m * n or len(original) % (m *n) != 0:
            return []

        matrix = [[0 for _ in range(n)] for _ in range(m)] 

        COLS = len(matrix[0])

        r = 0
        c = 0
        for i in range(len(original)):
            matrix[r][c] = original[i]
            c += 1
            c %= COLS
            if c == 0:
                r += 1

        return matrix