# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i

class Solution:
    def maxDifference(self, s: str) -> int:
        maxOddCount = 0
        minEvenCount = len(s)
        sCount = {}

        for c in s:
            sCount[c] = 1 + sCount.get(c, 0)

        for count in sCount.values():
            if count % 2 == 0:
                minEvenCount = min(minEvenCount, count)
            else:
                maxOddCount = max(maxOddCount, count)

        ans = maxOddCount - minEvenCount
        return ans