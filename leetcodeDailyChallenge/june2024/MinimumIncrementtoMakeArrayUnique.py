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

# another solution
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0

        for num in range(len(nums) + max(nums)):
            if count[num] > 1:
                tmp = count[num]
                count[num] = 1
                count[num + 1] += tmp - 1
                res += tmp - 1
        return res