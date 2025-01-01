# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        totalOnes = s.count("1")
        seenZeroes = 0
        seenOnes = 0

        ans = 0
        
        for i in range(len(s) - 1):
            seenZeroes += 1 if s[i] == "0" else 0
            seenOnes += 1 if s[i] == "1" else 0
            onesOnTheRight = totalOnes - seenOnes

            curr = seenZeroes + onesOnTheRight

            ans = max(ans, curr)

        return ans