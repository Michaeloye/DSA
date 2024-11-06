# https://leetcode.com/problems/find-if-array-can-be-sorted/

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def countBit(n):
            return bin(n).count("1")

        curMin = nums[0]
        curMax = nums[0]
        prevMax = float("-inf")

        for n in nums:
            if countBit(n) == countBit(curMin):
                curMin = min(curMin, n)
                curMax = max(curMax, n)
            else:
                if curMin < prevMax:
                    return False
                prevMax = curMax
                curMin = n
                curMax = n
        if curMin < prevMax:
            return False
        return True