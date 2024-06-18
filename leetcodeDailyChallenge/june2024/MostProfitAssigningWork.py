# https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ans = 0

        jobs = list(zip(difficulty, profit))
        jobs.sort()

        maxProfit = []
        maxSeen = 0
        for d, p in jobs:
            maxSeen = max(maxSeen, p)
            maxProfit.append((d, maxSeen))

        for w in worker:
            left, right = 0, len(difficulty) - 1
            while left <= right:
                mid = (left + right) // 2
                if maxProfit[mid][0] <= w:
                    left = mid + 1
                else:
                    right = mid - 1
            ans += maxProfit[right][1] if right >= 0 else 0
        return ans