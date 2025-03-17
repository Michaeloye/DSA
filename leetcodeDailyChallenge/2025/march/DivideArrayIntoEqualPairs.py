# https://leetcode.com/problems/divide-array-into-equal-pairs

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        pairs = {}

        for n in nums:
            pairs[n] = 1 + pairs.get(n, 0)

        for count in pairs.values():
            if count % 2 == 1:
                return False
        return True