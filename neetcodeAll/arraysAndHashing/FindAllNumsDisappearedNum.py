# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        numsSet = set(nums)
        disappearedNums = []

        for i in range(1, n + 1):
            if i not in numsSet:
                disappearedNums.append(i)

        return disappearedNums
