# https://leetcode.com/problems/first-unique-character-in-a-string/?envType=daily-question&envId=2024-02-05

class Solution:
    def firstUniqChar(self, s: str) -> int:
        charsMap = {} # (idx, count)

        for i in range(len(s)):
            if s[i] in charsMap:
                charsMap[s[i]] = (i, charsMap[s[i]][1] + 1)
            else:
                charsMap[s[i]] = (i, 1)
        
        ans = float('inf')
        
        for key in charsMap:
            idx, count = charsMap[key]

            if count == 1:
                ans = min(ans, idx)
        
        return -1 if ans == float('inf') else ans