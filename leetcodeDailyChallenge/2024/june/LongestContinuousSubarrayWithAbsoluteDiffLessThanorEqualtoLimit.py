# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQ = deque() # monotonic increasing
        maxQ = deque() # monotonic decreasing
        l = 0
        res = 0

        for r in range(len(nums)):
            while minQ and nums[r] < minQ[-1]:
                minQ.pop()
            while maxQ and nums[r] > maxQ[-1]:
                maxQ.pop()

            minQ.append(nums[r])
            maxQ.append(nums[r])

            while maxQ[0] - minQ[0] > limit:
                if nums[l] == maxQ[0]:
                    maxQ.popleft()
                elif nums[l] == minQ[0]:
                    minQ.popleft()
                l += 1
            res = max(res, r - l + 1)
        return res
