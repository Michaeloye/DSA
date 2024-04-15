# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        minMax = [0] * len(height)
        ans = 0

        maxVal = 0
        for i in range(1, len(height)):
            maxVal = max(maxVal, height[i - 1])
            leftMax[i] = maxVal

        maxVal = 0
        for i in range(len(height) - 2, -1, -1):
            maxVal = max(maxVal, height[i + 1])
            rightMax[i] = maxVal
        
        for i in range(len(height)):
            minMax[i] = min(leftMax[i], rightMax[i])
        
        print(minMax)
        for i in range(len(height)):
            diff = minMax[i] - height[i]
            ans += diff if diff >=0 else 0

        return ans