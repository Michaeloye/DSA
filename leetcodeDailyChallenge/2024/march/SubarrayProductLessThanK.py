# https://leetcode.com/problems/subarray-product-less-than-k

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        res = 0
        l = 0

        for r in range(len(nums)):
            product *= nums[r]
            while l <= r and product >= k:
                product = product // nums[l]
                l += 1
            res += r - l + 1
        
        return res