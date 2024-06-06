# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sPointer = 0
        tPointer = 0

        count = 0
        while sPointer < len(s) and tPointer < len(t):
            if s[sPointer] == t[tPointer]:
                count += 1
                tPointer += 1
            sPointer += 1

        res = len(t) - count

        return res
