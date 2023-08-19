from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        j = 0
        nums = sorted(list(set(nums)), reverse=True)
        maxNum = nums[0]

        for i in nums:
            if (i < maxNum):
                maxNum = i
                j += 1

                if (j == 2):
                    return i
        return nums[0]


soln = Solution()
nums = [2, 2, 3, 1]
print(soln.thirdMax(nums))
