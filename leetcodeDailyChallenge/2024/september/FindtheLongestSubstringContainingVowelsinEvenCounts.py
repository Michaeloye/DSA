# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = "aeiou"
        ans = 0
        mask = 0
        maskToIdx = {0: -1}

        for i, c in enumerate(s):
            if c in vowels:
                mask = mask ^ (1 + ord(c) - ord('a'))
            if mask in maskToIdx:
                length = i - maskToIdx[mask]
                ans = max(ans, length)
            else:
                maskToIdx[mask] = i
        
        return ans
