# https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0

        curProd = 1
        l = 0
        for r in range(len(nums)):
            curProd *= nums[r]

            while l <= r and curProd >= k:
                curProd = curProd // nums[l]
                l += 1
            
            ans += r - l + 1
        return ans