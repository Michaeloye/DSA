# https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        maxRank = max(ranks)
        l = 1
        r = maxRank * (cars ** 2)
        ans = 0

        def isValid(t):
            count = 0

            for r in ranks:
                n = int((t // r)** 0.5)
                count += n
            
            return True if count >= cars else False

        while l <= r:
            m = l + (r - l) // 2

            if isValid(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans