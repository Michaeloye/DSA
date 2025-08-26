# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiagonal = 0
        maxArea = 0

        for length, breadth in dimensions:
            diagonal = (length ** 2 + breadth ** 2) ** 0.5
            if diagonal == maxDiagonal:
                maxArea = max(maxArea, length * breadth)
            elif diagonal > maxDiagonal:
                maxArea = length * breadth
                maxDiagonal = diagonal
        return maxArea