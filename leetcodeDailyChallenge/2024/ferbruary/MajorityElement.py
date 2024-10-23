# https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mid = int(len(nums) // 2)
        numsMap = {}

        for num in nums:
            numsMap[num] = 1 + numsMap.get(num, 0)
            if numsMap[num] > mid:
                return num
