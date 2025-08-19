# https://leetcode.com/problems/number-of-zero-filled-subarrays/

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        no_of_prev_zeroes = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                no_of_prev_zeroes += 1
            else:
                no_of_prev_zeroes = 0
            
            ans += no_of_prev_zeroes

        return ans
