# https://leetcode.com/problems/find-pivot-index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prevSum = 0
        totalSum = 0

        for n in nums:
            totalSum += n

        for i, n in enumerate(nums):

            rightSum = totalSum - n - prevSum

            if rightSum == prevSum:
                return i

            prevSum += n

        return -1
