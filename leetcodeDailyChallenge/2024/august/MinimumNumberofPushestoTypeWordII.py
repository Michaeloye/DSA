# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        letterCount = {}

        for l in word:
            letterCount[l] = 1 + letterCount.get(l, 0)
        
        letterCountArr = list(letterCount.values())
        letterCountArr.sort(reverse=True)

        i = 0
        ans = 0

        for count in letterCountArr:
            ans = ans + (count * ((i // 8) + 1))
            i += 1
        return ans