# https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        durCost = {1: costs[0], 7: costs[1], 30: costs[2]}
        cache = {}

        def dfs(i):
            if i == len(days):
                return 0
            if i in cache:
                return cache[i]

            cache[i] = float("inf")

            for dur, cost in durCost.items():
                j = i

                while j < len(days) and days[j] < days[i] + dur:
                    j += 1

                cache[i] = min(cache[i], dfs(j) + cost)

            return cache[i]

        return dfs(0)
