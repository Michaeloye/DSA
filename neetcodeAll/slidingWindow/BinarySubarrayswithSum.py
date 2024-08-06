# https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        def helper(target):
            if target < 0:
                return 0

            l = 0
            c = 0
            res = 0

            for r in range(len(nums)):
                c += nums[r]

                while c > target:
                    c -= nums[l]
                    l += 1

                res += r - l + 1
            return res
        return helper(goal) - helper(goal - 1)