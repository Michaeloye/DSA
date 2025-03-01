# https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        zeroCount = 0

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

            if nums[i] > 0:
                ans.append(nums[i])
            elif nums[i] == 0:
                zeroCount += 1

        if nums[i + 1]:
            ans.append(nums[i + 1])
        else:
            zeroCount += 1

        ans = ans + ([0] * zeroCount)
        return ans
