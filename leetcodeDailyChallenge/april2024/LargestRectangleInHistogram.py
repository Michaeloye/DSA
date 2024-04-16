# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
# not a daily problem but kind of a prerequisite for maximal rectangle problem

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                idx, val = stack.pop()
                area = (i - idx) * val
                start = idx
                maxArea = max(maxArea, area)
            stack.append((start, heights[i]))
        
        while stack:
            idx, val = stack.pop()
            area = (len(heights) - idx) * val 
            maxArea = max(maxArea, area)

        return maxArea