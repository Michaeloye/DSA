# https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 0
        r = 0
        total = 0
        res = 0

        while r < len(nums):
            total += nums[r]

            while nums[r] * (r - l + 1) > total + k:
                total -= nums[l]
                l += 1

            res = max(res, r - l + 1)
            r += 1
        return res
