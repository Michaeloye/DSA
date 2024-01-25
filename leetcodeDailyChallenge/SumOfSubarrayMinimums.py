# https://leetcode.com/problems/sum-of-subarray-minimums/

# MEMORY LIMIT EXCEEDED
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        N = len(arr)

        def subseq(idx, end, minimumSum):
            if idx >= N:
                return minimumSum
            if end > N:
                idx += 1
                end = idx + 1

            selection = arr[idx:end]
            minimumSum += min(selection) if len(selection) > 0 else 0
            return subseq(idx, end + 1, minimumSum)

        minimum = subseq(0, 1, 0)
        return minimum % (10**9 + 7)
