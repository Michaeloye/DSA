# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        posCount = 0
        negCount = 0

        for num in nums:
            if num > 0:
                posCount += 1
            elif num < 0:
                negCount += 1
        
        return max(posCount, negCount)