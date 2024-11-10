# https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        res = float("inf")
        bits = [0] * 32
        l = 0

        def bitsUpdate(bits, n, diff):
            for i in range(32):
                if n & (1 << i):
                    bits[i] += diff

        def bitsToInt(bits):
            res = 0
            for i in range(32):
                if bits[i]:
                    res += (1 << i)
            return res

        for r in range(len(nums)):
            # set bits
            bitsUpdate(bits, nums[r], 1)

            # calculate the cur or
            curOr = bitsToInt(bits)

            # shift left pointer until condition is not met
            while l <= r and curOr >= k:
                res = min(res, r - l + 1)
                # unset bits
                bitsUpdate(bits, nums[l], -1)
                curOr = bitsToInt(bits)
                l += 1
        return -1 if res == float("inf") else res
