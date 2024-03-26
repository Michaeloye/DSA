# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] < 1:
                nums[i] = length + 1
        
        for n in nums:
            n = abs(n) - 1

            if n >= length:
                continue
            if nums[n] > 0:
                nums[n] *= -1

        for i in range(length):
            if nums[i] >= 0:
                return i + 1

        return length + 1