# https://leetcode.com/problems/minimum-increment-to-make-array-unique

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        res = 0

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                diff = nums[i - 1] - nums[i]
                nums[i] += diff + 1
                res += diff + 1
            elif nums[i - 1] == nums[i]:
                nums[i] += 1
                res += 1

        return res