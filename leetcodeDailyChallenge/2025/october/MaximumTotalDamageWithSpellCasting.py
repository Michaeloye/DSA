# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        unique = sorted(set(power))
        total = {}
        N = len(unique)
        for num in power:
            total[num] = num + total.get(num, 0)

        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]

            if i >= N:
                return 0
            
            skip = dfs(i + 1)

            j = i + 1
            while j < N and unique[j] - unique[i] < 3:
                j += 1
            take = total[unique[i]] + dfs(j)

            cache[i] = max(take, skip)
            return cache[i]

        return dfs(0)