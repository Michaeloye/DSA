# https://leetcode.com/problems/circular-sentence/?envType=daily-question&envId=2024-11-02

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        i = 0
        words = sentence.split(" ")

        while i + 1 < len(words):
            if words[i][-1] != words[i + 1][0]:
                return False
            i += 1

        return True if words[0][0] == words[-1][-1] else False