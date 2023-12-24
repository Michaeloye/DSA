# https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pLetterMap = {}
        sLetterMap = {}

        for i in range(len(p)):
            pLetterMap[p[i]] = 1 + pLetterMap.get(p[i], 0)
            sLetterMap[s[i]] = 1 + sLetterMap.get(s[i], 0)

        ans = [0] if pLetterMap == sLetterMap else []

        l = 0
        for r in range(len(p), len(s)):
            sLetterMap[s[r]] = 1 + sLetterMap.get(s[r], 0)
            sLetterMap[s[l]] -= 1

            if sLetterMap[s[l]] == 0:
                sLetterMap.pop(s[l])

            l += 1

            if pLetterMap == sLetterMap:
                ans.append(l)

        return ans
