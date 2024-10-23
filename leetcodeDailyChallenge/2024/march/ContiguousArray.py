# https://leetcode.com/problems/contiguous-array/description/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeroes = 0
        ones = 0
        
        diffMap = {} # diiff -> index
        res = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes += 1
            else:
                ones += 1
            
            diff = ones - zeroes
            if diff not in diffMap:
                diffMap[diff] = i
            if ones == zeroes:
                res = ones + zeroes
            else:
                res = max(res, i - diffMap[diff])

        return res