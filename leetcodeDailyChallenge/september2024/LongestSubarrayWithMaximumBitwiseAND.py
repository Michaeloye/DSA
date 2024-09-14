# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxNum = max(nums)
        size = 0
        res = 0

        for num in nums:
            if num == maxNum:
                size += 1
            else:
                size = 0
            res = max(res, size)
        return res


# one pass solution
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # if num < curMax =>  num & curMax < curMax
        # if num == curMax => num & curMax == curMax
        # if num > curMax => num & curMax < curMax
        size = 0
        res = 0
        curMax = 0

        for num in nums:
            if num > curMax:
                curMax = num
                size = 1
                res = 0
            elif num == curMax:
                size += 1
            else:
                size = 0

            res = max(res, size)
        return res
