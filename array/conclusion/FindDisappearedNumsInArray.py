from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        disappearedNums = []

        for i in range(1, numsLength + 1):
            if not (i in nums):
                disappearedNums.append(i)

        return disappearedNums


soln = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(soln.findDisappearedNumbers(nums))
