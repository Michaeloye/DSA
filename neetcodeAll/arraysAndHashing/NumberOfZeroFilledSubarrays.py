# https://leetcode.com/problems/number-of-zero-filled-subarrays/

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        numOfPrevZeroes = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                numOfPrevZeroes += 1
            else:
                numOfPrevZeroes = 0
                continue

            ans += numOfPrevZeroes

        return ans
