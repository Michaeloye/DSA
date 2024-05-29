# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letterCount = {}
        res = 0
        l = 0
        maxF = 0
        for r in range(len(s)):
            letterCount[s[r]] = 1 + letterCount.get(s[r], 0)
            maxF = max(maxF, letterCount[s[r]])
            windowLen = r - l + 1

            if windowLen - maxF > k:
                letterCount[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res