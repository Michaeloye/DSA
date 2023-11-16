# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        setNums = set(nums)

        for i in setNums:
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []


# OPTIMIZED


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        i = 0

        while i < len(nums):
            if target - nums[i] in numsMap:
                return [numsMap[target - nums[i]], i]
            else:
                numsMap[nums[i]] = i

            i += 1
