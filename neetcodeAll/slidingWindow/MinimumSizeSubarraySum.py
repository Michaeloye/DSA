# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums)
        l = 0
        subTotal = 0
        for r in range(len(nums)):
            subTotal += nums[r]

            while subTotal >= target:
                subTotal -= nums[l]
                res = min(res, r - l + 1)
                l += 1
            if r == len(nums) - 1 and l == 0:
                return 0

        return res
