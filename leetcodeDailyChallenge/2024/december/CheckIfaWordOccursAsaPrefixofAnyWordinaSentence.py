# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")

        for i, word in enumerate(words):
            j = 0
            seen = False
            while len(word) >= len(searchWord) and j < len(searchWord):
                if word[j] != searchWord[j]:
                    seen = False
                    break
                seen = True
                j += 1
            if seen:
                return i + 1
            
        return -1