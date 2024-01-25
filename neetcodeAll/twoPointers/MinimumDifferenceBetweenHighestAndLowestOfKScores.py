# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums = sorted(nums, reverse=True)

        minimum = float('inf')
        for i in range(n):
            diff = i + k - 1
            if diff < n and nums[i] - nums[diff] < minimum:
                minimum = nums[i] - nums[diff]

        return minimum
