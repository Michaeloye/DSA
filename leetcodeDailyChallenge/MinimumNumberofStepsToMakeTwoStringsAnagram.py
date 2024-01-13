# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCount = {}
        tCount = {}
        ans = 0

        for i in range(len(s)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            tCount[t[i]] = 1 + tCount.get(t[i], 0)

        for key in tCount:
            if key in sCount:
                sCount[key] -= tCount[key]

        for key in sCount:
            if sCount[key] > 0:
                ans += sCount[key]

        return ans
