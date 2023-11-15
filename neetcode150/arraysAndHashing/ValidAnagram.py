# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterMap = {}

        for i in s:
            if i in letterMap:
                letterMap[i] = letterMap[i] + 1
            else:
                letterMap[i] = 1

        for j in t:
            if j in letterMap:
                letterMap[j] = letterMap[j] - 1
                if letterMap[j] == 0:
                    del letterMap[j]
            else:
                return False

        return not (bool(len(letterMap)))
