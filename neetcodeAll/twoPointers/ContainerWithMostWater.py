# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxRes = 0

        while l < r:
            minHeight = min(height[l], height[r])
            res = (r - l) * minHeight
            maxRes = max(maxRes, res)

            if height[l] == height[r]:
                l += 1
            elif height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
        return maxRes
