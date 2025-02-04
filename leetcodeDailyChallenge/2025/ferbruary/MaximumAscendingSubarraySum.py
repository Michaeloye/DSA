# https://leetcode.com/problems/maximum-ascending-subarray-sum/description/

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curSum = nums[0]
        ans = curSum

        for i in range(1, len(nums)):
            if (nums[i] > nums[i - 1]):
                curSum += nums[i]
            else:
                curSum = nums[i]

            ans = max(ans, curSum)

        return ans