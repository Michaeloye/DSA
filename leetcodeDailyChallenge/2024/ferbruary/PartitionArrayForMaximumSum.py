# https://leetcode.com/problems/partition-array-for-maximum-sum

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        cache = {}
        def dfs(i):
            if i >= len(arr):
                return 0
            if i in cache:
                return cache[i]

            curMax = 0
            res = 0

            for j in range(i, min(len(arr), i + k)):
                curMax = max(curMax, arr[j])
                windowSize = j - i + 1
                res = max(res, dfs(j + 1) + (curMax * windowSize))

            cache[i] = res
            return cache[i]

        return dfs(0)