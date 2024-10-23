# https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        curCost = 0
        res = 0
        l = 0

        for r in range(len(s)):
            difference = abs(ord(s[r]) - ord(t[r]))
            curCost += difference
            
            while curCost > maxCost:
                curCost -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            res = max(res, r - l + 1)

        return res