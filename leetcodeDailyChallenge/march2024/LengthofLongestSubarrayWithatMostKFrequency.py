# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = {}
        l = 0
        ans = 0

        for r in range(len(nums)):
            curr = nums[r]
            count[curr] = 1 + count.get(curr, 0)

            while l <= r and count[curr] > k:
                count[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans