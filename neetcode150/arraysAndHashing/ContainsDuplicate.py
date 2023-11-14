# https://leetcode.com/problems/contains-duplicate/description/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setOfNums = set(nums)
        return len(nums) > len(setOfNums)
