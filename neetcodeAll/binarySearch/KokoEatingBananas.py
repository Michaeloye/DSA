# https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def getHours(k):
            h = 0

            for pile in piles:
                h += math.ceil(pile / k)

            return h

        l = 1
        r = max(piles)
        ans = r

        while l <= r:
            k = l + (r - l)//2
            curH = getHours(k)

            if curH <= h:
                ans = min(ans, k)
                r = k - 1
            elif curH > h:
                l = k + 1

        return ans