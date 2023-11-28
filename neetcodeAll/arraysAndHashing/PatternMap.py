# https://leetcode.com/problems/word-pattern

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternMap = {}
        sWords = s.split(" ")

        if len(pattern) != len(sWords):
            return False

        for idx, letter in enumerate(pattern):

            if letter in patternMap:
                if sWords[idx] != patternMap[letter]:
                    return False
                continue

            if sWords[idx] in set(patternMap.values()):
                return False

            patternMap[letter] = sWords[idx]

        return True
