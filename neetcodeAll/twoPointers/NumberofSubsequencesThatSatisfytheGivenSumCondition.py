# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        mod = (10 ** 9) + 7

        r = len(nums) - 1
        for l in range(len(nums)):
            while nums[l] + nums[r] > target and l <= r:
                r -= 1
            if l <= r:
                res += 2 ** (r - l)
                res %= mod

        return res