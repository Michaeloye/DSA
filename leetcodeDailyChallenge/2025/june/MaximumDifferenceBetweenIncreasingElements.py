# https://leetcode.com/problems/maximum-difference-between-increasing-elements/

# BRUTE FORCE
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    ans = max(ans, nums[j] - nums[i])

        return ans

# SLIDING WINDOW
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        n = len(nums)
        l = 0
        r = 1

        while r < n:
            if nums[r] <= nums[l]:
                l = r
            else:
                ans = max(ans, nums[r] - nums[l])
            r += 1
            
        return ans