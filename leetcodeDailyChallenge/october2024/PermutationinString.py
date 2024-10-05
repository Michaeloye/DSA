# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Map = Counter(s1)
        s2Map = {}
        r = len(s1) - 1

        for i in range(len(s1)):
            letter = s2[i]
            s2Map[letter] = 1 + s2Map.get(letter, 0)

        l = 0
        while r < len(s2):
            if s1Map == s2Map:
                return True

            s2Map[s2[l]] -= 1
            if s2Map[s2[l]] == 0:
                s2Map.pop(s2[l])
                
            l += 1
            r += 1
            if r < len(s2):
                s2Map[s2[r]] = 1 + s2Map.get(s2[r], 0)

        return False