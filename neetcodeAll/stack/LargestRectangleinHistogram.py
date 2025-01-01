# https://leetcode.com/problems/largest-rectangle-in-histogram/

# brute force approach
# O(n^2)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0

        for i in range(len(heights)):
            r = i

            while r < len(heights) and heights[r] >= heights[i]:
                r += 1
            
            l = i
            while l >= 0 and heights[l] >= heights[i]:
                l -= 1

            l += 1
            r -= 1

            h = heights[i]
            w = r - l + 1
            area = h * w
            ans = max(ans, area)
            
        return ans


# optimized solution
# O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (idx, height)
        ans = 0

        for i, h in enumerate(heights):
            
            start = i

            while stack and h < stack[-1][1]:
                idx, sh = stack.pop()
                w = i - idx
                area = w * sh
                ans = max(ans, area)
                start = idx
            
            stack.append((start, h))
        
        for i, h in stack:
            area = (len(heights) - i) * h
            ans = max(ans, area)
        return ans