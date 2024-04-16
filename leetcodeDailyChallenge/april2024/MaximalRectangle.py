# https://leetcode.com/problems/maximal-rectangle/description/

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def calcMaxHistArea(numbers):
            maxArea = 0
            stack = []

            for i in range(len(numbers)):
                newIdx = i
                while stack and stack[-1][1] > numbers[i]:
                    idx, val = stack.pop()
                    area = (i - idx) * val
                    newIdx = idx
                    maxArea = max(maxArea, area)
                stack.append((newIdx, numbers[i]))
            while stack:
                idx, val = stack.pop()
                area = (len(numbers) - idx) * val
                maxArea = max(maxArea, area)     
            return maxArea

        row = [0] * len(matrix[0])

        maxRectangle = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if int(matrix[i][j]) == 0:
                    row[j] = 0
                else:
                    row[j] += int(matrix[i][j])
            maxRectangle = max(maxRectangle, calcMaxHistArea(row))

        return maxRectangle