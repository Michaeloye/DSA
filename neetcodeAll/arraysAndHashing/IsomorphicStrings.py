# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        stringMap = {}
        for i, letter in enumerate(s):
            if letter not in stringMap:
                # check if that value in our hash map already exists
                if t[i] in set(stringMap.values()):
                    return False
                stringMap[letter] = t[i]

            if stringMap[s[i]] != t[i]:
                return False
        return True
