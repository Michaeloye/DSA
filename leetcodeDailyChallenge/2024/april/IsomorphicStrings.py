# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = {}
        tMap = {}

        for i in range(len(s)):
            if s[i] in sMap:
                val = sMap[s[i]]
                if val != t[i]:
                    return False
            if t[i] in tMap:
                val = tMap[t[i]]
                if val != s[i]:
                    return False
            sMap[s[i]] = t[i]
            tMap[t[i]] = s[i]
        return True