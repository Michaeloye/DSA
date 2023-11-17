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
        numsMap = {}  # val: index
        i = 0

        while i < len(nums):
            diff = target - nums[i]
            # if diff is not in numsMap add it to the numsMap
            if diff in numsMap:
                return [numsMap[diff], i]
            else:
                numsMap[nums[i]] = i

            i += 1
