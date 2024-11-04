# https://leetcode.com/problems/string-compression-iii/

class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        sepChars = []
        l = 0
        r = 0

        for r in range(1, len(word)):
            if word[r] != word[r - 1]:
                sepChars.append(word[l:r])
                l = r
        sepChars.append(word[l:r + 1])

        for split in sepChars:
            char = split[0]
            length = len(split)
            share = length // 9
            extra = length % 9

            while share:
                ans += "9" + char
                share -= 1
            if extra:
                ans += str(extra) + char
        return ans