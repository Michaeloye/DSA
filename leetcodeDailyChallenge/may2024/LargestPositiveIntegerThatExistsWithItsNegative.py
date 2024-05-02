# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()

        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[r] > -1 *nums[l]:
                r -= 1
            elif nums[r] < -1 * nums[l]:
                l += 1
            else:
                return nums[r]
        
        return -1