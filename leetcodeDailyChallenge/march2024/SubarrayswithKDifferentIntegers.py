# https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = {}
        res = 0
        lFar = 0
        lNear = 0

        for r in range(len(nums)):
            count[nums[r]] = 1 + count.get(nums[r], 0)

            while len(count) > k:
                count[nums[lNear]] -= 1
                if count[nums[lNear]] == 0:
                    count.pop(nums[lNear])
                lNear += 1
                lFar = lNear

            while count[nums[lNear]] > 1:
                count[nums[lNear]] -= 1
                if count[nums[lNear]] == 0:
                    count.pop(nums[lNear])
                lNear += 1

            if len(count) == k:
                res += lNear - lFar + 1

        return res