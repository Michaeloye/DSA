# https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        endIdx = -1
        arrWord = list(word)

        for i in range(len(arrWord)):
            if arrWord[i] == ch:
                endIdx = i
                break

        if endIdx == -1:
            return word
        
        l = 0
        while l <= endIdx:
            arrWord[l], arrWord[endIdx] = arrWord[endIdx], arrWord[l]
            l += 1
            endIdx -= 1
        
        return "".join(arrWord)
