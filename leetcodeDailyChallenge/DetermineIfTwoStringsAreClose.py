# https://leetcode.com/problems/determine-if-two-strings-are-close/

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word1Map = {}
        word2Map = {}

        for i in range(len(word1)):
            word1Map[word1[i]] = 1 + word1Map.get(word1[i], 0)
            word2Map[word2[i]] = 1 + word2Map.get(word2[i], 0)

        for key in word1Map:
            if key not in word2Map:
                return False

        if sorted(list(word1Map.values())) == sorted(list(word2Map.values())):
            return True
        return False
