# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        numCount = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(nums)):
            numCount[nums[r]] += 1

            while numCount[nums[r]] > k:
                numCount[nums[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res