# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            cur = 0
            for num in nums:
                cur += 1 if num >= i else 0
            if cur == i:
                return i

        return -1