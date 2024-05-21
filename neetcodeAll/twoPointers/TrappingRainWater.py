# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        maxLeft = height[l]
        maxRight = height[r]

        res = 0
        while l < r:
            if maxLeft < maxRight:
                diff = maxLeft - height[l]
                res += diff if diff > 0 else 0
                l += 1
                maxLeft = max(maxLeft, height[l])
            else:
                diff = maxRight - height[r]
                res += diff if diff > 0 else 0
                r -= 1
                maxRight = max(maxRight, height[r])
        return res